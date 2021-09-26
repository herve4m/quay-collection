#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Herve Quatremain <rv4m@yahoo.co.uk>
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
#  - The current user can create/delete robot accounts in their personnal
#    namespace, but not in the namespace of other users.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_robot
short_description: Manage Red Hat Quay robot accounts
description:
  - Create and delete robot accounts.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the robot account to create or remove, in the format
        C(namespace)+C(shortname). The namespace can be an organization or a
        personnal namespace.
      - The short name (the part after the C(+) sign) must be in lowercase,
        must not contain white spaces, must not start by a digit, and must be
        at least two characters long.
      - You can create and delete robot accounts in your personnal namespace,
        but not in the personnal namespace of other users. The token you use in
        C(quay_token) determines the user account you are using.
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
      - The module does not fail if the account does not exist because the
        state is already as expected.
      - If C(present), then the module creates the robot account if it does not
        already exist.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in C(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure robot account production+robotprod1 exists
  herve4m.quay.quay_robot:
    name: production+robotprod1
    description: Robot account for production
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure robot account lvasquez+myrobot exists in my namespace
  herve4m.quay.quay_robot:
    name: lvasquez+myrobot
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure robot account production+robotdev1 doest not exists
  herve4m.quay.quay_robot:
    name: production+robotdev1
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


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

    try:
        namespace, robot_shortname = name.split("+", 1)
    except ValueError:
        module.fail_json(
            msg=(
                "{name}: wrong format for the robot account name:"
                " `name' must be `namespace+robotshortname'."
            ).format(name=name)
        )

    # Check whether namespace exists (organization or user account).
    #
    # GET /api/v1/organization/{orgname}
    # GET /api/v1/users/{username}
    if module.get_object_path("organization/{orgname}", orgname=namespace):
        path_url = "organization/{orgname}/robots/{robot_shortname}".format(
            orgname=namespace, robot_shortname=robot_shortname
        )
    elif module.get_object_path("users/{username}", username=namespace):
        # Make sure that the current user is the owner of that namespace
        user = module.get_object_path("user/")
        myname = user.get("username")
        if namespace != myname:
            module.fail_json(
                msg="You, {user}, are not the owner of the {namespace} namespace.".format(
                    user=myname, namespace=namespace
                )
            )
        path_url = "user/robots/{robot_shortname}".format(robot_shortname=robot_shortname)
    else:
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )

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
        module.exit_json(changed=False)

    # Prepare the data that gets set for create
    new_fields = {}
    if description:
        new_fields["description"] = description

    module.unconditional_update("robot account", name, path_url, new_fields)
    module.exit_json(changed=True)


if __name__ == "__main__":
    main()
