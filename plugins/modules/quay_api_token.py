#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Herve Quatremain <rv4m@yahoo.co.uk>
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
module: quay_api_token
short_description: Create OAuth access tokens for accessing the Quay Container Registry API
description: Create OAuth access tokens for authenticating with the API.
version_added: '0.0.12'
author: Herve Quatremain (@herve4m)
options:
  quay_username:
    description:
      - The username to use for authenticating against the API.
      - If you do not set the parameter, then the module tries the
        C(QUAY_USERNAME) environment variable.
    type: str
    required: true
  quay_password:
    description:
      - The password to use for authenticating against the API.
      - If you do not set the parameter, then the module tries the
        C(QUAY_PASSWORD) environment variable.
    type: str
    required: true
  client_id:
    description:
      - The client ID associated with the OAuth application to use for
        generating the OAuth access token.
      - See the M(herve4m.quay.quay_application) module to create an application
        object and to retrieve the associated client ID.
    required: true
    type: str
  rights:
    description:
      - List of permissions to grant to the user account. C(all) means all the
        permissions.
    type: list
    elements: str
    choices:
      - org:admin
      - repo:admin
      - repo:create
      - repo:read
      - repo:write
      - super:user
      - user:admin
      - user:read
      - all
    default: repo:read
notes:
  - Supports C(check_mode).
  - The generated OAuth access token acts on behalf of the user account you use
    with the module (in I(quay_username)).
  - The module is not idempotent. Every time you run it, an additional OAuth
    access token is produced. The other OAuth access tokens stay valid.
  - You cannot delete OAuth access tokens.
extends_documentation_fragment:
  - herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Generate an OAuth access token
  herve4m.quay.quay_api_token:
    quay_username: lvasquez
    quay_password: vs9mrD55NP
    # The OAuth application must exist. See the following example that shows
    # how to create an organization and an application.
    client_id: PZ6F80R1LCVPGYNZGSZQ
    rights:
      - org:admin
      - user:admin
    quay_host: https://quay.example.com
  register: token_details

- name: Display the new OAuth access token
  debug:
    msg: "The OAuth access token is: {{ token_details['access_token'] }}"

# The following example creates an organization, an OAuth application, a user
# account, and then generates an OAuth access token for that user account.
# The OAuth access token of an existing super user is required to create the
# organization, the application, and the user account.
- name: Ensure the organization exists
  herve4m.quay.quay_organization:
    name: production
    email: prodlist@example.com
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the application extapp exists
  herve4m.quay.quay_application:
    organization: production
    name: extapp
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: app_details

- name: Ensure the user exists
  herve4m.quay.quay_user:
    username: jziglar
    password: i45fR38GhY
    email: jziglar@example.com
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Generate an OAuth access token for the user
  herve4m.quay.quay_api_token:
    quay_username: jziglar
    quay_password: i45fR38GhY
    client_id: "{{ app_details['client_id'] }}"
    rights:
      - all
    quay_host: https://quay.example.com
  register: token_details

- name: Display the new OAuth access token
  debug:
    msg: "The OAuth access token is: {{ token_details['access_token'] }}"
"""

RETURN = r"""
access_token:
  description: The OAuth access token.
  returned: always
  type: str
  sample: CywbRGkh1ttYkRRy9VL0Aw0yU9q7J62vIeo7WCFw
 """

import re

from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.basic import env_fallback
from ..module_utils.api_module import APIModuleNoAuth, APIModuleError


def main():
    allowed_rights = [
        "org:admin",
        "repo:admin",
        "repo:create",
        "repo:read",
        "repo:write",
        "super:user",
        "user:admin",
        "user:read",
        "all",
    ]
    argument_spec = dict(
        quay_username=dict(required=True, fallback=(env_fallback, ["QUAY_USERNAME"])),
        quay_password=dict(
            required=True, no_log=True, fallback=(env_fallback, ["QUAY_PASSWORD"])
        ),
        client_id=dict(required=True),
        rights=dict(
            type="list", elements="str", choices=allowed_rights, default=["repo:read"]
        ),
    )

    # Create a module for ourselves
    module = APIModuleNoAuth(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    client_id = module.params.get("client_id")
    rights = module.params.get("rights")
    if not rights:
        module.fail_json(msg="argument cannot be empty: rights")
    if "all" in rights:
        rights = set(allowed_rights)
        rights.remove("all")
    else:
        rights = set(rights)

    # Generate the OAuth access token
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    redirect_url = module.host_url._replace(path="/oauth/localapp")
    data = {
        "client_id": client_id,
        "redirect_uri": redirect_url.geturl(),
        "scope": " ".join(rights),
        "_csrf_token": module.token,
    }
    url = module.host_url._replace(path="/oauth/authorizeapp")
    if module.check_mode:
        module.exit_json(
            changed=True, access_token="NotValidCheckModeNotValidCheckModeNotVal"
        )
    try:
        response = module.make_raw_request(
            "POST",
            url,
            ok_error_codes=[302],
            headers=headers,
            data=urlencode(data),
            follow_redirects=False,
        )
    except APIModuleError as e:
        module.fail_json(msg=str(e))

    if "Location" not in response["headers"]:
        module.fail_json(msg="Cannot retrieve the OAuth access token from the returned data")

    try:
        token = re.search("access_token=(.*?)&", response["headers"]["Location"]).group(1)
    except AttributeError:
        module.fail_json(msg="Cannot retrieve the CSRF token from the returned data")

    module.exit_json(changed=True, access_token=token)


if __name__ == "__main__":
    main()
