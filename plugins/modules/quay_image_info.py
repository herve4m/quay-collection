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

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_image_info
short_description: Gather information about images in a Red Hat Quay repository
description:
  - Gather information about images in a repository.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  repository:
    description:
      - Name of the repository that contains the images to list. The format is
        C(namespace)/C(shortname). The namespace can be an organization or a
        personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
      - You cannot list images in the personal namespace of other users. The
        token you use in I(quay_token) determines the user account you are
        using.
    required: true
    type: str
notes:
  - The token that you provide in I(quay_token) must at least have the "View
    all visible repositories" permission.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Retrieve the images in the production/smallimage repository
  herve4m.quay.quay_image_info:
    repository: production/smallimage
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: images
"""

RETURN = r"""
images:
  description: List of the images in the repository.
  returned: always
  type: list
  elements: dict
  contains:
    tags:
      description: Tags associated with the image.
      type: list
      elements: str
      returned: always
      sample:
        - latest
        - 1.33.1
    id:
      description: Internal identifier of the image.
      type: str
      returned: always
      sample: d53469b7e6ba9295a4b7a7d9e29537ab879e1582e64d534b6ed2637453dade25
    created:
      description: Image creation date.
      type: str
      returned: always
      sample: Thu, 30 Sep 2021 07:18:56 -0000
  sample: [
            {
                "ancestors": "",
                "command": "",
                "comment": "",
                "created": "Thu, 30 Sep 2021 06:10:21 -0000",
                "id": "d534...de25",
                "size": 0,
                "sort_index": 0,
                "tags": [
                    "1.34.0"
                ],
                "uploading": false
            },
            {
                "ancestors": "",
                "command": "",
                "comment": "",
                "created": "Thu, 30 Sep 2021 06:10:22 -0000",
                "id": "be3e...29d4",
                "size": 0,
                "sort_index": 0,
                "tags": [
                    "latest",
                    "1.33.1"
                ],
                "uploading": false
            }
          ]
"""

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(repository=dict(required=True))

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("repository").strip("/")

    my_name = module.who_am_i()
    try:
        namespace, repo_shortname = name.split("/", 1)
    except ValueError:
        # No namespace part in the repository name. Therefore, the repository
        # is in the user's personal namespace
        namespace = my_name
        repo_shortname = name

    # Check whether namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        module.exit_json(changed=False, images=[])
    # Make sure that the current user is the owner of that namespace
    if (
        not namespace_details.get("is_organization")
        and namespace_details.get("name") != my_name
    ):
        module.fail_json(
            msg="You ({user}) are not the owner of {namespace}'s namespace.".format(
                user=my_name, namespace=namespace
            )
        )

    # Get the images
    #
    # GET /api/v1/repository/{namespace}/{repository}/image/
    # {
    #   "images": [
    #     {
    #       "id": "bda46e5356a27da3796e2eb49ab3d5678b61b894e2a5763dd45b249be3d729b2",
    #       "created": "Thu, 30 Sep 2021 06:10:21 -0000",
    #       "comment": "",
    #       "command": "",
    #       "size": 0,
    #       "uploading": false,
    #       "sort_index": 0,
    #       "tags": [
    #         "1.34.0"
    #       ],
    #       "ancestors": ""
    #     },
    #     {
    #       "id": "be3e4a5769a324347abd4eb36272e5948e2068b3a6dda975526e97deb5b629d4",
    #       "created": "Thu, 30 Sep 2021 06:10:22 -0000",
    #       "comment": "",
    #       "command": "",
    #       "size": 0,
    #       "uploading": false,
    #       "sort_index": 0,
    #       "tags": [
    #         "latest",
    #         "1.33.1",
    #         "test"
    #       ],
    #       "ancestors": ""
    #     },
    #     {
    #       "id": "d25a39b7d69a25b76d32439ebdb4e562845fa8d37a9a56724ae95347be4e6d25",
    #       "created": "Thu, 30 Sep 2021 06:10:24 -0000",
    #       "comment": "",
    #       "command": "",
    #       "size": 0,
    #       "uploading": false,
    #       "sort_index": 0,
    #       "tags": [
    #         "1.33.0"
    #       ],
    #       "ancestors": ""
    #     }
    #   ]
    # }
    images = module.get_object_path(
        "repository/{namespace}/{repository}/image/",
        namespace=namespace,
        repository=repo_shortname,
    )

    module.exit_json(changed=False, images=images.get("images", []) if images else [])


if __name__ == "__main__":
    main()
