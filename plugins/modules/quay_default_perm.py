#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, 2022, Herve Quatremain <rv4m@yahoo.co.uk>
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
# Note:
#  - The API uses the name `prototype` for default permissions.


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_default_perm
short_description: Manage Quay Container Registry default repository permissions
description:
  - Create, delete, and update default repository permissions.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  organization:
    description:
      - Name of the organization for the default permission.
        That organization must exist.
    required: true
    type: str
  name:
    description:
      - Name of the user or team that gets permission to new created
        repositories in the organization.
      - For robot accounts use the C(namespace)+C(shortrobotname) format.
    required: true
    type: str
  type:
    description:
      - Type of the account defined in I(name). Choose C(user)
        for both user and robot accounts.
    type: str
    choices: [user, team]
    default: user
  role:
    description:
      - Permission that Quay automatically grants to the user or team on new
        created repositories in the organization.
      - If you do not provide that parameter, then the module uses C(read) by
        default.
    type: str
    choices: [read, write, admin]
  creator:
    description:
      - Quay applies the default permission only when repositories are created
        by the user that you define in I(creator).
      - By default, if you do not provide that I(creator) parameter, then Quay
        applies the default permission to all new repositories, whoever creates
        them.
      - You cannot use robot accounts or teams for the I(creator) parameter.
        You can only use regular user accounts.
    type: str
  state:
    description:
      - If C(absent), then the module deletes the default permission.
      - If C(present), then the module creates the default permission if it
        does not already exist.
      - If the default permission already exists, then the module updates its
        role parameter (C(read), C(write), or C(admin)).
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
- name: Create default admin permission for user
  herve4m.quay.quay_default_perm:
    organization: production
    name: lvasquez
    type: user
    role: admin
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Create default write permission for robot
  herve4m.quay.quay_default_perm:
    organization: production
    name: production+automationrobot
    type: user
    role: write
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Create default read permission for team
  herve4m.quay.quay_default_perm:
    organization: production
    name: managers
    type: team
    role: read
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Grant read permission for the managers team when dwilde creates repo
  herve4m.quay.quay_default_perm:
    organization: production
    name: managers
    type: team
    role: read
    creator: dwilde
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure default permission for robot is removed
  herve4m.quay.quay_default_perm:
    organization: production
    name: production+automationrobot
    type: user
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        organization=dict(required=True),
        name=dict(required=True),
        type=dict(choices=["user", "team"], default="user"),
        role=dict(choices=["read", "write", "admin"]),
        creator=dict(),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    organization = module.params.get("organization")
    name = module.params.get("name")
    kind = module.params.get("type")
    role = module.params.get("role")
    creator = module.params.get("creator")
    state = module.params.get("state")

    if not module.get_organization(organization):
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {orgname} organization does not exist.".format(orgname=organization)
        )

    # Get the default permissions (prototypes) for the organization
    #
    # GET /api/v1/organization/{orgname}/prototypes
    # {
    #   "prototypes": [
    #     {
    #       "activating_user": {
    #         "name": "operator1",
    #         "is_robot": false,
    #         "kind": "user",
    #         "is_org_member": true,
    #         "avatar": {
    #           "name": "operator1",
    #           "hash": "b2eb...336b",
    #           "color": "#17becf",
    #           "kind": "user"
    #         }
    #       },
    #       "delegate": {
    #         "name": "team1",
    #         "kind": "team",
    #         "avatar": {
    #           "name": "team1",
    #           "hash": "5760...397e",
    #           "color": "#9c9ede",
    #           "kind": "team"
    #         }
    #       },
    #       "role": "admin",
    #       "id": "9ce2c228-8c38-4f9d-834e-3cd181247dc1"
    #     },
    #     {
    #       "activating_user": null,
    #       "delegate": {
    #         "name": "tata+mytest",
    #         "is_robot": true,
    #         "kind": "user",
    #         "is_org_member": true,
    #         "avatar": {
    #           "name": "tata+mytest",
    #           "hash": "1d29...1d29",
    #           "color": "#ad494a",
    #           "kind": "robot"
    #         }
    #       },
    #       "role": "write",
    #       "id": "b9c7c015-b59f-4c14-95eb-80b5d263a866"
    #     },
    #     {
    #       "activating_user": null,
    #       "delegate": {
    #         "name": "team1",
    #         "kind": "team",
    #         "avatar": {
    #           "name": "team1",
    #           "hash": "5760...397e",
    #           "color": "#9c9ede",
    #           "kind": "team"
    #         }
    #       },
    #       "role": "read",
    #       "id": "874f9fcb-d17d-4bac-95e6-5b543ab44927"
    #     }
    #   ]
    # }
    all_prototypes_list = module.get_object_path(
        "organization/{orgname}/prototypes", orgname=organization
    )

    # Finding a matching prototype
    prototype_details = None
    if all_prototypes_list:
        for proto in all_prototypes_list.get("prototypes", []):
            # Delegate section does not match
            if (
                "delegate" not in proto
                or not proto["delegate"]
                or proto["delegate"].get("name") != name
                or proto["delegate"].get("kind") != kind
            ):
                continue
            # User provides the `creator' parameter but the prototype does not
            # have a matching `activating_user' key, or it does not match.
            if creator and (
                "activating_user" not in proto
                or not proto["activating_user"]
                or proto["activating_user"].get("name") != creator
            ):
                continue
            # User does not provide the `creator' parameter but the prototype
            # has an `activating_user' key. No match
            if (
                not creator
                and "activating_user" in proto
                and proto["activating_user"]
                and proto["activating_user"].get("name")
            ):
                continue
            prototype_details = proto
            break

    # Remove the prototype
    if state == "absent":
        module.delete(
            prototype_details,
            "default permission",
            name,
            "organization/{orgname}/prototypes/{uuid}",
            orgname=organization,
            uuid=prototype_details.get("id", "") if prototype_details else "",
        )

    # Verify that the users and teams exist
    if kind == "user":
        if not module.get_account(name):
            module.fail_json(
                msg="The {user} user or robot account does not exist.".format(user=name)
            )
    elif not module.get_team(organization, name):
        module.fail_json(
            msg="The {team} team does not exist in the {orgname} organization.".format(
                team=name, orgname=organization
            )
        )
    if creator:
        user_details = module.get_account(creator)
        if not user_details:
            module.fail_json(
                msg="The {user} user account does not exist.".format(user=creator)
            )
        if user_details.get("is_robot"):
            module.fail_json(
                msg=(
                    "Robot accounts cannot be used for `creator':"
                    " {user} must be a user account."
                ).format(user=creator)
            )

    # Create the prototype
    if not prototype_details:
        new_fields = {
            "delegate": {"name": name, "kind": kind},
            "role": role if role else "read",
        }
        if creator:
            new_fields["activating_user"] = {"name": creator}
        module.create(
            "default permission",
            name,
            "organization/{orgname}/prototypes",
            new_fields,
            orgname=organization,
        )

    if not role:
        module.exit_json(changed=False)

    module.update(
        prototype_details,
        "default permission",
        name,
        "organization/{orgname}/prototypes/{uuid}",
        {"role": role},
        orgname=organization,
        uuid=prototype_details.get("id", ""),
    )


if __name__ == "__main__":
    main()
