#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021-2024, Herve Quatremain <rv4m@yahoo.co.uk>
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
short_description: Manage Quay Container Registry organizations
description:
  - Create, delete, and update organizations in Quay Container Registry.
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
  auto_prune_method:
    description:
      - Method to use for the auto-pruning tags policy.
      - If C(none), then the module ensures that no policy is in place. The
        tags are not pruned.
      - If C(tags), then the policy keeps only the number of tags that you
        specify in I(auto_prune_value).
      - If C(date), then the policy deletes the tags older than the time period
        that you specify in I(auto_prune_value).
      - I(auto_prune_value) is required when I(auto_prune_method) is C(tags) or
        C(date).
    type: str
    choices: [none, tags, date]
  auto_prune_value:
    description:
      - Number of tags to keep when I(auto_prune_value) is C(tags).
        The value must be 1 or more.
      - Period of time when I(auto_prune_value) is C(date). The value must be 1
        or more, and must be followed by a suffix; s (for second), m (for
        minute), h (for hour), d (for day), or w (for week).
      - I(auto_prune_method) is required when I(auto_prune_value) is set.
    type: str
  state:
    description:
      - If C(absent), then the module deletes the organization.
      - The module does not fail if the organization does not exist, because the
        state is already as expected.
      - If C(present), then the module creates the organization if it does not
        already exist.
      - If the organization already exists, then the module updates its state.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - Your Quay administrator must enable the auto-prune capability of your Quay
    installation (C(FEATURE_AUTO_PRUNE) in C(config.yaml)) to use the
    I(auto_prune_method) and I(auto_prune_value) parameters.
  - Using I(auto_prune_method) and I(auto_prune_value) requires Quay version
    3.11 or later.
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
    auto_prune_method: tags
    auto_prune_value: 20
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

import re

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
        auto_prune_method=dict(choices=["none", "tags", "date"]),
        auto_prune_value=dict(),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(
        argument_spec=argument_spec,
        required_if=[
            ("auto_prune_method", "tags", ["auto_prune_value"]),
            ("auto_prune_method", "date", ["auto_prune_value"]),
        ],
        required_by={
            "auto_prune_value": "auto_prune_method",
        },
        supports_check_mode=True,
    )

    # Extract our parameters
    name = module.params.get("name")
    new_name = module.params.get("new_name")
    email = module.params.get("email")
    tm_expiration = module.params.get("time_machine_expiration")
    auto_prune_method = module.params.get("auto_prune_method")
    auto_prune_value = module.params.get("auto_prune_value")
    state = module.params.get("state")

    # Validate the auto-pruning tags values
    if auto_prune_method == "tags":
        try:
            auto_prune_value = int(auto_prune_value)
        except ValueError:
            module.fail_json(
                msg=(
                    "Wrong format for the `auto_prune_value' parameter:"
                    " {auto_prune_value} is not a positive integer."
                ).format(auto_prune_value=auto_prune_value)
            )
        if auto_prune_value <= 0:
            module.fail_json(
                msg=(
                    "Wrong format for the `auto_prune_value' parameter:"
                    " {auto_prune_value} is not a positive integer."
                ).format(auto_prune_value=auto_prune_value)
            )
    if auto_prune_method == "date":
        value = "".join(auto_prune_value.split())
        if not re.match(r"[1-9]\d*[smhdw]$", value):
            module.fail_json(
                msg=(
                    "Wrong format for the `auto_prune_value' parameter:"
                    " {auto_prune_value} is not a positive integer followed by"
                    " the s, m, h, d, or w suffix."
                ).format(auto_prune_value=auto_prune_value)
            )
        auto_prune_value = value

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

    #
    # Process the auto-pruning tags policy configuration
    #

    # The user did not provide the auto_prune_method parameter, therefore there
    # is nothing to do.
    if auto_prune_method is None:
        module.exit_json(changed=created or updated)

    # Get the current auto-pruning tags policy:
    #
    # GET /api/v1/organization/{orgname}/autoprunepolicy/
    # {
    #   "policies": [
    #     {
    #       "uuid": "e54f146d-eb0e-446c-9057-61291a0b257c",
    #       "method": "creation_date",
    #       "value": "7h"
    #     }
    #   ]
    # }
    #
    # If no policy is defined, then the returned data is {"policies": []}
    prune_details = module.get_object_path(
        "organization/{orgname}/autoprunepolicy/", orgname=name
    )

    # Removing the auto-prune policies (the UI only manages one policy, but the
    # backend seems to allow several policies)
    if auto_prune_method == "none":
        if prune_details is None:
            module.exit_json(changed=created or updated)
        # Removing all the policies
        deleted = False
        for policy in prune_details.get("policies", []):
            uuid = policy.get("uuid")
            if module.delete(
                uuid,
                "auto-prune policy",
                uuid,
                "organization/{orgname}/autoprunepolicy/{uuid}",
                auto_exit=False,
                orgname=name,
                uuid=uuid,
            ):
                deleted = True
        module.exit_json(changed=created or updated or deleted)

    # Compose the request
    method = "creation_date" if auto_prune_method == "date" else "number_of_tags"
    new_policy = {
        "method": method,
        "value": auto_prune_value,
    }

    if prune_details:
        # Verify whether the policy already exists
        for policy in prune_details.get("policies", []):
            if policy.get("method") == method and policy.get("value") == auto_prune_value:
                module.exit_json(changed=created or updated)

        # If a policy already exists, then update it (the first one in the list)
        try:
            uuid = prune_details["policies"][0]["uuid"]
            new_policy["uuid"] = uuid
            module.unconditional_update(
                "auto-prune policy",
                uuid,
                "organization/{orgname}/autoprunepolicy/{uuid}",
                new_policy,
                orgname=name,
                uuid=uuid,
            )
            module.exit_json(changed=True)
        except (TypeError, IndexError):
            uuid = None

    # Create the policy
    module.create(
        "auto-prune policy",
        method,
        "organization/{orgname}/autoprunepolicy/",
        new_policy,
        orgname=name,
    )


if __name__ == "__main__":
    main()
