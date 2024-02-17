#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024 Herve Quatremain <rv4m@yahoo.co.uk>
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
module: quay_proxy_cache
short_description: Manage Quay Container Registry proxy cache configurations
description:
  - Create, delete, and update the proxy cache configuration in organizations.
version_added: '1.1.0'
author: Herve Quatremain (@herve4m)
options:
  organization:
    description:
      - Name of the organization in which to create the proxy cache
        configuration. That organization must exist.
    required: true
    type: str
  registry:
    description:
      - Name of the remote registry.
      - Add a namespace to the remote registry to restrict caching images from
        that namespace.
    type: str
    default: quay.io
  username:
    description:
      - Name of the user account to use for authenticating with the
        remote registry.
      - Do not set a username for a public access to the remote registry.
    type: str
  password:
    description:
      - User's password as a clear string.
      - Do not set a password for a public access to the remote registry.
    type: str
  insecure:
    description:
      - Whether to allow insecure connections to the remote registry.
      - If C(yes), then the module does not validate SSL certificates.
    type: bool
    default: no
  expiration:
    description:
      - Tag expiration in seconds for cached images.
      - 86400 (one day) by default.
    type: int
    default: 86400
  state:
    description:
      - If C(absent), then the module removes the proxy cache configuration.
      - The module does not fail if the proxy cache configuration does not exist,
        because the state is already as expected.
      - If C(present), then the module creates the proxy cache configuration.
      - If a proxy cache configuration already exists, then the module deletes it
        first.
    type: str
    default: present
    choices: [absent, present]
notes:
  - The module requires Quay version 3.7 or later.
  - To use the module, you must enable the proxy cache feature of your
    Quay installation (C(FEATURE_PROXY_CACHE) in C(config.yaml)).
  - When you set I(state) to C(present), the module always reports a changed
    status, because it cannot retrieve the current password for the remote
    registry to compare it with the I(password) parameter.
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Organization" permission.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure proxy cache is enabled in the production organization
  herve4m.quay.quay_proxy_cache:
    organization: production
    registry: quay.io/prodimgs
    username: cwade
    password: My53cr3Tpa55
    expiration: 172800
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure proxy cache is disabled in the production organization
  herve4m.quay.quay_proxy_cache:
    organization: production
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        organization=dict(required=True),
        registry=dict(default="quay.io"),
        username=dict(),
        password=dict(no_log=True),
        insecure=dict(type="bool", default=False),
        expiration=dict(type="int", default=86400),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    organization = module.params.get("organization")
    registry = module.params.get("registry")
    username = module.params.get("username")
    password = module.params.get("password")
    insecure = module.params.get("insecure")
    expiration = module.params.get("expiration")
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

    # Get the proxy cache details.
    #
    # GET /api/v1/organization/{orgname}/proxycache
    # {
    #   "upstream_registry": "quay.io",
    #   "expiration_s": 86400,
    #   "insecure": false
    # }
    cache_details = module.get_object_path(
        "organization/{orgname}/proxycache", orgname=organization
    )

    # Always remove the proxy cache configuration, because the configuration
    # cannot be updated (an error is received if you try to set a configuration
    # when one already exists)
    upd = module.delete(
        cache_details,
        "proxy cache",
        organization,
        "organization/{orgname}/proxycache",
        auto_exit=False,
        orgname=organization,
    )

    if state == "absent":
        module.exit_json(changed=upd)

    # Prepare the data that gets set for create
    new_fields = {
        "org_name": organization,
        "expiration_s": int(expiration),
        "insecure": insecure,
        "upstream_registry": registry,
        "upstream_registry_username": username if username else None,
        "upstream_registry_password": password if password else None,
    }

    module.create(
        "proxy cache",
        organization,
        "organization/{orgname}/proxycache",
        new_fields,
        orgname=organization,
    )


if __name__ == "__main__":
    main()
