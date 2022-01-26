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
module: quay_manifest_label
short_description: Manage Red Hat Quay image manifest labels
description:
  - Add or remove labels to image manifests.
version_added: '0.0.10'
author: Herve Quatremain (@herve4m)
options:
  image:
    description:
      - Manifest to update. The format is C(namespace)/C(repository):C(tag) or
        C(namespace)/C(repository)@C(digest). The namespace can be an
        organization or a personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
      - If you omit the tag and the digest part, then C(latest) is assumed.
    required: true
    type: str
  key:
    description:
      - Label's key.
    required: true
    type: str
  value:
    description:
      - Label's value. Required when C(state=present).
    type: str
  replace:
    description:
      - Only used when C(state=present).
      - If C(yes), then the module deletes all the labels that use the key you
        define in the I(key) parameter before adding the new label.
      - If C(no), then the module adds the new label even if existing labels
        already use the key you define in the I(key) parameter. Quay supports
        multiple labels with the same key.
    type: bool
    default: true
  state:
    description:
      - If C(absent), then the module deletes the labels that match the I(key)
        and I(value) parameters. If you do not provide the I(value) parameter,
        then the module deletes all the labels with the I(key) parameter.
      - If C(present), then the module adds a label to the manifest.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Labels defined in the Containerfile/Dockerfile cannot be deleted or
    updated. They are read-only.
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Repositories" permission.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.token
"""

EXAMPLES = r"""
- name: Ensure the manifest has the architecture label set
  herve4m.quay.quay_manifest_label:
    image: ansibletestorg/ansibletestrepo:v1.0.0
    key: architecture
    value: x86_64
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the manifest has an additional architecture label set
  herve4m.quay.quay_manifest_label:
    image: ansibletestorg/ansibletestrepo:v1.0.0
    key: architecture
    value: power
    replace: false
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the manifest has a specific component label removed
  herve4m.quay.quay_manifest_label:
    image: ansibletestorg/smallimage@sha256:4f6f...e797
    key: component
    value: front
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Remove all the labels that have a key set to scopes
  herve4m.quay.quay_manifest_label:
    image: ansibletestorg/ansibletestrepo:v1.0.0
    key: scopes
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r"""
id:
  description: Internal identifier of the label.
  returned: always
  type: str
  sample: 155f20b3-7ebf-4796-9d18-eb5c54bf7364
key:
  description: Label's key.
  returned: always
  type: str
  sample: architecture
value:
  description: Label's value.
  returned: always
  type: str
  sample: x86_64
source_type:
  description:
    - Whether the label has been set by the Containerfile/Dockerfile manifest
      (C(manifest)), or by an API call or from the web UI (C(api)).
    - Labels set in Containerfile/Dockerfile manifests are read-only.
  returned: always
  type: str
  sample: api
media_type:
  description: Format of the label (C(text/plain) or C(application/json)).
  returned: always
  type: str
  sample: text/plain
"""


from ..module_utils.api_module import APIModule
from ..module_utils.quay_image import QuayImage


def main():
    argument_spec = dict(
        image=dict(required=True),
        key=dict(required=True),
        value=dict(),
        replace=dict(type="bool", default=True),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(
        argument_spec=argument_spec,
        required_if=[
            ("state", "present", ["value"]),
        ],
        supports_check_mode=True,
    )

    # Extract our parameters
    image = module.params.get("image").strip("/")
    key = module.params.get("key")
    value = module.params.get("value")
    replace = module.params.get("replace")
    state = module.params.get("state")

    # Get the components of the given image (namespace, repository, tag, digest)
    img = QuayImage(module, image)
    namespace = img.namespace
    if namespace is None:
        module.fail_json(
            msg=(
                "The `image' parameter must include the"
                " organization: <organization>/{name}."
            ).format(name=image)
        )

    # Check whether the namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )

    # Get the digest
    if img.digest:
        manifest_digest = img.digest
    else:
        tags = module.get_tags(namespace, img.repository, img.tag, only_active_tags=False)
        if not tags:
            module.fail_json(msg="The {image} image does not exist.".format(image=image))
        try:
            manifest_digest = tags[0]["manifest_digest"]
        except KeyError:
            module.fail_json(
                msg="Cannot retrieve the manifest digest for the {image} image.".format(
                    image=image
                )
            )

    full_repo_name = "{namespace}/{repository}".format(
        namespace=namespace, repository=img.repository
    )

    # Get the labels
    #
    # GET /api/v1/repository/{namespace}/{repository}/manifest/{digest}/labels
    # {
    #   "labels": [
    #     {
    #       "id": "04fdb83e-e80c-4e52-b365-252268c391ae",
    #       "key": "maintainer",
    #       "value": "NGINX Docker Maintainers <docker-maint@nginx.com>",
    #       "source_type": "manifest",
    #       "media_type": "text/plain"
    #     },
    #     {
    #       "id": "155f20b3-7ebf-4796-9d18-eb5c54bf7364",
    #       "key": "mytest",
    #       "value": "myvalue",
    #       "source_type": "api",
    #       "media_type": "text/plain"
    #     }
    #   ]
    # }
    #
    # When `source_type' is `manifest', then the label is read-only because it
    # comes from the Containerfile/Dockerfile.
    # When `source_type' is `api', then the label is mutable (it has been set
    # by using the web UI or from a previous call to the API)
    res = module.get_object_path(
        "repository/{full_repo_name}/manifest/{digest}/labels",
        full_repo_name=full_repo_name,
        digest=manifest_digest,
    )
    labels = res.get("labels", [])

    # Remove the label
    if state == "absent":
        # Delete the labels that match key and value (if value is provided,
        # otherwise delete all the labels that match the key).
        changed = False
        for lbl in labels:
            if (
                lbl.get("source_type") != "manifest"
                and lbl.get("id")
                and lbl.get("key") == key
                and (value is None or lbl.get("value") == value)
            ):
                obj_name = key
                if value:
                    obj_name += "=" + value
                module.delete(
                    True,
                    "label",
                    obj_name,
                    "repository/{full_repo_name}/manifest/{digest}/labels/{id}",
                    auto_exit=False,
                    full_repo_name=full_repo_name,
                    digest=manifest_digest,
                    id=lbl.get("id"),
                )
                changed = True
        module.exit_json(changed=changed)

    # Retrieve the labels that might already exist with the given key
    matching_label = None
    changed = False
    for lbl in labels:
        if lbl.get("key") == key:
            if lbl.get("value") == value:
                matching_label = lbl

            # Remove the labels that match the key
            elif replace and lbl.get("source_type") != "manifest" and lbl.get("id"):
                module.delete(
                    True,
                    "label",
                    key,
                    "repository/{full_repo_name}/manifest/{digest}/labels/{id}",
                    auto_exit=False,
                    full_repo_name=full_repo_name,
                    digest=manifest_digest,
                    id=lbl.get("id"),
                )
                changed = True

    if matching_label:
        result = {"changed": changed}
        result.update(matching_label)
        module.exit_json(**result)

    new_fields = {"key": key, "value": value, "media_type": "text/plain"}
    data = module.create(
        "label",
        key + "=" + value,
        "repository/{full_repo_name}/manifest/{digest}/labels",
        new_fields,
        auto_exit=False,
        full_repo_name=full_repo_name,
        digest=manifest_digest,
    )
    result = {"changed": True}
    result.update(data.get("label"))
    module.exit_json(**result)


if __name__ == "__main__":
    main()
