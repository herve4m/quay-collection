#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, 2022, Herve Quatremain <rv4m@yahoo.co.uk>
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
module: quay_repository_mirror
short_description: Manage Quay Container Registry repository mirror configurations
description:
  - Configure and synchronize repository mirrors in Quay Container Registry.
version_added: '0.0.4'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the existing repository for which the mirror parameters are
        configured. The format for the name is C(namespace)/C(shortname). The
        namespace can only be an organization namespace.
    required: true
    type: str
  is_enabled:
    description:
      - Defines whether the mirror configuration is active or inactive.
      - C(false) by default.
    type: bool
  external_reference:
    description:
      - Path to the remote container repository to synchronize, such as
        quay.io/projectquay/quay for example.
      - That parameter is required when creating the mirroring configuration.
    type: str
  external_registry_username:
    description:
      - Username to use for pulling the image from the remote registry.
    type: str
  external_registry_password:
    description:
      - Password to use for pulling the image from the remote registry.
    type: str
  sync_interval:
    description:
      - Synchronization interval for this repository mirror in seconds.
      - 86400 (one day) by default.
    type: int
  sync_start_date:
    description:
      - The date and time at which the first synchronization should be
        initiated.
      - The format for the I(sync_start_date) parameter is ISO 8601 UTC, such
        as 2021-12-02T21:06:00Z.
      - If you do not provide the I(sync_start_date) parameter when you
        configure a new repository mirror, then the synchronization is
        immediately active, and a synchronization is initiated if the
        I(is_enabled) parameter is C(true).
    type: str
  robot_username:
    description:
      - Username of the robot account that is used for synchronization.
      - That parameter is required when creating the mirroring configuration.
    type: str
  image_tags:
    description:
      - List of image tags to be synchronized from the remote repository.
    type: list
    elements: str
  verify_tls:
    description:
      - Defines whether TLS of the external registry should be verified.
      - C(true) by default.
    type: bool
  http_proxy:
    description:
      - HTTP proxy to use for accessing the remote container registry.
      - See the C(curl) documentation for more details.
      - By default, no proxy is used.
    type: str
  https_proxy:
    description:
      - HTTPS proxy to use for accessing the remote container registry.
      - See the C(curl) documentation for more details.
      - By default, no proxy is used.
    type: str
  no_proxy:
    description:
      - Comma-separated list of hosts for which the proxy should not be used.
      - Only relevant when you also specify a proxy configuration by setting
        the I(http_proxy) or I(https_proxy) variables.
      - See the C(curl) documentation for more details.
    type: str
  force_sync:
    description:
      - Triggers an immediate image synchronization.
    type: bool
    default: false
notes:
  - Your Quay administrator must enable the mirroring capability of your Quay
    installation (C(FEATURE_REPO_MIRROR) in C(config.yaml)) to use that module.
  - You cannot modify a repository mirroring configuration if a synchronization
    is in progress.
  - There is no API function to remove the configuration. However, you can
    deactivate mirroring by setting the I(is_enabled) parameter to C(false) or
    by changing the repository mirror state (see the I(repo_state) parameter in
    the M(herve4m.quay.quay_repository) module).
    The configuration is preserved when you disable mirroring.
  - Supports C(check_mode).
  - The user account associated with the token that you provide in
    I(quay_token) must have administrator access to the repository.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure mirroring configuration is set for the existing production/smallimage repo
  herve4m.quay.quay_repository_mirror:
    name: production/smallimage
    external_reference: quay.io/projectquay/quay
    http_proxy: http://proxy.example.com:3128
    robot_username: production+auditrobot
    is_enabled: true
    image_tags:
      - latest
      - v3.5.2
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure mirroring is disabled for the production/smallimage repository
  herve4m.quay.quay_repository_mirror:
    name: production/smallimage
    is_enabled: false
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Immediate trigger a synchronization of the repository
  herve4m.quay.quay_repository_mirror:
    name: production/smallimage
    force_sync: true
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

"""

RETURN = r""" # """

