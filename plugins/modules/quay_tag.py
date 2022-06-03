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
module: quay_tag
short_description: Manage Red Hat Quay image tags
description:
  - Create, delete, and update image tags.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  image:
    description:
      - Name of the existing image. The format is
        C(namespace)/C(repository):C(tag) or
        C(namespace)/C(repository)@C(digest). The namespace can be an
        organization or a personal namespace.
      - If you omit the namespace part, then the module looks for the
        repository in your personal namespace.
      - If you omit the tag and the digest part, then C(latest) is assumed.
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
      - When you specify the image by its digest, in the I(image) parameter,
        then that I(tag) parameter is mandatory.
    type: str
  expiration:
    description:
      - Expiration date and time for the tag. The format is C(YYYYMMDDHHMM.SS)
        but you can change it by setting the I(expiration_format) parameter.
      - You cannot set an expiration date more that two years in the future.
        If you do so, then Quay forces the date at that two years boundary.
      - You cannot set an expiration date in the past.
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
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.token
  - herve4m.quay.auth.user
"""

EXAMPLES = r"""
- name: Ensure the latest tag is associated with the image that has tag v1.0.0
  herve4m.quay.quay_tag:
    image: production/smallimage:v1.0.0
    tag: latest
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure tag v0.0.2 is associated to the image with the specified digest
  herve4m.quay.quay_tag:
    image: production/smallimage@sha256:4f6f...e797
    tag: v0.0.2
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure tag v0.0.8 expires May 25, 2023 at 16:30
  herve4m.quay.quay_tag:
    image: production/smallimage:v0.0.8
    expiration: 202305251630.00
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure tag v0.0.8 does not expire anymore
  herve4m.quay.quay_tag:
    image: production/smallimage:v0.0.8
    expiration: ""
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure tag v0.0.1 does not exist
  herve4m.quay.quay_tag:
    image: production/smallimage:v0.0.1
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

import time

from ..module_utils.api_module import APIModule
from ..module_utils.quay_image import QuayImage
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

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    image = module.params.get("image").strip("/")
    tag = module.params.get("tag")
    expiration = module.params.get("expiration")
    expiration_format = module.params.get("expiration_format")
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

    if img.digest and not tag:
        module.fail_json(
            msg="Because you use a digest in image, the tag parameter is mandatory."
        )

    # Check whether the namespace exists (organization or user account)
    namespace_details = module.get_namespace(namespace)
    if not namespace_details:
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )

    full_repo_name = "{namespace}/{repository}".format(
        namespace=namespace, repository=img.repository
    )

    # Remove the tag
    if state == "absent":
        if tag:
            tag_to_delete = tag
        else:
            # Because the user did not provide the tag attribute, remove the
            # tag given in the image attribute.
            tag_to_delete = img.tag
        module.delete(
            True,
            "tag",
            tag_to_delete,
            "repository/{full_repo_name}/tag/{tag}",
            full_repo_name=full_repo_name,
            tag=tag_to_delete,
        )

    # Get the tag details for the image given in `image'.
    # If the image is specified with a tag, then only one tag is returned.
    # If the image is specified with a digest, then several tags might be
    # returned.
    #   [
    #      {
    #        "name": "v1.0.0",
    #        "reversion": False,
    #        "start_ts": 1633179652,
    #        "end_ts": 1633179654,
    #        "manifest_digest": "sha256:4f6f...5e797",
    #        "is_manifest_list": False,
    #        "size": 25343205,
    #        "last_modified": "Sat, 02 Oct 2021 13:00:52 -0000",
    #        "expiration": "Sat, 02 Oct 2021 13:00:54 -0000"
    #      }
    #   ]
    tags = module.get_tags(namespace, img.repository, img.tag, img.digest)
    tag_list = [t["name"] for t in tags if "name" in t]

    # No tag to set and no expiration date/time to update. Exit (no change)
    if (not tag or tag in tag_list) and expiration is None:
        module.exit_json(changed=False)

    # Convert the expiration date/time to the epoch format
    if expiration:
        try:
            tms = get_timestamp_for_time(expiration, expiration_format)
            if tms <= int(time.time() + 10):
                module.fail_json(
                    msg=("You cannot set an expiration date in the past: {time}").format(
                        time=expiration,
                    )
                )
            new_fields = {"expiration": tms}
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
        new_fields = {"expiration": None}

    if not tag_list:
        module.fail_json(msg="The {image} image does not exist.".format(image=image))

    # No tag to set or the image has already the requested tag. Only the
    # expiration date has to be updated
    if not tag or tag in tag_list:
        # In the list of returned tags, locate the tag to update
        if not tag:
            tag_details = tags[0]
        else:
            for t in tags:
                if t.get("name") == tag:
                    tag_details = t
                    break

        # The return object has the expiration date in epoch format in the
        # `end_ts' key. However, the PUT action uses the `expiration' key to
        # define that date.
        # Copy the `end_ts' attribute to `expiration' in the returned object so
        # that both object will use the same key for the same thing.
        if "end_ts" in tag_details:
            tag_details["expiration"] = tag_details["end_ts"]

        # The user did not provide the `tag' parameter. Update the tag provided
        # in the `image' parameter.
        module.update(
            tag_details,
            "tag",
            tag_details["name"],
            "repository/{full_repo_name}/tag/{tag}",
            new_fields,
            full_repo_name=full_repo_name,
            tag=tag_details["name"],
        )

    try:
        manifest_digest = tags[0]["manifest_digest"]
    except KeyError:
        module.fail_json(
            msg="Cannot retrieve the manifest digest for the {image} image.".format(
                image=image
            )
        )

    # The user has specified a tag in `tag'. Verify if that tag already exists
    # and if it points to the same image as the one provided in `image'.
    tags = module.get_tags(namespace, img.repository, tag)

    # The two tags point to the same image. No need to create the tag, only
    # the expiration need updating.
    if len(tags) > 0 and tags[0].get("manifest_digest") == manifest_digest:
        new_tag_details = tags[0]
        if "end_ts" in new_tag_details:
            new_tag_details["expiration"] = new_tag_details["end_ts"]
        created = False
    else:
        # Create the tag
        module.unconditional_update(
            "tag",
            tag,
            "repository/{full_repo_name}/tag/{tag}",
            {"manifest_digest": manifest_digest},
            full_repo_name=full_repo_name,
            tag=tag,
        )
        new_tag_details = {}
        created = True

    updated, _not_used = module.update(
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
