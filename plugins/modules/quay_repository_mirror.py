#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Herve Quatremain <rv4m@yahoo.co.uk>
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
from datetime import datetime

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_repository_mirror
short_description: Manage Red Hat Quay repositories mirrors
description:
  - Create, delete, and update mirror configuration in Red Hat Quay.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the repository to create, remove, or modify a mirror configuration.
        The format for the name is C(namespace)/C(shortname). The namespace can
        only be an organization namespace.
      - The name must be in lowercase and must not contain white spaces.
    required: true
    type: str
  state:
    description:
      - There is no API function to remove the configuration. The configuration
        can only be deactivated or the repository state can be changed. Note that
        when changing the state, the config remains in the current state.
    type: str
    default: present
  is_enabled:
    description:
      - Defines whether the mirror configuration is active or inactive.
    type: bool
    default: false
  external_reference:
    description:
      - Path to the remote container repository to sync.
      - e.g. quay.io/projectquay/quay
    type: str
    required: true
  external_registry_username:
    description:
      - Username for the chosen remote registry to pull the images.
    type: str
  external_registry_password:
    description:
      - Password for the chosen remote registry to pull the images.
    type: str
  sync_interval:
    description:
      - Sync interval for this repository mirror in seconds.
    type: int
    default: 86400
  sync_start_date:
    description:
      - The time from which the sync should run (ISO 8601 UTC).
      - eg. 2021-12-02T21:06:00.977021Z
    type: str
    default: 2021-01-01T12:00:00.000000Z
  robot_username:
    description:
      - Username of the robot that is authorised to sync.
    type: str
    required: true
  image_tags:
    description:
      - List of image tags to be synchronised from the remote repository.
    type: list
    elements: str
    required: true
  verify_tls:
    description:
      - Defines whether TLS of the external registry should be verified.
    type: bool
    default: true
  force_sync:
    description:
      - Triggers an immediate sync for the repository.
      - Be aware, if a sync is active configuration updates are skipped.
    type: bool
    default: false
notes:
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Repositories" and "Create Repositories" permissions.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure repository mirror conf for smallimage exists in the production organization
  herve4m.quay.quay_repository_mirror:
    name: production/smallimage
    external_reference: quay.io/projectquay/quay
    robot_username: production+auditrobot
    is_enabled: true
    tags:
      - latest
      - v3.5.2
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure repository mirror configuration for production/smallimage is disabled
  herve4m.quay.quay_repository_mirror:
    name: production/smallimage
    is_enabled: false
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Immediate trigger a sync of the repository
  herve4m.quay.quay_repository_mirror:
    name: production/smallimage
    force_sync: true
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        name=dict(required=True),
        is_enabled=dict(type="bool", default=False),
        force_sync=dict(type="bool", default=False),
        robot_username=dict(required=True),
        external_reference=dict(required=True),
        external_registry_username=dict(),
        external_registry_password=dict(no_log=True),
        verify_tls=dict(type="bool", default=True),
        image_tags=dict(type="list", elements="str"),
        sync_interval=dict(),
        sync_start_date=dict(),
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
    #     "sync_start_date": "2021-12-02T21:06:00.977021Z",
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

    # Check whether namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )

    changed = False
    if not mirror_details:
        # Create the repository mirror configuration
        new_fields = {
            "is_enabled": is_enabled,
            "robot_username": robot_username,
            "external_reference": external_reference,
            "external_registry_config": {"verify_tls": verify_tls},
            "root_rule": {"rule_kind": "tag_glob_csv", "rule_value": image_tags},
        }
        new_fields["sync_interval"] = sync_interval if sync_interval else 86400
        new_fields["sync_start_date"] = (
            sync_start_date
            if sync_start_date
            else datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        )
        new_fields["external_registry_username"] = (
            external_registry_username if external_registry_username else ""
        )
        new_fields["external_registry_password"] = (
            external_registry_username if external_registry_username else ""
        )

        module.create(
            "repository",
            full_repo_name,
            "repository/{full_repo_name}/mirror",
            new_fields,
            auto_exit=False,
            full_repo_name=full_repo_name,
        )
        changed = True

        if force_sync:
            module.create(
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror/sync-now",
                {},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )

    else:
        if mirror_details["sync_status"] == "SYNCING":
            module.exit_json(skipped=True)

        # Update external_registry_username
        if external_registry_password is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"external_registry_password": external_registry_password},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update external_registry_username
        if sync_start_date is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"external_registry_username": external_registry_username},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update sync_start_date
        if sync_start_date is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"sync_start_date": sync_start_date},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update sync_interval
        if sync_interval is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"sync_interval": sync_interval},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update image_tags
        if image_tags is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"root_rule": {"rule_kind": "tag_glob_csv", "rule_value": image_tags}},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update verify_tls
        if verify_tls is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"external_registry_config": {"verify_tls": verify_tls}},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update robot_username
        if robot_username is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"robot_username": robot_username},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update mirror active state
        if is_enabled is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"is_enabled": is_enabled},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True
        # Update external_reference
        if external_reference is not None:
            updated, _ = module.update(
                mirror_details,
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/mirror",
                {"external_reference": external_reference},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            if updated:
                changed = True

        if force_sync:
            if mirror_details["sync_status"] != "SYNC_NOW":
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