import copy
from datetime import datetime

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        name=dict(required=True),
        is_enabled=dict(type="bool"),
        force_sync=dict(type="bool", default=False),
        robot_username=dict(),
        external_reference=dict(),
        external_registry_username=dict(),
        external_registry_password=dict(no_log=True),
        verify_tls=dict(type="bool"),
        image_tags=dict(type="list", elements="str"),
        sync_interval=dict(type="int"),
        sync_start_date=dict(),
        http_proxy=dict(),
        https_proxy=dict(),
        no_proxy=dict(),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("name").strip("/")
    is_enabled = module.params.get("is_enabled")
    force_sync = module.params.get("force_sync")
    robot_username = module.params.get("robot_username")
    external_reference = module.params.get("external_reference")
    external_registry_username = module.params.get("external_registry_username")
    external_registry_password = module.params.get("external_registry_password")
    verify_tls = module.params.get("verify_tls")
    image_tags = module.params.get("image_tags")
    sync_interval = module.params.get("sync_interval")
    sync_start_date = module.params.get("sync_start_date")
    http_proxy = module.params.get("http_proxy")
    https_proxy = module.params.get("https_proxy")
    no_proxy = module.params.get("no_proxy")

    my_name = module.who_am_i()
    try:
        namespace, repo_shortname = name.split("/", 1)
    except ValueError:
        # No namespace part in the repository name. Therefore, the repository
        # is in the user's personal namespace
        if my_name:
            namespace = my_name
            repo_shortname = name
        else:
            module.fail_json(
                msg=(
                    "The `name' parameter must include the"
                    " organization: <organization>/{name}."
                ).format(name=name)
            )

    # Check whether namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )

    full_repo_name = "{namespace}/{repository}".format(
        namespace=namespace, repository=repo_shortname
    )

    # Get the repository mirror configuration details
    #
    # GET /api/v1/repository/{namespace}/{repository}/mirror
    # {
    #     "is_enabled": true,
    #     "mirror_type": "PULL",
    #     "external_reference": "quay.io/projectquay/quay",
    #     "external_registry_username": null,
    #     "external_registry_config": {
    #         "verify_tls": true,
    #         "proxy": {
    #             "http_proxy": null,
    #             "https_proxy": null,
    #             "no_proxy": null
    #         }
    #     },
    #     "sync_interval": 86400,
    #     "sync_start_date": "2021-01-01T12:00:00Z",
    #     "sync_expiration_date": null,
    #     "sync_retries_remaining": 3,
    #     "sync_status": "NEVER_RUN",
    #     "root_rule": {
    #         "rule_kind": "tag_glob_csv",
    #         "rule_value": [
    #             "latest"
    #         ]
    #     },
    #     "robot_username": "production+auditrobot"
    # }

    mirror_details = module.get_object_path(
        "repository/{full_repo_name}/mirror",
        ok_error_codes=[404, 403],
        full_repo_name=full_repo_name,
    )

    # Create a new synchronization configuration
    if not mirror_details:

        # Verify the mandatory parameters for creation
        missing_req_params = []
        if external_reference is None:
            missing_req_params.append("external_reference")
        if robot_username is None:
            missing_req_params.append("robot_username")
        if image_tags is None:
            missing_req_params.append("image_tags")
        if missing_req_params:
            module.fail_json(
                msg="missing required arguments: {args}".format(
                    args=", ".join(missing_req_params)
                )
            )

        # Create the repository mirror configuration
        new_fields = {
            "is_enabled": is_enabled if is_enabled is not None else False,
            "robot_username": robot_username,
            "external_reference": external_reference,
            "root_rule": {"rule_kind": "tag_glob_csv", "rule_value": image_tags},
            "sync_interval": int(sync_interval) if sync_interval is not None else 86400,
            "sync_start_date": sync_start_date
            if sync_start_date
            else datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "external_registry_username": external_registry_username
            if external_registry_username
            else None,
            "external_registry_config": {
                "verify_tls": verify_tls if verify_tls is not None else True,
                "proxy": {
                    "http_proxy": http_proxy if http_proxy else None,
                    "https_proxy": https_proxy if https_proxy else None,
                    "no_proxy": no_proxy if no_proxy else None,
                },
            },
        }
        if external_registry_password:
            new_fields["external_registry_password"] = external_registry_password

        module.create(
            "repository",
            full_repo_name,
            "repository/{full_repo_name}/mirror",
            new_fields,
            auto_exit=False,
            full_repo_name=full_repo_name,
        )

        if force_sync:
            module.create(
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror/sync-now",
                {},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )

        module.exit_json(changed=True)

    # Update the repository mirror configuration
    new_fields = {}
    if external_registry_password is not None:
        new_fields["external_registry_password"] = external_registry_password
    if external_registry_username is not None:
        new_fields["external_registry_username"] = external_registry_username
    if sync_start_date is not None:
        new_fields["sync_start_date"] = sync_start_date
    if sync_interval is not None:
        new_fields["sync_interval"] = int(sync_interval)
    if robot_username is not None:
        new_fields["robot_username"] = robot_username
    if external_reference is not None:
        new_fields["external_reference"] = external_reference
    if is_enabled is not None:
        new_fields["is_enabled"] = is_enabled
    if image_tags is not None:
        new_fields["root_rule"] = {"rule_kind": "tag_glob_csv", "rule_value": image_tags}

    try:
        registry_config = copy.deepcopy(mirror_details["external_registry_config"])
    except KeyError:
        registry_config = {}
    if verify_tls is not None:
        registry_config["verify_tls"] = verify_tls
    if http_proxy is not None:
        if "proxy" not in registry_config:
            registry_config["proxy"] = {}
        registry_config["proxy"]["http_proxy"] = http_proxy if http_proxy else None
    if https_proxy is not None:
        if "proxy" not in registry_config:
            registry_config["proxy"] = {}
        registry_config["proxy"]["https_proxy"] = https_proxy if https_proxy else None
    if no_proxy is not None:
        if "proxy" not in registry_config:
            registry_config["proxy"] = {}
        registry_config["proxy"]["no_proxy"] = no_proxy if no_proxy else None
    if registry_config:
        new_fields["external_registry_config"] = registry_config

    changed = False
    if new_fields:
        # Cannot update the configuration when a synchronization is in progress
        if mirror_details["sync_status"] == "SYNCING":
            module.exit_json(
                skipped=True,
                msg="cannot update the configuration while a synchronization is in progress",
            )
        updated, _not_used = module.update(
            mirror_details,
            "repository",
            full_repo_name,
            "repository/{full_repo_name}/mirror",
            new_fields,
            auto_exit=False,
            full_repo_name=full_repo_name,
        )
        if updated:
            changed = True

    if force_sync and mirror_details["sync_status"] not in ("SYNCING", "SYNC_NOW"):
        module.create(
            "repository",
            full_repo_name,
            "repository/{full_repo_name}/mirror/sync-now",
            {},
            auto_exit=False,
            full_repo_name=full_repo_name,
        )
        changed = True

    module.exit_json(changed=changed)


if __name__ == "__main__":
    main()
