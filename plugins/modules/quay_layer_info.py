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


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_layer_info
short_description: Gather information about image layers in Quay Container Registry
description:
  - Gather information about the layers of an image in a repository.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  image:
    description:
      - Name of the image. The format is C(namespace)/C(repository):C(tag) or
        C(namespace)/C(repository)@C(digest). The namespace can be an
        organization or a personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
      - If you omit the tag and the digest part, then C(latest) is assumed.
    required: true
    type: str
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Retrieve the layers of the coreos/dnsmasq:latest image
  herve4m.quay.quay_layer_info:
    image: coreos/dnsmasq:latest
    quay_host: quay.io
  register: layers
"""

RETURN = r"""
layers:
  description: Sorted list of the image layers. The top layer is listed first.
  returned: always
  type: list
  elements: dict
  contains:
    index:
      description: Index of the layer in the image.
      type: int
      returned: always
      sample: 4
    command:
      description: The command that was used to build the layer.
      type: list
      elements: str
      returned: always
      sample: ["/bin/sh", "-c", "#(nop) ", "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"]
    created_datetime:
      description: Layer creation date and time.
      type: str
      returned: always
      sample: Thu, 30 Sep 2021 07:18:56 -0000
  sample: [
            {
              "index": 6,
              "compressed_size": null,
              "is_remote": false,
              "urls": null,
              "command": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"
              ],
              "comment": null,
              "author": "Dalton Hubble <...>",
              "blob_digest": "sha256:a3ed...46d4",
              "created_datetime": "Thu, 16 Nov 2017 22:24:12 -0000"
            },
            {
              "index": 5,
              "compressed_size": null,
              "is_remote": false,
              "urls": null,
              "command": [
                "/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp"
              ],
              "comment": null,
              "author": "Dalton Hubble <...>",
              "blob_digest": "sha256:a3e...46d4",
              "created_datetime": "Thu, 16 Nov 2017 22:24:12 -0000"
            },
            {
              "index": 4,
              "compressed_size": null,
              "is_remote": false,
              "urls": null,
              "command": [
                "/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot "
              ],
              "comment": null,
              "author": "Dalton Hubble <...>",
              "blob_digest": "sha256:e40d...0351",
              "created_datetime": "Thu, 16 Nov 2017 22:24:11 -0000"
            },
            {
              "index": 3,
              "compressed_size": null,
              "is_remote": false,
              "urls": null,
              "command": [
                "/bin/sh -c apk -U add dnsmasq curl"
              ],
              "comment": null,
              "author": "Dalton Hubble <...>",
              "blob_digest": "sha256:7ef3...3a74",
              "created_datetime": "Thu, 16 Nov 2017 22:24:09 -0000"
            },
            {
              "index": 2,
              "compressed_size": null,
              "is_remote": false,
              "urls": null,
              "command": [
                "/bin/sh -c #(nop)  MAINTAINER Dalton Hubble <...>"
              ],
              "comment": null,
              "author": "Dalton Hubble <...>",
              "blob_digest": "sha256:a3ed...46d4",
              "created_datetime": "Thu, 16 Nov 2017 22:24:04 -0000"
            },
            {
              "index": 1,
              "compressed_size": null,
              "is_remote": false,
              "urls": null,
              "command": [
                "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]"
              ],
              "comment": null,
              "author": null,
              "blob_digest": "sha256:a3ed...46d4",
              "created_datetime": "Wed, 13 Sep 2017 14:32:26 -0000"
            },
            {
              "index": 0,
              "compressed_size": null,
              "is_remote": false,
              "urls": null,
              "command": [
                "/bin/sh -c #(nop) ADD file:4583...9e45 in / "
              ],
              "comment": null,
              "author": null,
              "blob_digest": "sha256:6d98...d913",
              "created_datetime": "Wed, 13 Sep 2017 14:32:25 -0000"
            }
        ]
