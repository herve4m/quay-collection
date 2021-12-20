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
module: quay_tag
short_description: Manage Red Hat Quay image tags
description:
  - Create, delete, and update image tags.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  image:
    description:
      - Name of the existing image to tag. The format is
        C(namespace)/C(repository):C(tag). The namespace can be an organization
        or a personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
      - If you omit the tag, then it defaults to C(latest).
    required: true
    type: str
  tag:
    description:
      - When C(state=present), the I(tag) parameter provides the new tag to add
        to the image. If another image already uses that tag, then the module
        removes the tag from that other image first.
      - When C(state=absent), the I(tag) parameter indicates the tag to remove.
        If you do not set that I(tag) parameter, then the module removes the
        tag that you give in the image name with the I(image) parameter.
    type: str
  expiration:
    description:
      - Expiration date and time for the tag. The format is C(YYYYMMDDHHMM.SS)
        but you can change it by setting the I(expiration_format) parameter.
      - You cannot set an expiration date more that two years in the future.
        If you do so, then Quay forces the date at that two years boundary.
    type: str
  expiration_format:
    description:
      - Indicate the time format used in the I(expiration) parameter.
      - Based on default Python format (see
        U(https://docs.python.org/3/library/time.html#time.strftime)).
    type: str
    default: "%Y%m%d%H%M.%S"
  state:
    description:
      - If C(absent), then the module deletes the image which tag is given in
        the I(tag) parameter, or if not set, in the image name.
      - If C(present), then the module adds the tag in the I(tag) parameter to
        the image.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Repositories" permission.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure the latest tag is associated with the image that has tag v1.0.0
  herve4m.quay.quay_tag:
    image: ansibletestorg/ansibletestrepo:v1.0.0
    tag: latest
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure tag v0.0.8 expires May 25, 2023 at 16:30
  herve4m.quay.quay_tag:
    image: ansibletestorg/ansibletestrepo:v0.0.8
    expire: 202305251630.00
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure tag v0.0.8 does not expire anymore
  herve4m.quay.quay_tag:
    image: ansibletestorg/ansibletestrepo:v0.0.8
    expire: ""
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure tag v0.0.1 does not exist
  herve4m.quay.quay_tag:
    image: ansibletestorg/ansibletestrepo:v0.0.1
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

import time

from ..module_utils.api_module import APIModule
from ansible.module_utils._text import to_native


# From the core file module.
def get_timestamp_for_time(formatted_time, time_format):
    struct = time.strptime(formatted_time, time_format)
    return int(time.mktime(struct))


def main():
    argument_spec = dict(
        image=dict(required=True),
        tag=dict(),
        expiration=dict(),
        expiration_format=dict(default="%Y%m%d%H%M.%S"),
        state=dict(choices=["present", "absent"], default="present"),
    )

    mutually_exclusive = [("regexp", "search_string")]

    # Create a module for ourselves
    module = APIModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    # Extract our parameters
    image = module.params.get("image").strip("/")
    tag = module.params.get("tag")
    expiration = module.params.get("expiration")
    expiration_format = module.params.get("expiration_format")
    state = module.params.get("state")

    # Get the tag from "namespace/repository:tag"
    try:
        repo, existing_tag = image.rsplit(":", 1)
    except ValueError:
        repo = image
        existing_tag = "latest"

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
                ).format(name=image)
            )

    # Check whether namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )

    full_repo_name = "{namespace}/{repository}".format(
        namespace=namespace, repository=repo_shortname
    )

    # Remove the tag
    if state == "absent":
        tag_to_delete = tag if tag else existing_tag
        module.delete(
            True,
            "tag",
            tag_to_delete,
            "repository/{full_repo_name}/tag/{tag}",
            full_repo_name=full_repo_name,
            tag=tag_to_delete,
        )

    # No tag to set and no expiration date/time to update. Exit (no change)
    if (not tag or tag == existing_tag) and expiration is None:
        module.exit_json(changed=False)

    # Convert the expiration date/time to the epoch format
    if expiration:
        try:
            expiration_epoch = get_timestamp_for_time(expiration, expiration_format)
        except (ValueError, OverflowError) as e:
            module.fail_json(
                msg=(
                    "Error while obtaining timestamp for time {time}"
                    " using format {format}: {error}"
                ).format(
                    time=expiration,
                    format=expiration_format,
                    error=to_native(e, nonstring="simplerepr"),
                )
            )
    else:
        expiration_epoch = 0

    # Get the tag details for the image given in `image'
    #
    # GET /api/v1/repository/{namespace}/{repository}/tag/?specificTag={tag}
    # {
    #   "tags": [
    #             {
    #               "name": "v1.0.0",
    #               "reversion": false,
    #               "start_ts": 1633179652,
    #               "end_ts": 1633179654,
    #               "manifest_digest": "sha256:4f6f...5e797",
    #               "is_manifest_list": false,
    #               "size": 25343205,
    #               "docker_image_id": "e942...dbea",
    #               "image_id": "e942...dbea",
    #               "last_modified": "Sat, 02 Oct 2021 13:00:52 -0000",
    #               "expiration": "Sat, 02 Oct 2021 13:00:54 -0000"
    #             }
    #   ],
    #   "page": 1,
    #   "has_additional": false
    query_params = {
        "onlyActiveTags": True,
        "limit": 100,
        "page": 1,
        "specificTag": existing_tag,
    }
    tags = module.get_object_path(
        "repository/{namespace}/{repository}/tag/",
        query_params=query_params,
        namespace=namespace,
        repository=repo_shortname,
    )
    if not tags or "tags" not in tags or len(tags["tags"]) == 0:
        module.fail_json(
            msg="The {tag} tag does not exist for the {image} image.".format(
                tag=existing_tag, image=full_repo_name
            )
        )
    if "manifest_digest" not in tags["tags"][0]:
        module.fail_json(
            msg="Cannot retrieve the manifest digest for the {image}:{tag} image.".format(
                tag=existing_tag, image=full_repo_name
            )
        )

    # The return object has the expiration date in epoch format in the `end_ts'
    # key. However, the PUT action use the `expiration' key to define that
    # date.
    # Copy the `end_ts' attribute to `expiration' in the returned object so
    # that both object will use the same key for the same thing.
    tag_details = tags["tags"][0]
    if "end_ts" in tag_details:
        tag_details["expiration"] = tag_details["end_ts"]

    new_fields = {}
    # The user did not provide the `tag' parameter. Update the tag provided in
    # the `image' parameter.
    if not tag or tag == existing_tag:
        if expiration is not None:
            new_fields["expiration"] = expiration_epoch if expiration_epoch else None
        module.update(
            tag_details,
            "tag",
            existing_tag,
            "repository/{full_repo_name}/tag/{tag}",
            new_fields,
            full_repo_name=full_repo_name,
            tag=existing_tag,
        )

    # The user has specified a tag in `tag'. Verify if that tag already exists
    # and if it points to the same image as the one provided in `image'.
    query_params["specificTag"] = tag
    tags = module.get_object_path(
        "repository/{namespace}/{repository}/tag/",
        query_params=query_params,
        namespace=namespace,
        repository=repo_shortname,
    )

    # The two tags point to the same image.
    if (
        tags
        and len(tags.get("tags", [])) > 0
        and tags["tags"][0].get("manifest_digest") == tag_details["manifest_digest"]
    ):
        new_tag_details = tags["tags"][0]
        if "end_ts" in new_tag_details:
            new_tag_details["expiration"] = new_tag_details["end_ts"]
        created = False
    else:
        # Create the tag
        module.unconditional_update(
            "tag",
            tag,
            "repository/{full_repo_name}/tag/{tag}",
            {"manifest_digest": tag_details["manifest_digest"]},
            full_repo_name=full_repo_name,
            tag=tag,
        )
        new_tag_details = {}
        created = True

    if expiration is not None:
        new_fields["expiration"] = expiration_epoch if expiration_epoch else None
    updated, _ = module.update(
        new_tag_details,
        "tag",
        tag,
        "repository/{full_repo_name}/tag/{tag}",
        new_fields,
        auto_exit=False,
        full_repo_name=full_repo_name,
        tag=tag,
    )
    module.exit_json(changed=created or updated)


if __name__ == "__main__":
    main()
