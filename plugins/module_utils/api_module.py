# Copyright: (c) 2021, Herve Quatremain <rv4m@yahoo.co.uk>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type

import socket
import json

from ansible.module_utils.basic import AnsibleModule, env_fallback

from ansible.module_utils.six.moves.urllib.parse import urlparse, urlencode
from ansible.module_utils.six.moves.urllib.error import HTTPError

from ansible.module_utils.urls import Request, SSLValidationError


class APIModuleError(Exception):
    """API request error exception.

    :param error_message: Error message.
    :type error_message: str
    """

    def __init__(self, error_message):
        """Initialize the object."""
        self.error_message = error_message

    def __str__(self):
        """Return the error message."""
        return self.error_message


class APIModule(AnsibleModule):
    """Ansible module for managing Red Hat Quay."""

    AUTH_ARGSPEC = dict(
        quay_host=dict(fallback=(env_fallback, ["QUAY_HOST"]), default="http://127.0.0.1"),
        quay_token=dict(no_log=True, fallback=(env_fallback, ["QUAY_TOKEN"])),
        validate_certs=dict(
            type="bool",
            aliases=["verify_ssl"],
            default=True,
            fallback=(env_fallback, ["QUAY_VERIFY_SSL"]),
        ),
    )

    def __init__(self, argument_spec, **kwargs):
        """Initialize the object."""
        full_argspec = {}
        full_argspec.update(APIModule.AUTH_ARGSPEC)
        full_argspec.update(argument_spec)

        super(APIModule, self).__init__(argument_spec=full_argspec, **kwargs)

        host = self.params.get("quay_host")

        # Try to parse the hostname as a URL
        try:
            self.host_url = urlparse(host, scheme="https")
        except Exception as e:
            self.fail_json(
                msg="Unable to parse quay_host as a URL ({host}): {error}".format(
                    host=host, error=e
                )
            )

        # Try to resolve the hostname
        try:
            socket.gethostbyname(self.host_url.hostname)
        except Exception as e:
            self.fail_json(
                msg="Unable to resolve quay_host ({host}): {error}".format(
                    host=self.host_url.hostname, error=e
                )
            )

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        token = self.params.get("quay_token")
        if token:
            headers["Authorization"] = "Bearer {token}".format(token=token)

        self.session = Request(
            validate_certs=self.params.get("validate_certs"), headers=headers
        )

        # Cache returns from API calls that get organization details
        self.cache_org = {}

    def build_url(self, endpoint, query_params=None):
        """Return a URL for the given endpoint.

        The URL is build as follows::

            https://<self.host_url>/api/v1/<endpoint>[?<query>]

        :param endpoint: Usually the API object name ("repository",
                         "superuser/users/", ...)
        :type endpoint: str
        :param query_params: The optional query to append to the URL
        :type query_params: dict

        :return: The full URL built from the given endpoint.
        :rtype: :py:class:``urllib.parse.ParseResult``
        """
        if not endpoint:
            api_path = "/api/v1/"
        else:
            api_path = "/api/v1/{endpoint}".format(endpoint=endpoint.lstrip("/"))
        url = self.host_url._replace(path=api_path)
        if query_params:
            url = url._replace(query=urlencode(query_params))
        return url

    def make_request(self, method, url, ok_error_codes=[404], **kwargs):
        """Perform an API call and return the retrieved data.

        :param method: GET, PUT, POST, or DELETE
        :type method: str
        :param url: URL to the API endpoint
        :type url: :py:class:``urllib.parse.ParseResult``
        :param ok_error_codes: HTTP error codes that are acceptable (not errors)
                               when returned by the API.
        :type ok_error_codes: list
        :param kwargs: Additionnal parameter to pass to the API (data
                       for PUT and POST requests, ...)

        :raises APIModuleError: The API request failed.

        :return: A dictionnary with two entries: ``status_code`` provides the
                 API call returned code and ``json`` provides the returned data
                 in JSON format.
        :rtype: dict
        """
        # In case someone is calling us directly; make sure we were given a
        # method, let's not just assume a GET
        if not method:
            raise Exception("The HTTP method must be provided.")

        # Extract the provided data
        data = json.dumps(kwargs.get("data", {}))

        try:
            response = self.session.open(method, url.geturl(), data=data)
        except SSLValidationError as ssl_err:
            raise APIModuleError(
                "Could not establish a secure connection to {host}: {error}.".format(
                    host=url.netloc, error=ssl_err
                )
            )
        except ConnectionError as con_err:
            raise APIModuleError(
                "Network error when trying to connect to {host}: {error}.".format(
                    host=url.netloc, error=con_err
                )
            )
        except HTTPError as he:
            if he.code in ok_error_codes:
                response = he
            # Sanity check: Did the server send back some kind of internal error?
            elif he.code >= 500:
                raise APIModuleError(
                    (
                        "The host sent back a server error: {path}: {error}."
                        " Please check the logs and try again later."
                    ).format(path=url.path, error=he)
                )
            # Sanity check: Did we fail to authenticate properly?
            # If so, fail out now; this is always a failure.
            elif he.code == 401:
                raise APIModuleError(
                    "Invalid authentication credentials for {path} (HTTP 401).".format(
                        path=url.path
                    )
                )
            # Sanity check: Did we get a forbidden response, which means that
            # the user isn't allowed to do this? Report that.
            elif he.code == 403:
                raise APIModuleError(
                    "You do not have permission to {method} {path} (HTTP 403).".format(
                        method=method, path=url.path
                    )
                )
            # Sanity check: Did we get a 404 response?
            # Requests with primary keys will return a 404 if there is no
            # response, and we want to consistently trap these.
            elif he.code == 405:
                raise APIModuleError(
                    "Cannot make a {method} request to this endpoint {path}.".format(
                        method=method, path=url.path
                    )
                )
            # Sanity check: Did we get some other kind of error?  If so, write
            # an appropriate error message.
            elif he.code >= 400:
                # We are going to return a 400 so the module can decide what to
                # do with it.
                response = he
            elif he.code == 204 and method == "DELETE":
                # A 204 is a normal response for a delete function
                response = he
            else:
                raise APIModuleError(
                    "Unexpected return code when calling {url}: {error}".format(
                        url=url.geturl(), error=he
                    )
                )
        except Exception as e:
            raise APIModuleError(
                (
                    "There was an unknown error when trying to connect"
                    " to {url}: {name}: {error}."
                ).format(name=type(e).__name__, error=e, url=url.geturl())
            )

        try:
            response_body = response.read()
        except Exception as e:
            raise APIModuleError(
                "Cannot read response from the {method} request to {path}: {error}.".format(
                    method=method, path=url.path, error=e
                )
            )

        response_json = {}
        if response_body:
            try:
                response_json = json.loads(response_body)
            except Exception as e:
                raise APIModuleError(
                    (
                        "Failed to parse the JSON response from the"
                        " {method} request to {path}: {error}."
                    ).format(method=method, path=url.path, error=e)
                )

        return {"status_code": response.status, "json": response_json}

    def get_error_message(self, response):
        """Return the error message provided in the API response.

        Example of messages returned by an API call:

            {
                "detail": "Requires authentication",
                "error_message": "Requires authentication",
                "error_type": "invalid_token",
                "title": "invalid_token",
                "type": "http://quay.example.com/api/v1/error/invalid_token",
                "status": 401
            }

        or
            {
                "message":"Invalid password, password must be at least 8
                           characters and contain no whitespace."
            }

        :param response: The response message from the API. This dictionary has
                         two keys: ``status_code`` provides the API call
                         returned code and ``json`` provides the returned data
                         in JSON format.
        :type response: dict

        :return: The error message or an empty string if the reponse does not
                 provide a message.
        :rtype: str
        """
        if not response or "json" not in response:
            return ""

        message = response["json"].get("message")
        if message:
            return message
        detail = response["json"].get("detail")
        error_message = response["json"].get("error_message")
        error_type = response["json"].get("error_type")
        title = response["json"].get("title")

        msg_fragments = []
        if title:
            msg_fragments.append(title)
        if error_type and error_type != title:
            msg_fragments.append(error_type)
        if error_message:
            msg_fragments.append(error_message)
        if detail and detail != error_message:
            msg_fragments.append(detail)
        return ": ".join(msg_fragments)

    def get_object_path(
        self, endpoint, query_params=None, exit_on_error=True, ok_error_codes=[404], **kwargs
    ):
        """Retrieve a single object from a GET API call.

        :param endpoint: API endpoint path. You can add path parameters in that
                         path by enclosing them in braces ``{}``.
                         For example, ``superuser/users/{username}``
        :type endpoint: str
        :param query_params: The optional query to append to the URL
        :type query_params: dict
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool
        :param ok_error_codes: HTTP error codes that are acceptable (not errors)
                               when returned by the API.
        :type ok_error_codes: list
        :param kwargs: Dictionnary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occured. That exception is only
                                raised when ``exit_on_error`` is ``False``.

        :return: The response from the API or ``None`` if the object does not
                 exist.
        :rtype: dict
        """
        for k in kwargs:
            endpoint = endpoint.replace("{" + k + "}", kwargs[k])

        url = self.build_url(endpoint, query_params=query_params)
        try:
            response = self.make_request("GET", url, ok_error_codes=ok_error_codes)
        except APIModuleError as e:
            if exit_on_error:
                self.fail_json(msg=str(e))
            else:
                raise

        if response["status_code"] in ok_error_codes:
            return None

        if response["status_code"] != 200:
            error_msg = self.get_error_message(response)
            if error_msg:
                fail_msg = "Unable to get {path}: {code}: {error}.".format(
                    path=url.path,
                    code=response["status_code"],
                    error=error_msg,
                )
            else:
                fail_msg = "Unable to get {path}: {code}.".format(
                    path=url.path,
                    code=response["status_code"],
                )
            if exit_on_error:
                self.fail_json(msg=fail_msg)
            else:
                raise APIModuleError(fail_msg)

        # Duplicate all attributes that have underscores (`_') in their name
        # with the same name but without the underscores. Some PUT data use
        # the attribute names without underscores.
        for k in response["json"].copy().keys():
            if "_" in k:
                response["json"][k.replace("_", "")] = response["json"][k]
        return response["json"]

    def delete(
        self,
        object,
        object_type,
        object_name,
        endpoint,
        auto_exit=True,
        exit_on_error=True,
        **kwargs
    ):
        """Delete an object.

        :param object: The object to delete. The function only uses that
                       parameter to decide if there is something to do. If
                       ``None`` then the function considers that the object
                       does no exist and therefore does not perform the DELETE
                       API call. This is usually the object you got from the
                       :py:meth:``get_object_path`` method.
        :type object: dict
        :param object_type: Type of the object to delete. Only used to return
                            error messages.
        :type object_type: str
        :param object_name: Name of the object to delete. Only used to return
                            error messages.
        :type object_name: str
        :param endpoint: API endpoint path. You can add path parameters in that
                         path by enclosing them in braces ``{}``.
                         For example, ``superuser/users/{username}``
        :type endpoint: str
        :param auto_exit: Exit the module when the API call is done.
        :type auto_exit: bool
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool
        :param kwargs: Dictionnary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occured. That exception is only
                                raised when ``exit_on_error`` is ``False``.

        :return: ``True`` if something has changed (object deleted), ``False``
                 otherwise.
        :rtype: bool
        """
        if object is None:
            if auto_exit:
                self.exit_json(changed=False)
            return False

        if self.check_mode:
            if auto_exit:
                self.exit_json(changed=True)
            return True

        for k in kwargs:
            endpoint = endpoint.replace("{" + k + "}", kwargs[k])

        url = self.build_url(endpoint)
        try:
            response = self.make_request("DELETE", url)
        except APIModuleError as e:
            if exit_on_error:
                self.fail_json(msg=str(e))
            else:
                raise

        # Success
        if response["status_code"] in [202, 204]:
            if auto_exit:
                self.exit_json(changed=True)
            return True

        # Failure
        error_msg = self.get_error_message(response)
        if error_msg:
            fail_msg = "Unable to delete {object_type} {name}: {error}".format(
                object_type=object_type, name=object_name, error=error_msg
            )
        else:
            fail_msg = "Unable to delete {object_type} {name}: {code}".format(
                object_type=object_type,
                name=object_name,
                code=response["status_code"],
            )
        if exit_on_error:
            self.fail_json(msg=fail_msg)
        else:
            raise APIModuleError(fail_msg)

    def create(
        self,
        object_type,
        object_name,
        endpoint,
        new_item,
        auto_exit=True,
        exit_on_error=True,
        ok_error_codes=[200, 201, 204],
        **kwargs
    ):
        """Create an object.

        :param object_type: Type of the object to create. Only used to return
                            error messages.
        :type object_type: str
        :param object_name: Name of the object to create. Only used to return
                            error messages.
        :type object_name: str
        :param endpoint: API endpoint path. You can add path parameters in that
                         path by enclosing them in braces ``{}``. For example,
                         ``organization/{orgname}/applications``
        :type endpoint: str
        :param new_item: The data to pass to the API call. This provides the
                         object details. For example,
                         ``{"username": "jdoe","email":"jdoe@example.com"}``
        :type new_item: dict
        :param auto_exit: Exit the module when the API call is done.
        :type auto_exit: bool
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool
        :param ok_error_codes: HTTP error codes that are acceptable (not errors)
                               when returned by the API.
        :type ok_error_codes: list
        :param kwargs: Dictionnary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"orgname":"devel"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occured. That exception is only
                                raised when ``exit_on_error`` is ``False``.

        :return: The data returned by the API call.
        :rtype: dict
        """
        if self.check_mode:
            if auto_exit:
                self.exit_json(changed=True)
            return {}

        for k in kwargs:
            endpoint = endpoint.replace("{" + k + "}", kwargs[k])

        url = self.build_url(endpoint)
        try:
            response = self.make_request(
                "POST", url, ok_error_codes=ok_error_codes, data=new_item
            )
        except APIModuleError as e:
            if exit_on_error:
                self.fail_json(msg=str(e))
            else:
                raise

        # Success
        if response["status_code"] in ok_error_codes:
            if auto_exit:
                self.exit_json(changed=True)
            return response.get("json", {})

        # Failure
        error_msg = self.get_error_message(response)
        if error_msg:
            fail_msg = "Unable to create {object_type} {name}: {error}".format(
                object_type=object_type, name=object_name, error=error_msg
            )
        else:
            fail_msg = "Unable to create {object_type} {name}: {code}".format(
                object_type=object_type,
                name=object_name,
                code=response["status_code"],
            )
        if exit_on_error:
            self.fail_json(msg=fail_msg)
        else:
            raise APIModuleError(fail_msg)

    def unconditional_update(
        self, object_type, object_name, endpoint, new_item, exit_on_error=True, **kwargs
    ):
        """Update an object without checking if it needs to be updated.

        :param object_type: Type of the object to update. Only used to return
                            error messages.
        :type object_type: str
        :param object_name: Name of the object to update. Only used to return
                            error messages.
        :type object_name: str
        :param endpoint: API endpoint path. You can add path parameters in that
                         path by enclosing them in braces ``{}``.
                         For example, ``superuser/users/{username}``
        :type endpoint: str
        :param new_item: The data to pass to the API call. This provides the
                         object details. For example,
                         ``{"enabled": False,"password":"Sup3r53cr3t"}``
        :type new_item: dict
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool
        :param kwargs: Dictionnary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occured. That exception is only
                                raised when ``exit_on_error`` is ``False``.

        :return: The data returned by the API call.
        :rtype: dict
        """
        if self.check_mode:
            return {}

        for k in kwargs:
            endpoint = endpoint.replace("{" + k + "}", kwargs[k])

        url = self.build_url(endpoint)
        try:
            response = self.make_request("PUT", url, data=new_item)
        except APIModuleError as e:
            if exit_on_error:
                self.fail_json(msg=str(e))
            else:
                raise

        # Failure
        if response["status_code"] not in [200, 201]:
            error_msg = self.get_error_message(response)
            if error_msg:
                fail_msg = "Unable to update {object_type} {name}: {error}".format(
                    object_type=object_type, name=object_name, error=error_msg
                )
            else:
                fail_msg = "Unable to update {object_type} {name}: {code}".format(
                    object_type=object_type,
                    name=object_name,
                    code=response["status_code"],
                )
            if exit_on_error:
                self.fail_json(msg=fail_msg)
            else:
                raise APIModuleError(fail_msg)

        return response.get("json", {})

    def need_update(self, object_type, object_name, old, new):
        """Tell if the new dictionary is a subset of the old one.

        This method is used to decide if the object must be updated (PUT) or
        not. If no new attribute, or no attribute change, then no need to
        call the API.

        :param object_type: Type of the object to update. Only used to return
                            error messages.
        :type object_type: str
        :param object_name: Name of the object to update. Only used to return
                            error messages.
        :type object_name: str
        :param old: The old object parameters.
        :type old: dict
        :param new: The new object parameters.
        :type new: dict

        :return: ``True`` is the new dictionary contains items not in the old
                 one. ``False`` otherwise.
        :rtype: bool
        """
        if old is None:
            old = {}
        for k in new:
            if k == "password":
                self.warn(
                    (
                        "The password field of {object_type} {name} has encrypted"
                        " data and may inaccurately report task is changed."
                    ).format(object_type=object_type, name=object_name)
                )
                return True

            if new.get(k) != old.get(k):
                return True
        return False

    def update(
        self,
        object,
        object_type,
        object_name,
        endpoint,
        new_item,
        auto_exit=True,
        exit_on_error=True,
        **kwargs
    ):
        """Update an object.

        :param object: The object to update. This is usually the object you got
                       from the :py:meth:``get_object_path`` method.
        :param object_type: Type of the object to update. Only used to return
                            error messages.
        :type object_type: str
        :param object_name: Name of the object to update. Only used to return
                            error messages.
        :type object_name: str
        :param endpoint: API endpoint path. You can add path parameters in that
                         path by enclosing them in braces ``{}``.
                         For example, ``superuser/users/{username}``
        :type endpoint: str
        :param new_item: The data to pass to the API call. This provides the
                         object details. For example,
                         ``{"enabled": False,"password":"Sup3r53cr3t"}``
        :type new_item: dict
        :param auto_exit: Exit the module when the API call is done.
        :type auto_exit: bool
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool
        :param kwargs: Dictionnary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occured. That exception is only
                                raised when ``exit_on_error`` is ``False``.

        :return: A tuple. The first item is ``True`` if something has changed
                 (object updated), ``False`` otherwise. The second item is a
                 dictionary that contains the data sent back by the API call.
        :rtype: list
        """
        needs_patch = self.need_update(object_type, object_name, object, new_item)

        # No change
        if not needs_patch:
            if auto_exit:
                self.exit_json(changed=False)
            return (False, {})

        # Check mode
        if self.check_mode:
            if auto_exit:
                self.exit_json(changed=True)
            return (True, new_item)

        data = self.unconditional_update(
            object_type,
            object_name,
            endpoint,
            new_item,
            exit_on_error=exit_on_error,
            **kwargs
        )

        # Success. Something has been changed
        if auto_exit:
            self.exit_json(changed=True)
        return (True, data)

    def who_am_i(self, exit_on_error=True):
        """Return the current user name.

        The user account used to access the API is defined by the token (who
        generated the token).

        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool

        :return: The name of the current user.
        :rtype: str
        """
        user = self.get_object_path("user/", exit_on_error=exit_on_error)
        return user.get("username")

    def get_account(self, account_name, exit_on_error=True):
        """Search for the given user account (user or robot).

        :param account_name: The account name to look for.
        :type account_name: str
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool

        :return: The user description or None if the user account cannot be
                 found. The returned dictionnary includes the ``is_robot`` key
                 which indicates if the account is a robot account (``True``)
                 or a user account (``False``).
        :rtype: dict or None
        """
        # Robot account
        try:
            namespace, robot_shortname = account_name.split("+", 1)
        except ValueError:
            pass
        else:
            # Checking if it is an organization robot account
            robot = self.get_object_path(
                "organization/{orgname}/robots/{robot_shortname}",
                ok_error_codes=[400, 404],
                exit_on_error=exit_on_error,
                orgname=namespace,
                robot_shortname=robot_shortname,
            )
            if robot:
                robot["is_organization"] = False
                robot["is_robot"] = True
                return robot
            # Checking if it is a robot account for the current user
            if self.who_am_i(exit_on_error=exit_on_error) != namespace:
                return None
            robot = self.get_object_path(
                "user/robots/{robot_shortname}",
                ok_error_codes=[400, 404],
                exit_on_error=exit_on_error,
                robot_shortname=robot_shortname,
            )
            if robot:
                robot["is_organization"] = False
                robot["is_robot"] = True
                return robot
            return None

        # Robot account for the current user (no prefix `<namespace>+' in the
        # given name)
        robot = self.get_object_path(
            "user/robots/{robot_shortname}",
            ok_error_codes=[400, 404],
            exit_on_error=exit_on_error,
            robot_shortname=account_name,
        )
        if isinstance(robot, dict) and robot:
            robot["is_organization"] = False
            robot["is_robot"] = True
            return robot

        # User account
        user = self.get_object_path(
            "users/{user}", exit_on_error=exit_on_error, user=account_name
        )
        if isinstance(user, dict) and user:
            user["name"] = user.get("username")
            user["is_organization"] = False
            user["is_robot"] = False
            return user
        return None

    def get_team(self, organization, team_name, exit_on_error=True):
        """Search for the given team.

        :param organization: The name of the organization to look for the team.
        :type organization: str
        :param team_name: The name of the team to look for.
        :type team_name: str
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool

        :return: The team description or None if the team cannot be found.
        :rtype: dict or None
        """
        org_details = self.get_organization(organization, exit_on_error=exit_on_error)
        if not org_details:
            return None
        return org_details["teams"].get(team_name, None) if "teams" in org_details else None

    def get_organization(self, organization, exit_on_error=True):
        """Search for the given organization.

        :param organization: The name of the organization to look for.
        :type organization: str
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool

        :return: The organization details or None if the organization cannot
                 be found.
        :rtype: dict or None
        """
        # Get the organization details from the given name.
        #
        # GET /api/v1/organization/{orgname}
        # {
        #   "name": "production",
        #   "email": "f87e5706-54ad-4c47-ab5c-81867468e313",
        #   "avatar": {
        #     "name": "myorg",
        #     "hash": "66bf...1252",
        #     "color": "#d62728",
        #     "kind": "user"
        #   },
        #   "is_admin": true,
        #   "is_member": true,
        #   "teams": {
        #     "owners": {
        #       "name": "owners",
        #       "description": "",
        #       "role": "admin",
        #       "avatar": {
        #         "name": "owners",
        #         "hash": "6f0e...8d90",
        #         "color": "#c7c7c7",
        #         "kind": "team"
        #       },
        #       "can_view": true,
        #       "repo_count": 0,
        #       "member_count": 1,
        #       "is_synced": false
        #     },
        #     "teamxyz": {
        #       "name": "teamxyz",
        #       "description": "My team description",
        #       "role": "member",
        #       "avatar": {
        #         "name": "teamxyz",
        #         "hash": "bf1e...1414",
        #         "color": "#a55194",
        #         "kind": "team"
        #       },
        #       "can_view": true,
        #       "repo_count": 0,
        #       "member_count": 0,
        #       "is_synced": false
        #     }
        #   },
        #   "ordered_teams": [
        #     "owners",
        #     "team1",
        #     "teamxyz"
        #   ],
        #   "invoice_email": false,
        #   "invoice_email_address": null,
        #   "tag_expiration_s": 86400,
        #   "is_free_account": true
        # }
        if organization in self.cache_org:
            return self.cache_org[organization]
        org_details = self.get_object_path(
            "organization/{orgname}", exit_on_error=exit_on_error, orgname=organization
        )
        if isinstance(org_details, dict) and org_details:
            org_details["is_organization"] = True
        else:
            org_details = None
        self.cache_org[organization] = org_details
        return org_details

    def get_namespace(self, namespace, exit_on_error=True):
        """Search for the given namespace.

        A namespace can be an organization or a user private namespace.

        :param namespace: The name of the namespace to look for.
        :type namespace: str
        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool

        :return: The namespace details or None if the namespace cannot be found.
                 If the namespace has been found, then the returned dictionary
                 includes the ``is_organization`` key which is ``True`` if the
                 namespace is an organization, or ``False`` is the namespace
                 is a user private namespace.
        :rtype: dict or None
        """
        org_details = self.get_organization(namespace, exit_on_error=exit_on_error)
        if org_details:
            return org_details

        user_details = self.get_account(namespace, exit_on_error=exit_on_error)
        if user_details and not user_details.get("is_robot"):
            return user_details
        return None
