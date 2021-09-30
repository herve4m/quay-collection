#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Herve Quatremain <rv4m@yahoo.co.uk>
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
  quay_token:
    description:
      - Token for authenticating with the API.
      - If you do not set the parameter, then the module tries the C(QUAY_TOKEN)
        environment variable.
    type: str
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
