# Copyright: (c) 2021-2024, Herve Quatremain <herve.quatremain@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type

import socket
import json
import re

from ansible.module_utils.basic import AnsibleModule, env_fallback
from ansible.module_utils._text import to_text
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
    """Ansible module for managing Quay Container Registry."""

    AUTH_ARGSPEC = dict(
        quay_host=dict(fallback=(env_fallback, ["QUAY_HOST"]), default="http://127.0.0.1"),
        quay_token=dict(no_log=True, fallback=(env_fallback, ["QUAY_TOKEN"])),
        quay_username=dict(fallback=(env_fallback, ["QUAY_USERNAME"])),
        quay_password=dict(no_log=True, fallback=(env_fallback, ["QUAY_PASSWORD"])),
        validate_certs=dict(
            type="bool",
            aliases=["verify_ssl"],
            default=True,
            fallback=(env_fallback, ["QUAY_VERIFY_SSL"]),
        ),
    )

    MUTUALLY_EXCLUSIVE = [
        ("quay_username", "quay_token"),
        ("quay_password", "quay_token"),
    ]

    REQUIRED_TOGETHER = [("quay_username", "quay_password")]

    def __init__(self, argument_spec, **kwargs):
        """Initialize the object.

        Sets:
        * :py:attr:``self.host_url``: :py:class:``urllib.parse.ParseResult``
          object that represents the base URL of the Quay server.
        * :py:attr:``self.authenticated``: Indicate if authentication must be
          performed (from the `quay_token' parameter) or if access is
          anonymous.
        * :py:attr:``self.cache_org``: Dictionary that is used to cache
          organization details. Keys are organization names.
        """
        self.authenticated = False
        self.token_authenticated = False

        full_argspec = {}
        full_argspec.update(self.AUTH_ARGSPEC)
        full_argspec.update(argument_spec)

        kwargs["mutually_exclusive"] = (
            kwargs.get("mutually_exclusive", []) + self.MUTUALLY_EXCLUSIVE
        )

        kwargs["required_together"] = (
            kwargs.get("required_together", []) + self.REQUIRED_TOGETHER
        )

        super(APIModule, self).__init__(argument_spec=full_argspec, **kwargs)

        host = self.params.get("quay_host")

        if not host.startswith("https://") and not host.startswith("http://"):
            host = "https://{host}".format(host=host)

        # Try to parse the hostname as a URL
        try:
            self.host_url = urlparse(host)
        except Exception as e:
            self.fail_json(
                msg="Unable to parse `quay_host' as a URL ({host}): {error}".format(
                    host=host, error=e
                )
            )

        # Try to resolve the hostname
        try:
            socket.gethostbyname(self.host_url.hostname)
        except Exception as e:
            self.fail_json(
                msg="Unable to resolve `quay_host' ({host}): {error}".format(
                    host=self.host_url.hostname, error=e
                )
            )

        # Create a network session object
        self.create_session()

        # Authenticate
        token = self.params.get("quay_token")
        if token:
            self.token_authenticated = True
            self.authenticated = True
            self.session.headers.update(
                {"Authorization": "Bearer {token}".format(token=token)}
            )
        else:
            token = self.authenticate()
            if token:
                self.session.headers.update({"X-CSRF-Token": token})
                self.authenticated = True
        self.token = token

        # Cache returns from API calls that get organization details
        self.cache_org = {}

    def create_session(self):
        """Create a network session.

        The session preserves cookies and headers between calls.
        """
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.session = Request(
            validate_certs=self.params.get("validate_certs"), headers=headers
        )

    def authenticate(self):
        """Authenticate by using a username and a password.

        :return: The session token.
        :rtype: str
        """
        username = self.params.get("quay_username")
        password = self.params.get("quay_password")
        if not username or not password:
            return None

        # Retrieve the CSRF cookie and token from the root page (GET /)
        url = self.host_url._replace(path="/")
        headers = {"Accept": "*/*"}
        try:
            html = self.make_raw_request("GET", url, headers=headers)
        except APIModuleError as e:
            self.fail_json(msg=str(e))
        try:
            csrf = re.search(r"window.__token\s*=\s*'(.*?)';", to_text(html["body"])).group(1)
        except AttributeError:
            self.fail_json(msg="Cannot retrieve the CSRF token from the returned data")

        # Log in to the web UI (POST /api/v1/signin)
        url = self.build_url("signin")
        headers = {"X-CSRF-Token": csrf}
        data = {"username": username, "password": password}
        try:
            response = self.make_json_request("POST", url, headers=headers, data=data)
        except APIModuleError as e:
            self.fail_json(msg=str(e))

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
            self.fail_json(msg=fail_msg)

        # Get the X-CSRF-Token header
        # Depending on the Quay version the headers might not be in lowercase
        headers_lower = dict((k.lower(), v) for k, v in response["headers"].items())
        token = headers_lower.get("x-next-csrf-token")
        if token is None:
            self.fail_json(msg="Cannot retrieve the authentication token")
        return token

    def logout(self):
        """Logout."""
        if self.authenticated and not self.token_authenticated:
            url = self.build_url("signout")
            try:
                self.make_json_request("POST", url)
            except APIModuleError:
                pass
        self.authenticated = False
        self.create_session()

    def fail_json(self, **kwargs):
        """Logout and then exit with an error."""
        self.logout()
        super(APIModule, self).fail_json(**kwargs)

    def exit_json(self, **kwargs):
        """Logout and then exit the module."""
        self.logout()
        super(APIModule, self).exit_json(**kwargs)

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

    def make_raw_request(self, method, url, ok_error_codes=None, **kwargs):
        """Perform an API call and return the retrieved data.

        :param method: GET, PUT, POST, or DELETE
        :type method: str
        :param url: URL to the API endpoint
        :type url: :py:class:``urllib.parse.ParseResult``
        :param ok_error_codes: HTTP error codes that are acceptable (not errors)
                               when returned by the API. 404 by default.
        :type ok_error_codes: list
        :param kwargs: Additional parameter to pass to the API (headers, data
                       for PUT and POST requests, ...)

        :raises APIModuleError: The API request failed.

        :return: A dictionary with three entries: ``status_code`` provides the
                 API call returned code, ``body`` provides the returned data,
                 and ``headers`` provides the returned headers (dictionary)
        :rtype: dict
        """
        if ok_error_codes is None:
            ok_error_codes = [404]
        # In case someone is calling us directly; make sure we were given a
        # method, let's not just assume a GET
        if not method:
            raise Exception("The HTTP method must be provided.")

        # Extract the provided headers and data
        headers = kwargs.get("headers", {})
        data = kwargs.get("data")
        if isinstance(data, dict):
            data = json.dumps(data)
        follow_redirects = kwargs.get("follow_redirects")

        try:
            if follow_redirects is not None:
                response = self.session.open(
                    method,
                    url.geturl(),
                    headers=headers,
                    data=data,
                    follow_redirects=follow_redirects,
                )
            else:
                response = self.session.open(method, url.geturl(), headers=headers, data=data)
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
                    "Authentication required for {path} (HTTP 401).".format(path=url.path)
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
            # Convert the list of tuples to a dictionary
            response_headers = {}
            for r in response.getheaders():
                response_headers[r[0]] = r[1]
        except Exception as e:
            raise APIModuleError(
                "Cannot read response from the {method} request to {path}: {error}.".format(
                    method=method, path=url.path, error=e
                )
            )

        return {
            "status_code": response.status,
            "body": response_body,
            "headers": response_headers,
        }

    def make_json_request(self, method, url, ok_error_codes=None, **kwargs):
        """Perform an API call and return the retrieved JSON data.

        :param method: GET, PUT, POST, or DELETE
        :type method: str
        :param url: URL to the API endpoint
        :type url: :py:class:``urllib.parse.ParseResult``
        :param ok_error_codes: HTTP error codes that are acceptable (not errors)
                               when returned by the API. 404 by default.
        :type ok_error_codes: list
        :param kwargs: Additional parameter to pass to the API (data
                       for PUT and POST requests, ...)

        :raises APIModuleError: The API request failed.

        :return: A dictionary with three entries: ``status_code`` provides the
                 API call returned code, ``json`` provides the returned data
                 in JSON format, and ``headers`` provides the returned headers
                 (dictionary)
        :rtype: dict
        """
        response = self.make_raw_request(method, url, ok_error_codes, **kwargs)
        response_body = response.get("body")
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

        return {
            "status_code": response["status_code"],
            "json": response_json,
            "headers": response["headers"],
        }

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

        :return: The error message or an empty string if the response does not
                 provide a message.
        :rtype: str
        """
        if not response or "json" not in response:
            return ""

        # Some API calls do not return JSON, but a string
        if isinstance(response["json"], str):
            return response["json"]

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
        self, endpoint, query_params=None, exit_on_error=True, ok_error_codes=None, **kwargs
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
                               when returned by the API. 404 by default.
        :type ok_error_codes: list
        :param kwargs: Dictionary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occurred. That exception is only
                                raised when ``exit_on_error`` is ``False``.

        :return: The response from the API or ``None`` if the object does not
                 exist.
        :rtype: dict
        """
        if ok_error_codes is None:
            ok_error_codes = [404]
        for k in kwargs:
            endpoint = endpoint.replace("{" + k + "}", kwargs[k])

        url = self.build_url(endpoint, query_params=query_params)
        try:
            response = self.make_json_request("GET", url, ok_error_codes=ok_error_codes)
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
        try:
            for k in response["json"].copy().keys():
                if "_" in k:
                    response["json"][k.replace("_", "")] = response["json"][k]
        except AttributeError:
            pass
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
        :param kwargs: Dictionary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occurred. That exception is only
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
            response = self.make_json_request("DELETE", url)
        except APIModuleError as e:
            if exit_on_error:
                self.fail_json(msg=str(e))
            else:
                raise

        # Success
        if response["status_code"] in [200, 201, 202, 204]:
            if auto_exit:
                self.exit_json(changed=True)
            return True

        # Object not found
        if response["status_code"] in [400, 404]:
            if auto_exit:
                self.exit_json(changed=False)
            return False

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
        ok_error_codes=None,
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
                               when returned by the API. 200, 201, and 204 by
                               default.
        :type ok_error_codes: list
        :param kwargs: Dictionary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"orgname":"devel"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occurred. That exception is only
                                raised when ``exit_on_error`` is ``False``.

        :return: The data returned by the API call.
        :rtype: dict
        """
        if ok_error_codes is None:
            ok_error_codes = [200, 201, 204]
        if self.check_mode:
            if auto_exit:
                self.exit_json(changed=True)
            return {}

        for k in kwargs:
            endpoint = endpoint.replace("{" + k + "}", kwargs[k])

        url = self.build_url(endpoint)
        try:
            response = self.make_json_request(
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
        :param kwargs: Dictionary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occurred. That exception is only
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
            response = self.make_json_request("PUT", url, data=new_item)
        except APIModuleError as e:
            if exit_on_error:
                self.fail_json(msg=str(e))
            else:
                raise

        # Failure
        if response["status_code"] not in [200, 201, 204]:
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
        :param kwargs: Dictionary used to substitute parameters in the given
                       ``endpoint`` string. For example ``{"username":"jdoe"}``
        :type kwargs: dict

        :raises APIModuleError: An API error occurred. That exception is only
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
        If the `quay_token' parameter has not been provided, then all the
        API calls are anonymous and the method returns ``None``.

        :param exit_on_error: If ``True`` (the default), exit the module on API
                              error. Otherwise, raise the
                              :py:class:``APIModuleError`` exception.
        :type exit_on_error: bool

        :return: The name of the current user or None if access to the API is
                 anonymous.
        :rtype: str
        """
        if not self.authenticated:
            return None
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
                 found. The returned dictionary includes the ``is_robot`` key
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
        if self.authenticated:
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

        # User account.
        #
        # Uses the "entities" (search) endpoint rather than the "users"
        # endpoint because the "users" endpoint only returns the users already
        # defined in the internal database. LDAP users that have not yet been
        # used in Quay are not in the internal database and are not returned
        # when using the "users" endpoint.
        #
        # GET /api/v1/entities/user9
        # {
        #   "results": [
        #     {
        #       "name": "user9",
        #       "kind": "external",
        #       "title": "user9@example.com",
        #       "avatar": {
        #         "name": "user9",
        #         "hash": "b1e7...098e",
        #         "color": "#1f77b4",
        #         "kind": "user"
        #       }
        #     },
        #     {
        #       "name": "user911",
        #       "kind": "external",
        #       "title": "user911@example.com",
        #       "avatar": {
        #         "name": "user911",
        #         "hash": "5f67...3016",
        #         "color": "#a55194",
        #         "kind": "user"
        #       }
        #     },
        #     {
        #       "name": "user912",
        #       "kind": "external",
        #       "title": "user912@example.com",
        #       "avatar": {
        #         "name": "user912",
        #         "hash": "7587...20ab",
        #         "color": "#5254a3",
        #         "kind": "user"
        #       }
        #     }
        #   ]
        # }
        user = self.get_object_path(
            "entities/{user}",
            query_params={"includeOrgs": False, "includeTeams": False},
            exit_on_error=exit_on_error,
            user=account_name,
        )
        if isinstance(user, dict) and len(user.get("results", [])) != 0:
            # Search for an exact match for the username
            for res in user["results"]:
                if res.get("name") == account_name:
                    break
            else:
                return None
            user["name"] = account_name
            user["is_organization"] = False
            user["is_robot"] = False
            # The LDAP user account is not yet declared into the Quay internal
            # database. Add it.
            if res.get("kind") == "external":
                try:
                    self.create(
                        "user",
                        user["name"],
                        "entities/link/{user}",
                        {},
                        auto_exit=False,
                        exit_on_error=False,
                        user=user["name"],
                    )
                except APIModuleError:
                    pass
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

    def get_tags(self, namespace, repository, tag=None, digest=None, only_active_tags=True):
        """Return the list of tags for the given repository.

        :param namespace: The name of the repository's namespace.
        :type namespace: str
        :param repository: The name of the repository.
        :type repository: str
        :param tag: The tag to retrieve and return. If ``None`` (the default),
                    then the :py:attribute:``digest`` is used instead. If that
                    attribute is also not set, then all the tags for the given
                    repository are returned.
        :type tag: str
        :param digest: The image digest to search for. Only used if the
                       :py:attribute:``tag`` attribute is None.
        :type digest: str
        :param only_active_tags: If ``True`` (the default), then only return
                                 active tags.
        :type only_active_tags: bool

        :return: The list of tags or an empty list if no tag has been retrieved.
                 Each item in the list is the dictionary retrieved from the API.
                 For example::

                    [
                        {
                            "name": "1.33.0",
                            "reversion": False,
                            "start_ts": 1632982224,
                            "manifest_digest": "sha256:f948...95fe",
                            "is_manifest_list": False,
                            "size": 784606,
                            "last_modified": "Thu, 30 Sep 2021 06:10:24 -0000"
                        },
                        {
                            "name": "latest",
                            "reversion": False,
                            "start_ts": 1632982222,
                            "manifest_digest": "sha256:9ce9...f3c7",
                            "is_manifest_list": False,
                            "size": 784538,
                            "last_modified": "Thu, 30 Sep 2021 06:10:22 -0000"
                        },
                        {
                            "name": "1.34.0",
                            "reversion": False,
                            "start_ts": 1632982221,
                            "end_ts": 1640336040,
                            "manifest_digest": "sha256:a8f2...5ea7",
                            "is_manifest_list": False,
                            "size": 802700,
                            "last_modified": "Thu, 30 Sep 2021 06:10:21 -0000",
                            "expiration": "Fri, 24 Dec 2021 08:54:00 -0000"
                        }
                    ]
        """
        # Get the tags
        #
        # GET /api/v1/repository/{namespace}/{repository}/tag/?specificTag={tag}
        # {
        # "tags": [
        #     {
        #     "name": "v0.5.0",
        #     "reversion": false,
        #     "start_ts": 1510871118,
        #     "manifest_digest": "sha256:9107...5377",
        #     "is_manifest_list": false,
        #     "size": 0,
        #     "last_modified": "Thu, 16 Nov 2017 22:25:18 -0000"
        #     },
        #     {
        #     "name": "latest",
        #     "reversion": false,
        #     "start_ts": 1510871113,
        #     "manifest_digest": "sha256:53b2...a7c8",
        #     "is_manifest_list": false,
        #     "size": 0,
        #     "last_modified": "Thu, 16 Nov 2017 22:25:13 -0000"
        #     },
        #     {
        #     "name": "v0.4.1",
        #     "reversion": false,
        #     "start_ts": 1501630807,
        #     "manifest_digest": "sha256:06f2...bee4",
        #     "is_manifest_list": false,
        #     "size": 0,
        #     "last_modified": "Tue, 01 Aug 2017 23:40:07 -0000"
        #     },
        #     {
        #     "name": "v0.4.0",
        #     "reversion": false,
        #     "start_ts": 1492586027,
        #     "manifest_digest": "sha256:4472...6ecb",
        #     "is_manifest_list": false,
        #     "size": 0,
        #     "last_modified": "Wed, 19 Apr 2017 07:13:47 -0000"
        #     },
        #     {
        #     "name": "v0.3.0",
        #     "reversion": false,
        #     "start_ts": 1471626798,
        #     "manifest_digest": "sha256:0b92...1747",
        #     "is_manifest_list": false,
        #     "size": 8584000,
        #     "last_modified": "Fri, 19 Aug 2016 17:13:18 -0000"
        #     }
        # ],
        # "page": 1,
        # "has_additional": false
        # }
        query_params = {"onlyActiveTags": only_active_tags, "limit": 100}
        if tag:
            query_params["specificTag"] = tag
        tag_list = []
        page = 1
        while True:
            query_params["page"] = page

            tags = self.get_object_path(
                "repository/{namespace}/{repository}/tag/",
                query_params=query_params,
                namespace=namespace,
                repository=repository,
            )
            if tags:
                if tag or not digest:
                    tag_list.extend(tags.get("tags", []))
                else:
                    tag_list.extend(
                        [
                            t
                            for t in tags.get("tags", [])
                            if t.get("manifest_digest") == digest
                        ]
                    )
                if tags.get("has_additional", False):
                    page += 1
                    continue
            break
        return tag_list


class APIModuleNoAuth(APIModule):
    AUTH_ARGSPEC = dict(
        quay_host=dict(fallback=(env_fallback, ["QUAY_HOST"]), default="http://127.0.0.1"),
        validate_certs=dict(
            type="bool",
            aliases=["verify_ssl"],
            default=True,
            fallback=(env_fallback, ["QUAY_VERIFY_SSL"]),
        ),
    )
    MUTUALLY_EXCLUSIVE = []
    REQUIRED_TOGETHER = []
