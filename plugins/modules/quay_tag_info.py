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
module: quay_tag_info
short_description: Gather information about tags in a Red Hat Quay repository
description:
  - Gather information about the tags in a repository.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  repository:
    description:
      - Name of the repository that contains the tags to list. The format is
        C(namespace)/C(shortname). The namespace can be an organization or a
        personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
    required: true
    type: str
  tag:
    description:
      - Gather information on that specific tag instead of returning data on
        all the tags in the repository.
      - Mutually exclusive with I(digest).
    type: str
  digest:
    description:
      - Gather information on the images with that digest instead of returning
        data on all the tags in the repository.
      - Mutually exclusive with I(tag).
    type: str
  only_active_tags:
    description:
      - If C(yes), then the module only collects information on tags that have
        not expired and have not been deleted. If C(no), then the module
        returns information on all the tags.
      - You can identify expired and deleted tags (when I(only_active_tags) is
        C(no)) in the returned data by inspecting the C(end_ts) or
        C(expiration) tag attributes. Those attributes provide the expiration
        or deletion date.
    type: bool
    default: no
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Retrieve the tags in the production/smallimage repository
  herve4m.quay.quay_tag_info:
    repository: production/smallimage
    only_active_tags: true
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: tags

- name: Gather info on tag 0.1.2 of the testing image in my personal namespace
  herve4m.quay.quay_tag_info:
    repository: testimg
    tag: "0.1.2"
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: tag_info

- name: Retrieve the tags from the images with the given digest
  herve4m.quay.quay_tag_info:
    repository: production/smallimage
    digest: "sha256:53b2...a7c8"
    only_active_tags: true
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
  register: tags
"""

RETURN = r"""
tags:
  description: List of the tags in the repository.
  returned: always
  type: list
  elements: dict
  contains:
    name:
      description: Tag identifier.
      type: str
      returned: always
      sample: 0.1.2
    size:
      description: Size of the associated image in bytes.
      type: int
      returned: always
      sample: 802700
    manifest_digest:
      description:
        - SHA256 digest for the tag.
        - You can use that digest to pull the image instead of using the tag
          name. For example,
          C(podman pull quay.example.com/production/smallimage@sha256:a8f2...5ea7)
      type: str
      returned: always
      sample: sha256:a8f231c07da40107543d74ed1e9a1938a004b498377dbefcf29082c7a9e55ea7
    start_ts:
      description: Time in seconds since the epoch of the last tag modification.
      type: int
      returned: always
      sample: 1632982222
    last_modified:
      description:
        - Date and time of the last tag modification in a human readable format.
      type: str
      returned: always
      sample: Thu, 30 Sep 2021 06:10:22 -0000
    end_ts:
      description:
        - Time in seconds since the epoch of the tag expiration.
        - The module only returns expired tags when the I(only_active_tags)
          parameter is C(no).
      type: int
      returned: only when an expiration date has been explicitly assigned.
      sample: 1640336040
    expiration:
      description: Expiration date and time in a human readable format.
      type: str
      returned: only when an expiration date has been explicitly assigned.
      sample: Fri, 24 Dec 2021 08:54:00 -0000
  sample: [
            {
              "name": "1.33.1",
              "reversion": false,
              "start_ts": 1632982223,
              "manifest_digest": "sha256:9ce9...f3c7",
              "is_manifest_list": false,
              "size": 784538,
              "last_modified": "Thu, 30 Sep 2021 06:10:23 -0000"
            },
            {
              "name": "latest",
              "reversion": false,
              "start_ts": 1632982222,
              "manifest_digest": "sha256:9ce9...f3c7",
              "is_manifest_list": false,
              "size": 784538,
              "last_modified": "Thu, 30 Sep 2021 06:10:22 -0000"
            },
            {
              "name": "1.34.0",
              "reversion": false,
              "start_ts": 1632982221,
              "end_ts": 1640336040,
              "manifest_digest": "sha256:a8f2...5ea7",
              "is_manifest_list": false,
              "size": 802700,
              "last_modified": "Thu, 30 Sep 2021 06:10:21 -0000",
              "expiration": "Fri, 24 Dec 2021 08:54:00 -0000"
            }
          ]
"""

from ..module_utils.api_module import APIModule
from ..module_utils.quay_image import QuayImage


def main():
    argument_spec = dict(
        repository=dict(required=True),
        tag=dict(),
        digest=dict(),
        only_active_tags=dict(type="bool", default=False),
    )

    mutually_exclusive = [("tag", "digest")]

    # Create a module for ourselves
    module = APIModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    # Extract our parameters
    name = module.params.get("repository").strip("/")
    tag = module.params.get("tag")
    digest = module.params.get("digest")
    only_active_tags = module.params.get("only_active_tags")

    # Get the components of the given image (namespace, repository)
    img = QuayImage(module, name)
    namespace = img.namespace
    if namespace is None:
        module.fail_json(
            msg=(
                "The `repository' parameter must include the"
                " organization: <organization>/{name}."
            ).format(name=name)
        )

    # Check whether namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        module.exit_json(changed=False, tags=[])

    # Get the tags
    #   [
    #     {
    #       "name": "1.33.0",
    #       "reversion": False,
    #       "start_ts": 1632982224,
    #       "manifest_digest": "sha256:f948...95fe",
    #       "is_manifest_list": False,
    #       "size": 784606,
    #       "last_modified": "Thu, 30 Sep 2021 06:10:24 -0000"
    #     },
    #     {
    #       "name": "latest",
    #       "reversion": False,
    #       "start_ts": 1632982222,
    #       "manifest_digest": "sha256:9ce9...f3c7",
    #       "is_manifest_list": False,
    #       "size": 784538,
    #       "last_modified": "Thu, 30 Sep 2021 06:10:22 -0000"
    #     },
    #     {
    #       "name": "1.34.0",
    #       "reversion": False,
    #       "start_ts": 1632982221,
    #       "end_ts": 1640336040,
    #       "manifest_digest": "sha256:a8f2...5ea7",
    #       "is_manifest_list": False,
    #       "size": 802700,
    #       "last_modified": "Thu, 30 Sep 2021 06:10:21 -0000",
    #       "expiration": "Fri, 24 Dec 2021 08:54:00 -0000"
    #     },
    #     {
    #       "name": "latest",
    #       "reversion": False,
    #       "start_ts": 1632921128,
    #       "end_ts": 1632982222,
    #       "manifest_digest": "sha256:9ce9...f3c7",
    #       "is_manifest_list": False,
    #       "size": 784538,
    #       "last_modified": "Wed, 29 Sep 2021 13:12:08 -0000",
    #       "expiration": "Thu, 30 Sep 2021 06:10:22 -0000"
    #     }
    #   ]
    tag_list = module.get_tags(namespace, img.repository, tag, digest, only_active_tags)
    module.exit_json(changed=False, tags=tag_list)


if __name__ == "__main__":
    main()
