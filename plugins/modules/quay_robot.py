#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021-2024, Herve Quatremain <herve.quatremain@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# For accessing the API documentation from a running system, use the swagger-ui
# container image:
#
#  $ podman run -p 8888:8080 --name=swag -d --rm \
#      -e API_URL=http://your.quay.installation:8080/api/v1/discovery \
#      docker.io/swaggerapi/swagger-ui
#
#  (replace the hostname and port in API_URL with your own installation)
#
# And then navigate to http://localhost:8888
#
# Notes:
#  - You cannot rename robot accounts.
#  - You cannot update the description of robot accounts.
#  - The current user can create/delete robot accounts in their personal
#    namespace, but not in the namespace of other users.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_robot
short_description: Manage Quay Container Registry robot accounts
description:
  - Create and delete robot accounts.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the robot account to create or remove, in the format
        C(namespace)+C(shortname). The namespace can be an organization or a
        personal namespace.
      - The short name (the part after the C(+) sign) must be in lowercase,
        must not contain white spaces, must not start by a digit, and must be
        at least two characters long.
      - If you omit the namespace part in the name, then the module uses your
        personal namespace.
      - You can create and delete robot accounts in your personal namespace,
        but not in the personal namespace of other users. The token you use in
        I(quay_token) determines the user account you are using.
    required: true
    type: str
  description:
    description:
      - Description of the robot account. You cannot update the description
        of existing robot accounts.
    type: str
  state:
    description:
      - If C(absent), then the module deletes the robot account.
      - The module does not fail if the account does not exist, because the
        state is already as expected.
      - If C(present), then the module creates the robot account if it does not
        already exist.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure the robot account production+robotprod1 exists
  herve4m.quay.quay_robot:
    name: production+robotprod1
    description: Robot account for production
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: robot_details

- ansible.builtin.debug:
    msg: "Robot token: {{ robot_details['token'] }}"

- ansible.builtin.debug:
    msg: "Docker configuration (Base64): {{ robot_details['name']
      | herve4m.quay.quay_docker_config(robot_details['token'],
      'https://quay.example.com') }}"

- name: Ensure the robot account myrobot exists in my namespace
  herve4m.quay.quay_robot:
    name: myrobot
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the robot account production+robotdev1 does not exists
  herve4m.quay.quay_robot:
    name: production+robotdev1
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r"""
name:
  description:
    - Token name.
    - From this name and the token, in I(token), you can construct a Docker
      configuration file that you can use to manage images in the container
      image registry. See P(herve4m.quay.quay_docker_config#filter).
  returned: changed
  type: str
  sample: production+robotprod1
token:
  description: Robot credential (token).
  returned: changed
  type: str
  sample: IWG3K5EW92KZLPP42PMOKM5CJ2DEAQMSCU33A35NR7MNL21004NKVP3BECOWSQP2
"""

from ..module_utils.api_module import APIModule


def exit_module(module, changed, data):
    """Exit the module and return data.

    :param module: The module object.
    :type module: :py:class:``APIModule``
    :param changed: The changed status of the object.
    :type changed: bool
    :param data: The data returned by the API call.
    :type data: dict
    """
    result = {"changed": changed}
    if data:
        if "name" in data:
            result["name"] = data["name"]
        if "token" in data:
            result["token"] = data["token"]
    module.exit_json(**result)


def main():
    argument_spec = dict(
        name=dict(required=True),
        description=dict(),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("name")
    description = module.params.get("description")
    state = module.params.get("state")

    my_name = module.who_am_i()
    try:
        namespace, robot_shortname = name.split("+", 1)
    except ValueError:
        # No namespace part in the robot account name. Therefore, the robot
        # account is in the user's personal namespace
        if my_name:
            namespace = my_name
            robot_shortname = name
        else:
            module.fail_json(
                msg=(
                    "The `name' parameter must include the"
                    " organization: <organization>+{name}."
                ).format(name=name)
            )

    # Check whether namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )
    # Make sure that the current user is the owner of that namespace
    if (
        not namespace_details.get("is_organization")
        and namespace_details.get("name") != my_name
    ):
        if my_name:
            msg = "You ({user}) are not the owner of {namespace}'s namespace.".format(
                user=my_name, namespace=namespace
            )
        else:
            msg = "You cannot access {namespace}'s namespace.".format(namespace=namespace)
        module.fail_json(msg=msg)

    # Build the API URL to access the robot object.
    if namespace_details.get("is_organization"):
        path_url = "organization/{orgname}/robots/{robot_shortname}".format(
            orgname=namespace, robot_shortname=robot_shortname
        )
    else:
        path_url = "user/robots/{robot_shortname}".format(robot_shortname=robot_shortname)

    # Get the robot account details.
    #
    # For robot accounts in organizations:
    #
    # GET /api/v1/organization/{orgname}/robots/{robot_shortname}
    # {
    #   "name": "production+robot1",
    #   "created": "Sun, 26 Sep 2021 14:22:14 -0000",
    #   "last_accessed": null,
    #   "description": "Robot for the production environment",
    #   "token": "D69U...TQT6",
    #   "unstructured_metadata": {}
    # }
    #
    # For robot accounts for the current user:
    #
    # GET /api/v1/user/robots/{robot_shortname}
    # {
    #   "name": "operator1+monrobot",
    #   "created": "Sun, 26 Sep 2021 14:33:43 -0000",
    #   "last_accessed": null,
    #   "description": "Robot for my personal namespace",
    #   "token": "EUF6...X0MU",
    #   "unstructured_metadata": {}
    # }
    robot_details = module.get_object_path(path_url, ok_error_codes=[400, 404])

    # Remove the robot account
    if state == "absent":
        module.delete(robot_details, "robot account", name, path_url)

    if robot_details:
        exit_module(module, False, robot_details)

    # Prepare the data that gets set for create
    new_fields = {}
    if description:
        new_fields["description"] = description

    data = module.unconditional_update("robot account", name, path_url, new_fields)
    exit_module(module, True, data)


if __name__ == "__main__":
    main()
