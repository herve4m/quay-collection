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
module: quay_layer_info
short_description: Gather information about image layers in Red Hat Quay
description:
  - Gather information about the layers of an image in a repository.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  image:
    description:
      - Name of the image. The format is C(namespace)/C(repository):C(tag). The
        namespace can be an organization or a personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
      - If you omit the tag, then it defaults to C(latest).
    required: true
    type: str
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.token
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
    id:
      description: Internal identifier of the layer.
      type: str
      returned: always
      sample: a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c
    sort_index:
      description: Index of the layer in the image.
      type: int
      returned: always
      sample: 4
    ancestors:
      description: Forward slash separated list of the parent layer identifiers.
      type: str
      returned: always
      sample: /f243...b231/15e0...2e36/a52c...327c/
    command:
      description: The command that was used to build the layer.
      type: list
      elements: str
      returned: always
      sample: ["/bin/sh", "-c", "#(nop) ", "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"]
    created:
      description: Layer creation date and time.
      type: str
      returned: always
      sample: Thu, 30 Sep 2021 07:18:56 -0000
  sample: [
            {
                "ancestors":
                "/f757...6b36/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/",
                "command": [
                    "/bin/sh",
                    "-c",
                    "#(nop) ",
                    "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"
                ],
                "comment": null,
                "created": "Thu, 16 Nov 2017 22:24:13 -0000",
                "id": "3f7885b48af404b0b9fffb2120e5907929504b33a104894762e4e192f5db9e63",
                "size": 32,
                "sort_index": 6,
                "uploading": false
            },
            {
                "ancestors": "/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/",
                "command": [
                    "/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp"
                ],
                "comment": null,
                "created": "Thu, 16 Nov 2017 22:24:12 -0000",
                "id": "f7573df3a79319ce013ada220edea02c4def0bb2938d059313ca3b50c22c6b36",
                "size": 32,
                "sort_index": 5,
                "uploading": false
            },
            {
                "ancestors": "/e619...cc21/f243...b231/15e0...2e36/a52c...327c/",
                "command": [
                    "/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot "
                ],
                "comment": null,
                "created": "Thu, 16 Nov 2017 22:24:11 -0000",
                "id": "e6f4fbbb429f4a42e138489b72fc451df7567750bfb28dfa81a4f93fb31b4f62",
                "size": 848185,
                "sort_index": 4,
                "uploading": false
            },
            {
                "ancestors": "/f243...b231/15e0...2e36/a52c...327c/",
                "command": [
                    "/bin/sh -c apk -U add dnsmasq curl"
                ],
                "comment": null,
                "created": "Thu, 16 Nov 2017 22:24:10 -0000",
                "id": "e6197fd52d52021b186662d4477d11db4520cbca280883245ef31cc4e2b3cc21",
                "size": 2010338,
                "sort_index": 3,
                "uploading": false
            },
            {
                "ancestors": "/15e0...2e36/a52c...327c/",
                "command": [
                    "/bin/sh -c #(nop)  MAINTAINER Dalton Hubble <dalton.hubble@coreos.com>"
                ],
                "comment": null,
                "created": "Thu, 16 Nov 2017 22:24:04 -0000",
                "id": "f2435a32f659b4a4568fbad867e9b88fa421586ab171ee2cd8096217e7ecb231",
                "size": 32,
                "sort_index": 2,
                "uploading": false
            },
            {
                "ancestors": "/a52c...327c/",
                "command": [
                    "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]"
                ],
                "comment": null,
                "created": "Wed, 13 Sep 2017 14:32:26 -0000",
                "id": "15e0dc04655d169bbdc7e942756a594e808c6c50214aca9b97deb36715ec2e36",
                "size": 32,
                "sort_index": 1,
                "uploading": false
            },
            {
                "ancestors": "//",
                "command": [
                    "/bin/sh -c #(nop) ADD file:4583...9e45 in / "
                ],
                "comment": null,
                "created": "Wed, 13 Sep 2017 14:32:26 -0000",
                "id": "a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c",
                "size": 1990402,
                "sort_index": 0,
                "uploading": false
            }
        ]
