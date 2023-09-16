#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, 2023, Herve Quatremain <rv4m@yahoo.co.uk>
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
module: quay_manifest_label_info
short_description: Gather information about manifest labels in Quay Container Registry
description:
  - Gather information about the manifest labels in a repository.
version_added: '0.0.10'
author: Herve Quatremain (@herve4m)
options:
  image:
    description:
      - Name of the image that contains the manifest to process. The format is
        C(namespace)/C(repository):C(tag) or
        C(namespace)/C(repository)@C(digest). The namespace can be an
        organization or a personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
      - If you omit the tag and the digest part, then C(latest) is assumed.
    required: true
    type: str
  key:
    description:
      - Gather information on the labels with that specific key instead of
        returning data on all the labels in the manifest.
    type: str
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Retrieve all the labels of the centos7/nginx-116-centos7 manifest
  herve4m.quay.quay_manifest_label_info:
    image: centos7/nginx-116-centos7:latest
    quay_host: quay.io
  register: labels

- name: Retrieve the labels with a specific key
  herve4m.quay.quay_manifest_label_info:
    image: production/smallimage@sha256:4f6f...e797
    key: architecture
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: label_info
"""

RETURN = r"""
labels:
  description: List of the labels in the manifest.
  returned: always
  type: list
  elements: dict
  contains:
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
        - Whether the label has been set by the Containerfile/Dockerfile
          manifest (C(manifest)), or by an API call or from the web UI (C(api)).
        - Labels set in Containerfile/Dockerfile manifests are read-only.
      returned: always
      type: str
      sample: api
    media_type:
      description: Format of the label (C(text/plain) or C(application/json)).
      returned: always
      type: str
      sample: text/plain
  sample: [
            {
              "value": "SoftwareCollections.org <sclorg@redhat.com>",
              "media_type": "text/plain",
              "id": "1f5ccf29-9013-49ca-b1e7-864218b03f17",
              "key": "maintainer",
              "source_type": "manifest"
            },
            {
              "value": "2020-08-09 00:00:00+01:00",
              "media_type": "text/plain",
              "id": "d6e6ea21-d132-4ad9-97bf-05997e1f2b9d",
              "key": "org.opencontainers.image.created",
              "source_type": "manifest"
            },
            {
              "value": "GPLv2",
              "media_type": "text/plain",
              "id": "6a657897-0a40-4de0-a531-b45f751deb0f",
              "key": "org.label-schema.license",
              "source_type": "manifest"
            },
            {
              "value": "Nginx 1.16",
              "media_type": "text/plain",
              "id": "79da339b-0324-45c5-a1a9-06ffd607c3bd",
              "key": "io.k8s.display-name",
              "source_type": "manifest"
            },
            {
              "value": "1.16",
              "media_type": "text/plain",
              "id": "6d2710d8-4a2b-4150-b578-877e1f4ab5a5",
              "key": "version",
              "source_type": "manifest"
            },
            {
              "value": "centos7/nginx-116-centos7",
              "media_type": "text/plain",
              "id": "ea9a9a03-9b16-49d2-a2b8-0e30e1a1c1c1",
              "key": "name",
              "source_type": "manifest"
            }
          ]
"""


from ..module_utils.api_module import APIModule
from ..module_utils.quay_image import QuayImage


def main():
    argument_spec = dict(
        image=dict(required=True),
        key=dict(no_log=True),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    image = module.params.get("image").strip("/")
    key = module.params.get("key")

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
        module.exit_json(changed=False, labels=[])

    # Get the digest
    if img.digest:
        manifest_digest = img.digest
    else:
        tags = module.get_tags(namespace, img.repository, img.tag, only_active_tags=False)
        if not tags:
            module.exit_json(changed=False, labels=[])
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
    if key:
        labels = [lbl for lbl in res.get("labels", []) if lbl.get("key") == key]
    else:
        labels = res.get("labels", [])

    module.exit_json(changed=False, labels=labels)


if __name__ == "__main__":
    main()
