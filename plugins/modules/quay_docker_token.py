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
module: quay_docker_token
short_description: Manage tokens for accessing Quay Container Registry repositories
description:
  - Create or delete tokens for client tools to access repositories.
  - For example, the C(docker), C(podman), and C(skopeo) command-line tools can
    use such tokens.
  - Kubernetes can also use those tokens, declared is Kubernetes secret
    objects, to pull images and deploy pods.
  - Using tokens is an alternative to using your user login and password.
  - The tokens you create are for the user account you are logged in.
    You cannot create tokens for other users, even if you are logged in with a
    super user account.
version_added: '0.0.11'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the token to create or delete.
    required: true
    type: str
  state:
    description:
      - If C(absent), then the module deletes the token.
      - The module does not fail if the token does not exist because the
        state is already as expected.
      - If C(present), then the module creates the token if it does not
        already exist.
      - If the token already exists, then the module returns its details.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The tokens you create with this module are unrelated to OAUth access tokens
    that you use to access the Quay API.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure the token exists for my account
  herve4m.quay.quay_docker_token:
    name: token_for_pull
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: token_details

- name: Ensure the image is pulled
  containers.podman.podman_image:
    name: quay.example.com/production/smallimage:v1.0.0
    username: "{{ token_details['username'] }}"
    password: "{{ token_details['token_code'] }}"

- name: Ensure the token does not exist
  herve4m.quay.quay_docker_token:
    name: token_for_pull
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r"""
name:
  description: Name of the application token.
  returned: always
  type: str
  sample: my_push_token
uuid:
  description: Internal ID of the application token.
  returned: always
  type: str
  sample: 31b32343-e974-4f8c-bd9c-db5a0406f211
username:
  description:
    - Username to use with client commands such as C(docker) or C(podman).
    - When you use a token with those commands, do not use your login name
      but use this username instead.
    - For Quay, that username is always C($app).
    - Because the C($) character is a special shell character, you might have
      to protect it with a backslash or by using single quotation marks.
  returned: always
  type: str
  sample: $app
token_code:
  description: Token to use as the password.
  returned: always
  type: str
  sample: OVKFT8YJBTQYG4Z30YHDOPJBU4M2VPMCQJ5IYW4BAQGZD8T5V70JORLJBJHFYVVFQ89K7
auth_b64:
  description:
    - Base 64 encoding of the username and the token
      (C(I(username):I(token_code)))
    - Some client configuration files, such as the C(~/.docker/config.json)
      Docker configuration file, require that you provide the username and the
      token in that format.
    - You can decode the string by using the C(base64 --decode) command. See
      the C(base64)(1) man page.
  returned: always
  type: str
  sample: JGFw...NzBK
dockerconfigjson_b64:
  description:
    - Base 64 encoding of the C(~/.docker/config.json) configuration file.
    - The C(containers-auth.json)(5) man page describe the format of the file.
  returned: always
  type: str
  sample: ewog...Cn0=
created:
  description: Token creation date and time.
  returned: always
  type: str
  sample: Wed, 25 May 2022 12:46:41 -0000
last_accessed:
  description:
    - Last date and time the token was used.
    - If the token has not been used yet, then I(last_accessed) is C(null).
  returned: always
  type: str
  sample: Wed, 25 May 2022 12:49:45 -0000
expiration:
  description:
    - Expiration date and time of the token.
    - By default, tokens do not expire. In that case I(expiration) is C(null).
    - Your Quay administrator might have activated expiration by setting the
      C(APP_SPECIFIC_TOKEN_EXPIRATION) directive in the C(config.yaml)
      configuration file.
  returned: always
  type: str
  sample: Fri, 29 Apr 2023 13:31:05 -0000
 """

import base64

from ansible.module_utils._text import to_bytes, to_text
from ..module_utils.api_module import APIModule


