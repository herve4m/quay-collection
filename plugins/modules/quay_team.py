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
module: quay_team
short_description: Manage Red Hat Quay teams
description:
  - Create, delete, and update teams in organizations.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the team to create, remove, or modify.
      - The name must be in lowercase, must not contain white spaces, must not
        start by a digit, and must be at least two characters long.
    required: true
    type: str
  organization:
    description:
      - Name of the organization for the team. That organization must exist.
    required: true
    type: str
  role:
    description:
      - Role of the team within the organization.
    type: str
    choices: [member, creator, admin]
  description:
    description:
      - Text in Markdown format that describes the team.
    type: str
  members:
    description:
      - List of the user or robot accounts in the team. Use the syntax
        C(organization)+C(robotshortname) for robot accounts.
    type: list
    elements: str
  append:
    description:
      - If C(yes), then add the users specified in I(members) to the team.
      - If C(no), then the module sets the team members to users specified in
        I(members), removing all others users from the team.
    type: bool
    default: yes
  state:
    description:
      - If C(absent), then the module deletes the team.
      - The module does not fail if the team does not exist because the
        state is already as expected.
      - If C(present), then the module creates the team if it does not
        already exist.
      - If the team already exists, then the module updates its state.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.token
"""

EXAMPLES = r"""
- name: Ensure team operators exists in the production organization
  herve4m.quay.quay_team:
    name: operators
    organization: production
    description: |
        # Operation Team

        * Operators can create repositories
        * Operators can store their images in those repositories
    role: creator
    members:
      - lvasquez
      - dwilde
      - production+automationrobot
    append: false
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure team developers does not exist in the production organization
  herve4m.quay.quay_team:
    name: developers
    organization: production
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure team administrators has no members
  herve4m.quay.quay_team:
    name: administrators
    organization: production
    members: []
    append: false
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure team operators has additionnal members
  herve4m.quay.quay_team:
    name: operators
    organization: production
    members:
      - jziglar
      - chorwitz
    append: true
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        name=dict(required=True),
        organization=dict(required=True),
        role=dict(choices=["member", "creator", "admin"]),
        description=dict(),
        members=dict(type="list", elements="str"),
        append=dict(type="bool", default=True),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("name")
    organization = module.params.get("organization")
    description = module.params.get("description")
    role = module.params.get("role")
    members = module.params.get("members")
    append = module.params.get("append")
    state = module.params.get("state")

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
    #     "team1": {
    #       "name": "team1",
    #       "description": "My line1\nMy line2\nMy line3",
    #       "role": "member",
    #       "avatar": {
    #         "name": "team1",
    #         "hash": "5760...397e",
    #         "color": "#9c9ede",
    #         "kind": "team"
    #       },
    #       "can_view": true,
    #       "repo_count": 0,
    #       "member_count": 0,
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
    org_details = module.get_organization(organization)
    if not org_details:
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {orgname} organization does not exist.".format(orgname=organization)
        )

    # Get the team details
    team_details = org_details["teams"].get(name) if "teams" in org_details else None

    # Remove the team
    if state == "absent":
        # It seems that you cannot delete a team when the role is not member.
        # Change the role to member then.
        if team_details:
            module.update(
                team_details,
                "team",
                name,
                "organization/{orgname}/team/{teamname}",
                {"role": "member"},
                auto_exit=False,
                orgname=organization,
                teamname=name,
            )
        module.delete(
            team_details,
            "team",
            name,
            "organization/{orgname}/team/{teamname}",
            orgname=organization,
            teamname=name,
        )

    # Prepare the data that gets set for create or update
    new_fields = {"name": name}
    if description is not None:
        new_fields["description"] = description
    # The role attribute is mandatory
    if role:
        new_fields["role"] = role
    elif team_details:
        new_fields["role"] = team_details.get("role", "member")
    else:
        new_fields["role"] = "member"

    # Same PUT request for creating or updating the object
    updated, _not_used = module.update(
        team_details,
        "team",
        name,
        "organization/{orgname}/team/{teamname}",
        new_fields,
        auto_exit=False,
        orgname=organization,
        teamname=name,
    )

    # Get the team members.
    #
    # GET /api/v1/organization/{orgname}/team/{teamname}/members
    # {
    #   "name": "teamxyz",
    #   "members": [
    #     {
    #       "name": "operator1",
    #       "kind": "user",
    #       "is_robot": false,
    #       "avatar": {
    #         "name": "operator1",
    #         "hash": "b2eb...336b",
    #         "color": "#17becf",
    #         "kind": "user"
    #       },
    #       "invited": false
    #     },
    #     {
    #       "name": "developer1",
    #       "kind": "user",
    #       "is_robot": false,
    #       "avatar": {
    #         "name": "developer1",
    #         "hash": "d7bc...9b34",
    #         "color": "#9c9ede",
    #         "kind": "user"
    #       },
    #       "invited": false
    #     },
    #     {
    #       "name": "production+automation",
    #       "kind": "user",
    #       "is_robot": true,
    #       "avatar": {
    #         "name": "production+automation",
    #         "hash": "1543...a801",
    #         "color": "#5254a3",
    #         "kind": "robot"
    #       },
    #       "invited": false
    #     }
    #   ],
    #   "can_edit": true
    # }
    team_members = module.get_object_path(
        "organization/{orgname}/team/{teamname}/members",
        query_params={"includePending": True},
        orgname=organization,
        teamname=name,
    )
    if team_members:
        current_members = set(
            [user["name"] for user in team_members.get("members", []) if "name" in user]
        )
    else:
        current_members = set()

    new_members = set(members if members else [])

    to_add = new_members - current_members
    if append:
        to_delete = set()
    else:
        to_delete = current_members - new_members

    # Checking that all the user account to add exist
    accounts_not_found = []
    for member in to_add:
        if module.get_account(member) is None:
            accounts_not_found.append(member)
    if accounts_not_found:
        module.fail_json(
            msg="At least one user to add as team member does not exist: {users}.".format(
                users=", ".join(accounts_not_found)
            )
        )

    for member in to_add:
        module.unconditional_update(
            "team member",
            member,
            "organization/{orgname}/team/{teamname}/members/{member}",
            {},
            orgname=organization,
            teamname=name,
            member=member,
        )
    for member in to_delete:
        module.delete(
            True,
            "team member",
            member,
            "organization/{orgname}/team/{teamname}/members/{member}",
            auto_exit=False,
            orgname=organization,
            teamname=name,
            member=member,
        )

    module.exit_json(changed=updated or len(to_add) or len(to_delete))


if __name__ == "__main__":
    main()
