#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Herve Quatremain <herve.quatremain@redhat.com>
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
module: quay_team_ldap
short_description: Synchronize Quay Container Registry teams with LDAP groups
description:
  - Synchronize and unsynchronize teams in organizations with LDAP groups.
version_added: '0.0.9'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the team to synchronize or unsynchronize with an LDAP group.
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
      - If C(yes), then the team members are retrieved from the LDAP group
        that you define in I(group_dn). The pre-existing members are removed
        from the team before the synchronization process starts.
        Existing robot account members are not removed.
      - If C(no), then the synchronization from LDAP is disabled. Existing
        team members (from LDAP) are kept, except if you set I(keep_users) to
        C(no).
    type: bool
    default: yes
  group_dn:
    description:
      - LDAP group distinguished name (DN), relative to the base DN that you
        defined in the C(config.yaml) Quay configuration file with the
        C(LDAP_BASE_DN) parameter.
      - For example, if the LDAP group DN is
        C(cn=group1,ou=groups,dc=example,dc=org) and the base DN is
        C(dc=example,dc=org), then you must set I(group_dn) to
        C(cn=group1,ou=groups).
      - I(group_dn) is required when I(sync) is C(yes).
    type: str
  keep_users:
    description:
      - If C(yes), then the current team members are kept after the
        synchronization is disabled.
      - If C(no), then the team members are removed (except robot accounts).
      - I(keep_users) is only used when I(sync) is C(no).
    type: bool
    default: yes
notes:
  - The module requires that your Quay administrator configures the Quay
    authentication method to LDAP (C(AUTHENTICATION_TYPE) to C(LDAP) in
    C(config.yaml) and the C(LDAP_*) parameters correctly set).
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure team operators exists before activating LDAP synchronization
  herve4m.quay.quay_team:
    name: operators
    organization: production
    role: creator
    # Only robot accounts can be added to a team you prepare for LDAP
    # synchronization. User accounts that you might add are removed when the
    # synchronization is activated
    members:
      - production+automationrobot
    append: false
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure team operators is synchronized with the op1 LDAP group
  herve4m.quay.quay_team_ldap:
    name: operators
    organization: production
    sync: true
    group_dn: cn=op1,ou=groups
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure team operators is not synchronized anymore with an LDAP group
  herve4m.quay.quay_team_ldap:
    name: operators
    organization: production
    sync: false
    # Remove all the users from the team synchronized from the LDAP group
    keep_users: false
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
        group_dn=dict(),
        keep_users=dict(type="bool", default=True),
    )

    # Create a module for ourselves
    module = APIModule(
        argument_spec=argument_spec,
        required_if=[
            ("sync", True, ["group_dn"]),
        ],
        supports_check_mode=True,
    )

    # Extract our parameters
    name = module.params.get("name")
    organization = module.params.get("organization")
    sync = module.params.get("sync")
    group_dn = module.params.get("group_dn")
    keep_users = module.params.get("keep_users")

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
    #     "service": "ldap",
    #     "base_dn": "dc=example,dc=org"
    #   },
    #   "synced": {
    #     "service": "ldap",
    #     "last_updated": "Mon, 17 Jan 2022 15:09:00 -0000",
    #     "config": {
    #       "group_dn": "cn=group1,ou=users"
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
    #     "service": "ldap",
    #     "base_dn": "dc=example,dc=org"
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

    # Disable LDAP synchronization
    if not sync:
        if "synced" not in team_details:
            module.exit_json(changed=False)
        module.delete(
            team_details,
            "LDAP synchronization",
            name,
            "organization/{orgname}/team/{team}/syncing",
            auto_exit=False,
            orgname=organization,
            team=name,
        )
        # Remove the users from the team (skip robot accounts)
        if not keep_users:
            to_delete = [
                user["name"]
                for user in team_details.get("members", [])
                if "name" in user and not user.get("is_robot")
            ]

            for member in to_delete:
                module.delete(
                    True,
                    "team member",
                    member,
                    "organization/{orgname}/team/{team}/members/{member}",
                    auto_exit=False,
                    orgname=organization,
                    team=name,
                    member=member,
                )
        module.exit_json(changed=True)

    # Activate LDAP synchronization
    try:
        if team_details["synced"]["config"]["group_dn"] == group_dn:
            module.exit_json(changed=False)
    except KeyError:
        pass
    # Already synchronized but with a different group. Unsynchronize first
    # (there is not update/PUT API endpoint)
    if "synced" in team_details:
        module.delete(
            team_details,
            "LDAP synchronization",
            name,
            "organization/{orgname}/team/{team}/syncing",
            auto_exit=False,
            orgname=organization,
            team=name,
        )
    module.create(
        "LDAP synchronization",
        name,
        "organization/{orgname}/team/{team}/syncing",
        {"group_dn": group_dn},
        orgname=organization,
        team=name,
    )


if __name__ == "__main__":
    main()