def exit_module(module, changed, data):
    """Exit the module and return data.

    :param module: The module object.
    :type module: :py:class:``APIModule``
    :param changed: The changed status of the object.
    :type changed: bool
    :param data: The data returned by the API call.
    :type data: dict
    """
    result = {"changed": changed}
    if data:
        result.update(data)
        # Rename the "title" key to "name"
        if "title" in result:
            result["name"] = result["title"]
            del result["title"]
        # Add the "username" key (always $app)
        result["username"] = "$app"
        if "token_code" in result:
            auth = "$app:{token}".format(token=result["token_code"])
            result["auth_b64"] = to_text(base64.b64encode(to_bytes(auth)))
            docker_conf = """{
  "auths": {
    "%s": {
      "auth": "%s",
      "email": ""
    }
  }
}""" % (
                module.host_url.netloc,
                result["auth_b64"],
            )
            result["dockerconfigjson_b64"] = to_text(base64.b64encode(to_bytes(docker_conf)))
    module.exit_json(**result)


def main():
    argument_spec = dict(
        name=dict(required=True),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("name")
    state = module.params.get("state")

    # Retrieve the user application tokens
    #
    # GET /api/v1/user/apptoken
    # {
    #   "tokens": [
    #     {
    #       "uuid": "46c72673-a78c-4fe7-a54d-43ce2d6aa440",
    #       "title": "test",
    #       "last_accessed": "Fri, 18 Feb 2022 12:22:35 -0000",
    #       "created": "Fri, 18 Feb 2022 11:52:54 -0000",
    #       "expiration": null
    #     },
    #     {
    #       "uuid": "5e79c964-1c50-4ef8-b802-cd8db81ec9f3",
    #       "title": "1token",
    #       "last_accessed": null,
    #       "created": "Fri, 18 Feb 2022 11:53:05 -0000",
    #       "expiration": null
    #     },
    #     {
    #       "uuid": "196b81c3-d691-49ac-b3d7-1728437e7cb1",
    #       "title": "anotherone",
    #       "last_accessed": null,
    #       "created": "Fri, 18 Feb 2022 11:53:09 -0000",
    #       "expiration": null
    #     }
    #   ],
    #   "only_expiring": null
    # }
    token_lst = module.get_object_path("user/apptoken")

    # Looking for the requested token (multiple tokens can have the same name)
    tokens = [t for t in token_lst.get("tokens", []) if t.get("title") == name]

    # Remove (revoke) the tokens matching the given name
    if state == "absent":
        for token in tokens:
            module.delete(
                token,
                "application token",
                name,
                "user/apptoken/{uuid}",
                auto_exit=False,
                uuid=token.get("uuid", "") if token else "",
            )
        module.exit_json(changed=True if tokens else False)

    if tokens:
        # Retrieve the token code (from the first token)
        #
        # GET /api/v1/user/apptoken/{uuid}
        # {
        #   "token": {
        #     "uuid": "196b81c3-d691-49ac-b3d7-1728437e7cb1",
        #     "title": "anotherone",
        #     "last_accessed": null,
        #     "created": "Fri, 18 Feb 2022 11:53:09 -0000",
        #     "expiration": null,
        #     "token_code": "BQU8...OS6S"
        #   }
        # }
        token = module.get_object_path("user/apptoken/{uuid}", uuid=tokens[0].get("uuid", ""))
        exit_module(module, False, token.get("token"))

    # Create the token
    #
    # POST /api/v1/user/apptoken
    # {
    #   "token": {
    #     "uuid": "cca9d9d0-ac59-40af-9216-f852cf3f4dc9",
    #     "title": "mynewtoken",
    #     "last_accessed": null,
    #     "created": "Fri, 18 Feb 2022 12:27:51 -0000",
    #     "expiration": null,
    #     "token_code": "KNS7...LVTD"
    #   }
    # }
    token = module.create(
        "application token",
        name,
        "user/apptoken",
        {"title": name},
        auto_exit=False,
    )
    exit_module(module, True, token.get("token"))


if __name__ == "__main__":
    main()
