#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Herve Quatremain <rv4m@yahoo.co.uk>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import base64
import json

from ansible.module_utils.common.text.converters import to_bytes, to_text
from ansible.module_utils.six.moves.urllib.parse import urlparse
from ansible.parsing.ajson import AnsibleJSONEncoder


def quay_docker_config(
    name, token, url="http://127.0.0.1", email="", encoding="utf-8", *args, **kw
):
    """Build a Docker configuration in JSON format.

    :param name: Username
    :type name: str
    :param token: Token/password
    :type token: str
    :param url: URL of the container image registry
    :type url: str
    :param email: User email address
    :type email: str
    :param encoding: Character encoding for ``name`` and ``token``
    :type encoding: str

    :return: The Docker configuration encoded in Base64
    :rtype: str
    """
    repo_host = urlparse(url).netloc
    auth = to_text(
        base64.b64encode(
            to_bytes(name + ":" + token, encoding=encoding, errors="surrogate_or_strict")
        )
    )
    docker_config = {"auths": {}}
    docker_config["auths"][repo_host] = {"auth": auth, "email": email}

    # defaults for filters
    if "vault_to_text" not in kw:
        kw["vault_to_text"] = True
    if "preprocess_unsafe" not in kw:
        kw["preprocess_unsafe"] = False

    return to_text(
        base64.b64encode(
            to_bytes(
                json.dumps(docker_config, cls=AnsibleJSONEncoder, *args, **kw),
                encoding=encoding,
                errors="surrogate_or_strict",
            )
        )
    )


class FilterModule(object):
    """Quay jinja2 filter"""

    def filters(self):
        return {"quay_docker_config": quay_docker_config}
