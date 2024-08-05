#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, 2022, Herve Quatremain <herve.quatremain@redhat.com>
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
#  - The module is not idempotent because it can only be used once, on a fresh
#    Quay installation.
#  - The /api/v1/user/initialize API endpoint can only be called once, just
#    after installation, when the database is empty.
#  - The two following parameters must be set in config.yaml for the endpoint
#    to work:
#      FEATURE_USER_INITIALIZE: true
#      AUTHENTICATION_TYPE: Database
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_first_user
short_description: Create the first user account
description:
  - Create the first user just after installing Quay Container Registry.
version_added: '0.0.7'
author: Herve Quatremain (@herve4m)
options:
  username:
    description:
      - Name of the user account to create.
      - You probably want that user account to have superuser permissions so
        that you can use the returned token to create additional objects.
        To do so, add the account name to the C(SUPER_USERS) section in the
        C(config.yaml) file before using the M(herve4m.quay.quay_first_user)
        module.
    required: true
    type: str
  email:
    description:
      - User's email address.
      - If your Quay administrator has enabled the mailing capability of your
        Quay installation (C(FEATURE_MAILING) to C(true) in C(config.yaml)),
        then this I(email) parameter is mandatory.
    type: str
  password:
    description:
      - User's password as a clear string.
      - The password must be at least eight characters long and must not
        contain white spaces.
    required: true
    type: str
  create_token:
    description:
      - If C(yes), then an OAuth access token is created and returned. You can
        use that returned token with the other Quay modules, by setting it in
        the I(quay_token) parameter. The token is valid for 2 hours 30 minutes.
      - If C(no), then no access token is created.
    type: bool
    default: no
notes:
  - The module requires Quay version 3.6 or later.
  - To use the module, you must enable the first user creation feature of your
    Quay installation (C(FEATURE_USER_INITIALIZE) in C(config.yaml)).
  - You must also use the internal database of your Quay installation for
    authentication (C(AUTHENTICATION_TYPE) to C(Database) in C(config.yaml)).
  - Use the module just after installing Quay, when the database is empty.
    The module fails if user accounts are already defined in the database.
  - Supports C(check_mode).
extends_documentation_fragment:
  - herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure the initial user exists
  herve4m.quay.quay_first_user:
    username: admin
    email: admin@example.com
    password: S6tGwo13
    create_token: true
    quay_host: https://quay.example.com
  register: result

- ansible.builtin.debug:
    msg: "Access token: {{ result['access_token'] }}"
"""

RETURN = r"""
access_token:
  description:
    - The access token that you can use for subsequent module calls.
    - The token is valid for 2 hours 30 minutes.
  returned: only when you set the I(create_token) parameter to C(yes)
  type: str
  sample: W2YX0V838JZ5FHHUH82Q25FZZMRX8YTB1MTN56P3
email:
  description: User's email address.
  returned: always
  type: str
  sample: admin@example.com
encrypted_password:
  description: Encrypted user's password.
  returned: always
  type: str
  sample: /pbR5LPYx4Y3w/SSf2dAwNxCCNgwmmZk+x04TKn6xEKL2At5wblOy7wA1tNZEhRc
username:
  description: Name of the created user account.
  returned: always
  type: str
  sample: admin
"""

from ..module_utils.api_module import APIModuleNoAuth


def main():
    argument_spec = dict(
        username=dict(required=True),
        email=dict(),
        password=dict(no_log=True, required=True),
        create_token=dict(type="bool", default=False),
    )

    # Create a module for ourselves
    module = APIModuleNoAuth(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    username = module.params.get("username")
    email = module.params.get("email")
    password = module.params.get("password")
    create_token = module.params.get("create_token")

    new_fields = {"username": username, "password": password, "access_token": create_token}
    if email:
        new_fields["email"] = email
    data = module.create("user", username, "user/initialize", new_fields, auto_exit=False)
    result = {"changed": True}
    result.update(data)
    module.exit_json(**result)


if __name__ == "__main__":
    main()
