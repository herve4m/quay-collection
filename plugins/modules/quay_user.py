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
#  - The API does not allow renaming a user.
#  - The API does not allow deleting or updating superusers.
#  - A user is flagged as a superuser when their name is listed in the Quay
#    configuration file, `config.yaml`, under the `SUPER_USERS` directive.
#  - The API can set the superuser flag (the API updates the configuration file)
#    but that only takes effect once Quay is restarted.
#  - As a consequence, the module allows users to set/unset the flag by using
#    the `superuser` parameter but does not restart Quay so the change is
#    not immediatly reflected.
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_user
short_description: Manage Red Hat Quay users
description:
  - Create, delete, and update user accounts in Red Hat Quay.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  username:
    description:
      - Name of the user account to create, remove, or modify.
    required: true
    type: str
  email:
    description:
      - User's email address.
      - If you have enabled the mailing capabily of your Quay installation,
        then this I(email) parameter is mandatory.
    type: str
  password:
    description:
      - User's password as a clear string.
      - The password must be at least eight characters long and must not
        contain white spaces.
    type: str
  enabled:
    description:
      - Enable (C(true)) or disable (C(false)) the user account.
      - When their account is disabled, the user cannot log in to the web UI
        and cannot push or pull container images.
    type: bool
  superuser:
    description:
      - Grant superuser permissions to the user.
      - Granting superuser privileges to a user is not immediate and
        usually requires a restart of the Red Hat Quay service.
      - You cannot revoke superuser permissions.
    type: bool
    default: False
    aliases: ['is_superuser']
  state:
    description:
      - If C(absent), then the module deletes the user.
      - You cannot delete superuser accounts.
      - The module does not fail if the user does not exist because the state
        is already as expected.
      - If C(present), then the module creates the user if it does not already
        exist.
      - If the user account already exists, then the module updates its state.
      - You cannot update superuser accounts.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the
    "Super User Access" permission.
  - You cannot delete or modify superuser accounts.
  - You cannot revoke superuser privileges with this module.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure the user exists
  herve4m.quay.quay_user:
    username: lvasquez
    email: lvasquez@example.com
    password: vs9mrD55NP
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the user is removed
  herve4m.quay.quay_user:
    username:  dwilde
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the user is a superuser
  herve4m.quay.quay_user:
    username: jziglar
    email: jziglar@example.com
    state: present
    # Only effective after a restart of the Red Hat Quay service.
    superuser: true
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the user account is disabled
  herve4m.quay.quay_user:
    username: chorwitz
    email: chorwitz@example.com
    state: present
    enabled: false
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        username=dict(required=True),
        email=dict(),
        password=dict(no_log=True),
        enabled=dict(type="bool"),
        superuser=dict(type="bool", default=False, aliases=["is_superuser"]),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    username = module.params.get("username")
    email = module.params.get("email")
    password = module.params.get("password")
    enabled = module.params.get("enabled")
    superuser = module.params.get("superuser")
    state = module.params.get("state")

    # Get the user details from its name.
    #
    # GET /api/v1/superuser/users/{username}
    # {
    #   "kind": "user",
    #   "name": "student",
    #   "username": "student",
    #   "email": "student@example.com",
    #   "verified": true,
    #   "avatar": {
    #     "name": "student",
    #     "hash": "616b...717e",
    #     "color": "#aec7e8",
    #     "kind": "user"
    #   },
    #   "super_user": false,
    #   "enabled": true
    # }
    user_details = module.get_object_path("superuser/users/{username}", username=username)

    if user_details and user_details.get("super_user"):
        module.warn(
            "The {name} user is a superuser. You cannot delete or update superusers.".format(
                name=username
            )
        )
        module.exit_json(changed=False)

    # Remove the user
    if state == "absent":
        # It seems that only enabled users can be deleted
        if user_details:
            # Force the superuser flag to False for the API to update the
            # Quay `config.yaml` configuration file. That only works if a
            # previous module execution set that flag for the user and the Quay
            # system has not yet been restarted.
            module.unconditional_update(
                "user",
                username,
                "superuser/users/{username}",
                {"enabled": True, "superuser": False},
                username=username,
            )

        module.delete(
            user_details,
            "user",
            username,
            "superuser/users/{username}",
            username=username,
        )

    # Create the user
    if user_details is None:
        new_fields = {"username": username}
        if email:
            new_fields["email"] = email
        module.create("user", username, "superuser/users/", new_fields, auto_exit=False)
        user_details = new_fields
        user_details["enabled"] = True
        created = True
    else:
        created = False

    # Create the data that gets sent for update
    new_fields = {"superuser": superuser}
    if enabled is not None:
        new_fields["enabled"] = enabled
    if email:
        new_fields["email"] = email
    if password:
        new_fields["password"] = password

    updated, _ = module.update(
        user_details,
        "user",
        username,
        "superuser/users/{username}",
        new_fields,
        auto_exit=False,
        username=username,
    )

    module.exit_json(changed=created or updated)


if __name__ == "__main__":
    main()
