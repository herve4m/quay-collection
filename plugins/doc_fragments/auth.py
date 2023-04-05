# -*- coding: utf-8 -*-

# Copyright: (c) 2021, 2022, Herve Quatremain <rv4m@yahoo.co.uk>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    # Ansible Galaxy documentation fragment
    DOCUMENTATION = r"""
options:
  quay_host:
    description:
      - URL for accessing the API. U(https://quay.example.com:8443) for example.
      - If you do not set the parameter, then the module uses the C(QUAY_HOST)
        environment variable.
      - If you do no set the environment variable either, then the module uses
        the U(http://127.0.0.1) URL.
    type: str
    default: http://127.0.0.1
  validate_certs:
    description:
      - Whether to allow insecure connections to the API.
      - If C(no), then the module does not validate SSL certificates.
      - If you do not set the parameter, then the module tries the
        C(QUAY_VERIFY_SSL) environment variable (C(yes), C(1), and C(True) mean
        yes, and C(no), C(0), C(False), and no value mean no).
    type: bool
    default: yes
    aliases: [verify_ssl]
"""

    LOGIN = r"""
options:
  quay_token:
    description:
      - OAuth access token for authenticating against the API.
      - If you do not set the parameter, then the module tries the C(QUAY_TOKEN)
        environment variable.
      - Mutually exclusive with I(quay_username) and I(quay_password).
    type: str
  quay_username:
    description:
      - The username to use for authenticating against the API.
      - If you do not set the parameter, then the module tries the
        C(QUAY_USERNAME) environment variable.
      - If you set I(quay_username), then you also need to set I(quay_password).
      - Mutually exclusive with I(quay_token).
    type: str
  quay_password:
    description:
      - The password to use for authenticating against the API.
      - If you do not set the parameter, then the module tries the
        C(QUAY_PASSWORD) environment variable.
      - If you set I(quay_password), then you also need to set I(quay_username).
      - Mutually exclusive with I(quay_token).
    type: str
"""