"""

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(image=dict(required=True))

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("image").strip("/:")

    # Get the tag from "namespace/repository:tag"
    try:
        repo, tag = name.rsplit(":", 1)
    except ValueError:
        repo = name
        tag = "latest"

    # Get the namespace and the repository
    my_name = module.who_am_i()
    try:
        namespace, repo_shortname = repo.split("/", 1)
    except ValueError:
        # No namespace part in the repository name. Therefore, the repository
        # is in the user's personal namespace
        if my_name:
            namespace = my_name
            repo_shortname = repo
        else:
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

    # Get the layers
    #
    # GET /api/v1/repository/{namespace}/{repository}/tag/{tag}/images?owned=false
    # {
    #   "images": [
    #     {
    #       "comment": null,
    #       "ancestors":
    #         "/f757...6b36/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/",
    #       "created": "Thu, 16 Nov 2017 22:24:13 -0000",
    #       "uploading": false,
    #       "sort_index": 6,
    #       "command": [
    #         "/bin/sh",
    #         "-c",
    #         "#(nop) ",
    #         "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"
    #       ],
    #       "id": "3f78...9e63",
    #       "size": 32
    #     },
    #     {
    #       "comment": null,
    #       "ancestors": "/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/",
    #       "created": "Thu, 16 Nov 2017 22:24:12 -0000",
    #       "uploading": false,
    #       "sort_index": 5,
    #       "command": [
    #         "/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp"
    #       ],
    #       "id": "f757...6b36",
    #       "size": 32
    #     },
    #     {
    #       "comment": null,
    #       "ancestors": "/e619...cc21/f243...b231/15e0...2e36/a52c...327c/",
    #       "created": "Thu, 16 Nov 2017 22:24:11 -0000",
    #       "uploading": false,
    #       "sort_index": 4,
    #       "command": [
    #         "/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot "
    #       ],
    #       "id": "e6f4...4f62",
    #       "size": 848185
    #     },
    #     {
    #       "comment": null,
    #       "ancestors": "/f243...b231/15e0...2e36/a52c...327c/",
    #       "created": "Thu, 16 Nov 2017 22:24:10 -0000",
    #       "uploading": false,
    #       "sort_index": 3,
    #       "command": [
    #         "/bin/sh -c apk -U add dnsmasq curl"
    #       ],
    #       "id": "e619...cc21",
    #       "size": 2010338
    #     },
    #     {
    #       "comment": null,
    #       "ancestors": "/15e0...2e36/a52c...327c/",
    #       "created": "Thu, 16 Nov 2017 22:24:04 -0000",
    #       "uploading": false,
    #       "sort_index": 2,
    #       "command": [
    #         "/bin/sh -c #(nop)  MAINTAINER Dalton Hubble <dalton.hubble@coreos.com>"
    #       ],
    #       "id": "f243...b231",
    #       "size": 32
    #     },
    #     {
    #       "comment": null,
    #       "ancestors": "/a52c...327c/",
    #       "created": "Wed, 13 Sep 2017 14:32:26 -0000",
    #       "uploading": false,
    #       "sort_index": 1,
    #       "command": [
    #         "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]"
    #       ],
    #       "id": "15e0...2e36",
    #       "size": 32
    #     },
    #     {
    #       "comment": null,
    #       "ancestors": "//",
    #       "created": "Wed, 13 Sep 2017 14:32:26 -0000",
    #       "uploading": false,
    #       "sort_index": 0,
    #       "command": [
    #         "/bin/sh -c #(nop) ADD file:4583...9e45 in / "
    #       ],
    #       "id": "a52c...327c",
    #       "size": 1990402
    #     }
    #   ]
    # }
    images = module.get_object_path(
        "repository/{namespace}/{repository}/tag/{tag}/images",
        query_params={"owned": False},
        namespace=namespace,
        repository=repo_shortname,
        tag=tag,
    )

    # It seems that layers are already returned in reverse sort index but
    # make sure anyway
    module.exit_json(
        changed=False,
        layers=sorted(images.get("images", []), key=lambda k: k["sort_index"], reverse=True)
        if images
        else [],
    )


if __name__ == "__main__":
    main()
