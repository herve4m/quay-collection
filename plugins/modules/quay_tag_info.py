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
      - You cannot list tags in the personal namespace of other users. The
        token you use in I(quay_token) determines the user account you are
        using.
    required: true
    type: str
  tag:
    description:
      - Gather information on that specific tag instead of returning data on
        all the tags in the repository.
    type: str
  only_active_tags:
    description:
      - If C(yes), then the module only collects information on tags that have
        not expired. If C(no), then the module returns information on all the
        tags.
      - You can identify expired tags (when I(only_active_tags) is C(no)) in
        the returned data by inspecting the C(end_ts) or C(expiration)
        tag attributes. Those attributes provide the expiration date.
    type: bool
    default: no
notes:
  - The token that you provide in I(quay_token) must at least have the "View
    all visible repositories" permission.
extends_documentation_fragment: herve4m.quay.auth
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
    image_id:
      description: Identifier of the image associated with the tag.
      type: str
      returned: always
      sample: d53469b7e6ba9295a4b7a7d9e29537ab879e1582e64d534b6ed2637453dade25
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
              "docker_image_id": "be3e...29d4",
              "image_id": "be3e...29d4",
              "last_modified": "Thu, 30 Sep 2021 06:10:23 -0000"
            },
            {
              "name": "latest",
              "reversion": false,
              "start_ts": 1632982222,
              "manifest_digest": "sha256:9ce9...f3c7",
              "is_manifest_list": false,
              "size": 784538,
              "docker_image_id": "be3e...29d4",
              "image_id": "be3e...29d4",
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
              "docker_image_id": "bda4...29b2",
              "image_id": "bda4...29b2",
              "last_modified": "Thu, 30 Sep 2021 06:10:21 -0000",
              "expiration": "Fri, 24 Dec 2021 08:54:00 -0000"
            }
          ]
"""

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        repository=dict(required=True),
        tag=dict(),
        only_active_tags=dict(type="bool", default=False),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("repository").strip("/")
    tag = module.params.get("tag")
    only_active_tags = module.params.get("only_active_tags")

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

    # Get the tags
    #
    # GET /api/v1/repository/{namespace}/{repository}/tag/
    # {
    #   "tags": [
    #     {
    #       "name": "1.33.0",
    #       "reversion": false,
    #       "start_ts": 1632982224,
    #       "manifest_digest": "sha256:f948...95fe",
    #       "is_manifest_list": false,
    #       "size": 784606,
    #       "docker_image_id": "d25a...6d25",
    #       "image_id": "d25a...6d25",
    #       "last_modified": "Thu, 30 Sep 2021 06:10:24 -0000"
    #     },
    #     {
    #       "name": "latest",
    #       "reversion": false,
    #       "start_ts": 1632982222,
    #       "manifest_digest": "sha256:9ce9...f3c7",
    #       "is_manifest_list": false,
    #       "size": 784538,
    #       "docker_image_id": "be3e...29d4",
    #       "image_id": "be3e...29d4",
    #       "last_modified": "Thu, 30 Sep 2021 06:10:22 -0000"
    #     },
    #     {
    #       "name": "1.34.0",
    #       "reversion": false,
    #       "start_ts": 1632982221,
    #       "end_ts": 1640336040,
    #       "manifest_digest": "sha256:a8f2...5ea7",
    #       "is_manifest_list": false,
    #       "size": 802700,
    #       "docker_image_id": "bda4...29b2",
    #       "image_id": "bda4...29b2",
    #       "last_modified": "Thu, 30 Sep 2021 06:10:21 -0000",
    #       "expiration": "Fri, 24 Dec 2021 08:54:00 -0000"
    #     },
    #     {
    #       "name": "latest",
    #       "reversion": false,
    #       "start_ts": 1632921128,
    #       "end_ts": 1632982222,
    #       "manifest_digest": "sha256:9ce9...f3c7",
    #       "is_manifest_list": false,
    #       "size": 784538,
    #       "docker_image_id": "be3e...29d4",
    #       "image_id": "be3e...29d4",
    #       "last_modified": "Wed, 29 Sep 2021 13:12:08 -0000",
    #       "expiration": "Thu, 30 Sep 2021 06:10:22 -0000"
    #     }
    #   ],
    #   "page": 1,
    #   "has_additional": false
    query_params = {"onlyActiveTags": only_active_tags, "limit": 100}
    if tag:
        query_params["specificTag"] = tag
    tag_list = []
    page = 1
    while True:
        query_params["page"] = page

        tags = module.get_object_path(
            "repository/{namespace}/{repository}/tag/",
            query_params=query_params,
            namespace=namespace,
            repository=repo_shortname,
        )
        if tags:
            tag_list.extend(tags.get("tags", []))
            if tags.get("has_additional", False):
                page += 1
                continue
        break

    module.exit_json(changed=False, tags=tag_list)


if __name__ == "__main__":
    main()
