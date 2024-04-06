#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Herve Quatremain <rv4m@yahoo.co.uk>
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
module: quay_team_oidc
short_description: Synchronize Quay Container Registry teams with OIDC groups
description:
  - Synchronize and unsynchronize teams in organizations with OIDC groups.
version_added: '1.2.0'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the team to synchronize or unsynchronize with an OIDC group.
        That team must exist (see the M(herve4m.quay.quay_team) module to
        create it).
    required: true
    type: str
  organization:
    description:
      - Name of the organization for the team. That organization must exist.
    required: true
    type: str
  sync:
    description:
      - If C(yes), then the team members are retrieved from the OIDC group
        that you define in I(group_name). The pre-existing members are removed
        from the team before the synchronization process starts.
        Existing robot account members are not removed.
      - If C(no), then the synchronization from OIDC is disabled.
    type: bool
    default: yes
  group_name:
    description:
      - OIDC group name.
      - I(group_name) is required when I(sync) is C(yes).
    type: str
notes:
  - The module requires Quay version 3.11 or later.
  - The module requires that your Quay administrator configures the Quay
    authentication method to OIDC (C(AUTHENTICATION_TYPE) to C(OIDC) in
    C(config.yaml)), and enables team synchronization (C(FEATURE_TEAM_SYNCING)
    to C(true) in C(config.yaml)).
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure team operators exists before activating OIDC synchronization
  herve4m.quay.quay_team:
    name: operators
    organization: production
    role: creator
    # Only robot accounts can be added to a team you prepare for OIDC
    # synchronization. User accounts that you might add are removed when the
    # synchronization is activated
    members:
      - production+automationrobot
    append: false
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure team operators is synchronized with the op1 OIDC group
  herve4m.quay.quay_team_oidc:
    name: operators
    organization: production
    sync: true
    group_name: op1
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure team operators is not synchronized anymore with an OIDC group
  herve4m.quay.quay_team_oidc:
    name: operators
    organization: production
    sync: false
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        name=dict(required=True),
        organization=dict(required=True),
        sync=dict(type="bool", default=True),
        group_name=dict(),
    )

    # Create a module for ourselves
    module = APIModule(
        argument_spec=argument_spec,
        required_if=[
            ("sync", True, ["group_name"]),
        ],
        supports_check_mode=True,
    )

    # Extract our parameters
    name = module.params.get("name")
    organization = module.params.get("organization")
    sync = module.params.get("sync")
    group_name = module.params.get("group_name")

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
        if not sync:
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {orgname} organization does not exist.".format(orgname=organization)
        )

    # Get the team synchronization status
    #
    # For a synchronized team, the result has a "synced" dictionary:
    #
    # GET /api/v1/organization/{orgname}/team/{teamname}/members
    # {
    #   "name": "ansibletestteam2",
    #   "members": [
    #     {
    #       "name": "ansibletestorg+ansibletestrobot1",
    #       "kind": "user",
    #       "is_robot": true,
    #       "avatar": {
    #         "name": "ansibletestorg+ansibletestrobot1",
    #         "hash": "cc0d...a0d3",
    #         "color": "#e377c2",
    #         "kind": "robot"
    #       },
    #       "invited": false
    #     },
    #     {
    #       "name": "user1",
    #       "kind": "user",
    #       "is_robot": false,
    #       "avatar": {
    #         "name": "user1",
    #         "hash": "b36a...e210",
    #         "color": "#9edae5",
    #         "kind": "user"
    #       },
    #       "invited": false
    #     }
    #   ],
    #   "can_edit": true,
    #   "can_sync": {
    #     "service": "oidc"
    #   },
    #   "synced": {
    #     "service": "oidc",
    #     "last_updated": null,
    #     "config": {
    #       "group_name": "mygroup"
    #     }
    #   }
    # }
    #
    # For an unsynchronized team, the "synced" dictionary is absent:
    #
    # GET /api/v1/organization/{orgname}/team/{teamname}/members
    # {
    #   "name": "foobar",
    #   "members": [],
    #   "can_edit": true,
    #   "can_sync": {
    #     "service": "oidc"
    #   }
    # }
    team_details = module.get_object_path(
        "organization/{orgname}/team/{team}/members", orgname=organization, team=name
    )
    if team_details is None:
        if not sync:
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {team} team does not exist in the {orgname} organization.".format(
                team=name, orgname=organization
            )
        )

    # Disable OIDC synchronization
    if not sync:
        if "synced" not in team_details:
            module.exit_json(changed=False)
        module.delete(
            team_details,
            "OIDC synchronization",
            name,
            "organization/{orgname}/team/{team}/syncing",
            orgname=organization,
            team=name,
        )

    # Activate OIDC synchronization
    try:
        if team_details["synced"]["config"]["group_name"] == group_name:
            module.exit_json(changed=False)
    except KeyError:
        pass
    # Already synchronized but with a different group. Unsynchronize first
    # (there is not update/PUT API endpoint)
    if "synced" in team_details:
        module.delete(
            team_details,
            "OIDC synchronization",
            name,
            "organization/{orgname}/team/{team}/syncing",
            auto_exit=False,
            orgname=organization,
            team=name,
        )
    module.create(
        "OIDC synchronization",
        name,
        "organization/{orgname}/team/{team}/syncing",
        {"group_name": group_name},
        orgname=organization,
        team=name,
    )


if __name__ == "__main__":
    main()
