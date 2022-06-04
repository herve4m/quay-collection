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


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_organization
short_description: Manage Red Hat Quay organizations
description:
  - Create, delete, and update organizations in Red Hat Quay.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the organization to create, remove, or modify.
      - The name must be in lowercase and must not contain white spaces. For
        compatibility with earlier versions of Docker, the name must be at
        least four characters long.
    required: true
    type: str
  new_name:
    description:
      - New name for the organization.
      - Setting this option changes the name of the organization which current
        name is provided in I(name).
      - The token you use to connect to the API (in I(quay_token)) must have
        the "Super User Access" permission.
    type: str
  email:
    description:
      - Email address to associate with the new organization.
      - If your Quay administrator has enabled the mailing capability of your
        Quay installation (C(FEATURE_MAILING) to C(true) in C(config.yaml)),
        then this I(email) parameter is mandatory.
      - You cannot use the same address as your account email.
    type: str
  time_machine_expiration:
    description:
      - The amount of time, after a tag is deleted, that the tag is accessible
        in time machine before being garbage collected.
    type: str
    choices: [0s, 1d, 7d, 14d, 1month]
  state:
    description:
      - If C(absent), then the module deletes the organization.
      - The module does not fail if the organization does not exist because the
        state is already as expected.
      - If C(present), then the module creates the organization if it does not
        already exist.
      - If the organization already exists, then the module updates its state.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
  - To rename organizations, the token must also have the "Super User Access"
    permission.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure the organization exists
  herve4m.quay.quay_organization:
    name: production
    email: prodlist@example.com
    time_machine_expiration: "7d"
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

# Renaming requires superuser permissions
- name: Ensure the organization has a new name
  herve4m.quay.quay_organization:
    name: production
    new_name: development
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the organization is removed
  herve4m.quay.quay_organization:
    name: development
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    tm_allowed_values = {
        "0s": 0,
        "1d": 86400,
        "7d": 604800,
        "14d": 1209600,
        "1month": 2419200,
    }
    argument_spec = dict(
        name=dict(required=True),
        new_name=dict(),
        email=dict(),
        time_machine_expiration=dict(choices=list(tm_allowed_values.keys())),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("name")
    new_name = module.params.get("new_name")
    email = module.params.get("email")
    tm_expiration = module.params.get("time_machine_expiration")
    state = module.params.get("state")

    org_details = module.get_organization(name)
    new_org_details = module.get_organization(new_name) if new_name else None

    # The destination organization already exists
    if org_details and new_org_details:
        module.fail_json(
            msg="The {orgname} organization (`new_name') already exists.".format(
                orgname=new_name
            )
        )

    # Remove the organization
    if state == "absent":
        if new_org_details:
            module.delete(
                new_org_details,
                "organization",
                new_name,
                "organization/{orgname}",
                orgname=new_name,
            )
        else:
            module.delete(
                org_details,
                "organization",
                name,
                "organization/{orgname}",
                orgname=name,
            )

    # Renaming the organization (requires superuser permissions)
    created = False
    if new_name:
        # The original organization does not exists...
        if not org_details:
            # and neither the new organization. Create that new organization.
            if not new_org_details:
                new_fields = {"name": new_name}
                if email:
                    new_fields["email"] = email
                module.create(
                    "organization",
                    new_name,
                    "organization/",
                    new_fields,
                    auto_exit=False,
                )
                created = True
            else:
                # The original organization does not exists but the new one
                # does. Use that new organization in the rest of the module.
                org_details = new_org_details
            # Use the new organization name in the rest of the module
            name = new_name
            new_name = None
        else:
            # The original organization exists. Rename it.
            # Requires superuser permissions.
            module.update(
                org_details,
                "organization",
                new_name,
                "superuser/organizations/{orgname}",
                {"name": new_name},
                auto_exit=False,
                orgname=name,
            )
            created = True
            name = new_name
            new_name = None
    elif not org_details:
        new_fields = {"name": name}
        if email:
            new_fields["email"] = email
        module.create(
            "organization",
            name,
            "organization/",
            new_fields,
            auto_exit=False,
        )
        created = True

    # Prepare the data that gets set for update
    new_fields = {}
    if tm_expiration:
        new_fields["tag_expiration_s"] = tm_allowed_values[tm_expiration]
    if email:
        new_fields["email"] = email

    # Update the organization
    updated, _not_used = module.update(
        org_details,
        "organization",
        name,
        "organization/{orgname}",
        new_fields,
        auto_exit=False,
        orgname=name,
    )

    module.exit_json(changed=created or updated)


if __name__ == "__main__":
    main()