"""

from ..module_utils.api_module import APIModule
from ..module_utils.quay_image import QuayImage


def main():
    argument_spec = dict(image=dict(required=True))

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("image").strip("/:")

    # Get the components of the given image (namespace, repository, tag, digest)
    img = QuayImage(module, name)
    namespace = img.namespace
    if namespace is None:
        module.fail_json(
            msg=(
                "The `image' parameter must include the"
                " organization: <organization>/{name}."
            ).format(name=name)
        )

    # Check whether namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        module.exit_json(changed=False, layers=[])

    # Get the digest
    if img.digest:
        manifest_digest = img.digest
    else:
        tags = module.get_tags(namespace, img.repository, img.tag, only_active_tags=False)
        if not tags:
            module.exit_json(changed=False, layers=[])
        try:
            manifest_digest = tags[0]["manifest_digest"]
        except KeyError:
            module.fail_json(
                msg="Cannot retrieve the manifest digest for the {image} image.".format(
                    image=name
                )
            )

    # Get the layers
    #
    # GET /api/v1/repository/{namespace}/{repository}/manifest/{digest}
    # {
    #   "digest": "sha256:53b2...a7c8",
    #   "is_manifest_list": false,
    #   "manifest_data": "{\n   \"schemaVersion\": 1,\n ... }",
    #   "config_media_type": null,
    #   "layers": [
    #     {
    #       "index": 0,
    #       "compressed_size": null,
    #       "is_remote": false,
    #       "urls": null,
    #       "command": [
    #         "/bin/sh -c #(nop) ADD file:4583...9e45 in / "
    #       ],
    #       "comment": null,
    #       "author": null,
    #       "blob_digest": "sha256:6d98...d913",
    #       "created_datetime": "Wed, 13 Sep 2017 14:32:25 -0000"
    #     },
    #     {
    #       "index": 1,
    #       "compressed_size": null,
    #       "is_remote": false,
    #       "urls": null,
    #       "command": [
    #         "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]"
    #       ],
    #       "comment": null,
    #       "author": null,
    #       "blob_digest": "sha256:a3ed...46d4",
    #       "created_datetime": "Wed, 13 Sep 2017 14:32:26 -0000"
    #     },
    #     {
    #       "index": 2,
    #       "compressed_size": null,
    #       "is_remote": false,
    #       "urls": null,
    #       "command": [
    #         "/bin/sh -c #(nop)  MAINTAINER Dalton Hubble <...>"
    #       ],
    #       "comment": null,
    #       "author": "Dalton Hubble <...>",
    #       "blob_digest": "sha256:a3ed...46d4",
    #       "created_datetime": "Thu, 16 Nov 2017 22:24:04 -0000"
    #     },
    #     {
    #       "index": 3,
    #       "compressed_size": null,
    #       "is_remote": false,
    #       "urls": null,
    #       "command": [
    #         "/bin/sh -c apk -U add dnsmasq curl"
    #       ],
    #       "comment": null,
    #       "author": "Dalton Hubble <...>",
    #       "blob_digest": "sha256:7ef3...3a74",
    #       "created_datetime": "Thu, 16 Nov 2017 22:24:09 -0000"
    #     },
    #     {
    #       "index": 4,
    #       "compressed_size": null,
    #       "is_remote": false,
    #       "urls": null,
    #       "command": [
    #         "/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot "
    #       ],
    #       "comment": null,
    #       "author": "Dalton Hubble <...>",
    #       "blob_digest": "sha256:e40d...0351",
    #       "created_datetime": "Thu, 16 Nov 2017 22:24:11 -0000"
    #     },
    #     {
    #       "index": 5,
    #       "compressed_size": null,
    #       "is_remote": false,
    #       "urls": null,
    #       "command": [
    #         "/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp"
    #       ],
    #       "comment": null,
    #       "author": "Dalton Hubble <...>",
    #       "blob_digest": "sha256:a3ed...46d4",
    #       "created_datetime": "Thu, 16 Nov 2017 22:24:12 -0000"
    #     },
    #     {
    #       "index": 6,
    #       "compressed_size": null,
    #       "is_remote": false,
    #       "urls": null,
    #       "command": [
    #         "/bin/sh",
    #         "-c",
    #         "#(nop) ",
    #         "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"
    #       ],
    #       "comment": null,
    #       "author": "Dalton Hubble <...>",
    #       "blob_digest": "sha256:a3ed...46d4",
    #       "created_datetime": "Thu, 16 Nov 2017 22:24:12 -0000"
    #     }
    #   ]
    # }
    images = module.get_object_path(
        "repository/{namespace}/{repository}/manifest/{manifest_digest}",
        namespace=namespace,
        repository=img.repository,
        manifest_digest=manifest_digest,
    )

    # Sort the layers in reverse sort index
    module.exit_json(
        changed=False,
        layers=(
            sorted(images.get("layers", []), key=lambda k: k["index"], reverse=True)
            if images
            else []
        ),
    )


if __name__ == "__main__":
    main()
