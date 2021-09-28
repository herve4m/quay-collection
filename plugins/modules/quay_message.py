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
#
# Note:
#  - The API does not allow updating a message. When the module needs to update
#    the message, the module deletes it and then recreates it.
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: quay_message
short_description: Manage Red Hat Quay global messages
description:
  - Create, delete, and update global messages (message of the day) that
    display on the web UI pages.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  content:
    description:
      - Text of the message to display on each web UI page.
    type: str
  severity:
    description:
      - Severity of the message.
      - If you do not set this parameter, then the module creates the message
        with the C(info) severity.
    type: str
    choices: [info, warning, error]
  format:
    description:
      - Format of the text in C(content).
      - If you do not set this parameter, then the module uses the C(plain)
        format.
    type: str
    aliases: [ media_type ]
    choices: [markdown, plain]
  regexp:
    description:
      - The regular expression to look for in the existing messages. This does
        not have to match an entire line.
      - For C(state=present), if several messages match then the module updates
        one and deletes the others.
      - For C(state=absent), the module deletes all the messages that match.
      - Uses Python regular expressions. See
        U(https://docs.python.org/3/library/re.html).
      - Mutually exclusive with C(search_string).
    type: str
    aliases: [regex]
  search_string:
    description:
      - The literal string to look for in the existing messages. This does not
        have to match an entire line.
      - For C(state=present), if several messages match then the module updates
        one and deletes the others.
      - For C(state=absent), the module deletes all the messages that match.
      - Mutually exclusive with C(regexp).
    type: str
  search_severity:
    description:
      - Search messages by their severity level.
      - If you also set C(search_string), C(regexp), or C(content), messages
        must match all those criteria.
    type: str
    choices: [info, warning, error]
  state:
    description:
      - If C(absent), then the module deletes all the messages which content
        matches C(search_string), C(regexp), C(content), or C(search_severity).
      - If C(present), then the module creates the message if it does not
        already exist (that is, if no message matches C(search_string),
        C(regexp), or C(content)). Is several messages match, only one is
        updated and the others are deleted.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in C(quay_token) must have the
    "Super User Access" permission.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure the message of the day is published
  herve4m.quay.quay_message:
    content: |
      # Information message

      Lorem **ipsum** dolor sit amet, `consectetur` adipiscing elit, sed do
      eiusmod tempor incididunt ut labore et dolore magna aliqua:

      * Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
        ut aliquip ex ea commodo consequat.
      *  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
         dolore eu fugiat nulla pariatur
    format: markdown
    severity: info
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure a message in plain text is published
  herve4m.quay.quay_message:
    content: System maintenance tomorrow at 6 AM
    format: plain
    severity: info
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the message severity is upgraded to warning
  herve4m.quay.quay_message:
    content: System maintenance tomorrow at 6 AM
    severity: warning
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the message content is updated
  herve4m.quay.quay_message:
    content: System maintenance tomorrow at 7 AM
    # Find the message to update by a matching string
    search_string: tomorrow at 6 AM
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the existing message as an error priority now
  herve4m.quay.quay_message:
    # Find the message to update by a matching string
    search_string: incididunt ut labore et dolore
    severity: error
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the warning message is removed
  herve4m.quay.quay_message:
    # Find the message to delete by its exact content
    content: System maintenance tomorrow at 7 AM
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the messages of the day are removed
  herve4m.quay.quay_message:
    # Find the messages to delete by a matching regular expression
    regexp: 'message\s+of\s+the\s+day'
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the lorem ipsum error messages are removed
  herve4m.quay.quay_message:
    # Find the messages to delete by a matching string and severity
    search_string: lorem ipsum
    search_severity: error
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure all the warning messages are removed
  herve4m.quay.quay_message:
    search_severity: warning
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

import re

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        content=dict(),
        severity=dict(choices=["info", "warning", "error"]),
        format=dict(choices=["markdown", "plain"], aliases=["media_type"]),
        regexp=dict(aliases=["regex"]),
        search_string=dict(),
        search_severity=dict(choices=["info", "warning", "error"]),
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
    content = module.params.get("content")
    severity = module.params.get("severity")
    format = module.params.get("format")
    regexp = module.params.get("regexp")
    search_string = module.params.get("search_string")
    search_severity = module.params.get("search_severity")
    state = module.params.get("state")

    if regexp is not None:
        bre_m = re.compile(regexp)

    # Get the messages.
    #
    # GET /api/v1/messages
    # {
    #   "messages": [
    #     {
    #       "uuid": "b660493e-364d-4839-8fb9-0eed79b9cfca",
    #       "content": "# My message\n\n* line 1\n* line 2",
    #       "severity": "warning",
    #       "media_type": "text/markdown"
    #     },
    #     {
    #       "uuid": "a93cd813-ca73-4b75-b7d8-6c3e3d7266e9",
    #       "content": "My text message",
    #       "severity": "info",
    #       "media_type": "text/plain"
    #     }
    #   ]
    # }
    messages = module.get_object_path("messages")

    # Search for the message to delete/create. To match messages, use
    # `search_string' or `regexp', or the provided text in `content' if none
    # of the two options are given.
    match_messages = []
    found = False
    for message in messages.get("messages", []):
        # Severiy does not match: move to the next message
        if search_severity and message.get("severity") != search_severity:
            continue
        message_content = message.get("content", "")
        if search_string is not None:
            if search_string in message_content:
                found = True
                match_messages.append(message)
            continue
        if regexp is not None:
            if bre_m.search(message_content):
                found = True
                match_messages.append(message)
            continue
        if content is not None:
            if content == message_content:
                found = True
                match_messages.append(message)
            continue
        # None of the `search_string', `regexp', or `content' parameters are
        # provided. If `search_severity' is, then all messages matching that
        # severity are selected.
        if search_severity:
            found = True
            match_messages.append(message)

    # Remove the matching messages
    if state == "absent":
        for message in match_messages:
            uuid = message.get("uuid", "")
            module.delete(
                True,
                "global message",
                uuid,
                "message/{uuid}",
                auto_exit=False,
                uuid=uuid,
            )
        module.exit_json(changed=found)

    # Prepare the data that gets set for update/create
    new_fields = {}
    if content is not None:
        new_fields["content"] = content
    if severity:
        new_fields["severity"] = severity
    if format:
        new_fields["media_type"] = "text/{format}".format(format=format)

    # Some existing messages match. Verify if there is a message that exactly
    # matches (same severity, media type, and content). If yes, then do
    # nothing. If no, then delete all the messages that match and then recreate
    # the message with the provided parameters.
    if found:
        for message in match_messages:
            for attr in new_fields:
                if new_fields[attr] != message.get(attr):
                    break
            else:
                # Exact match
                module.exit_json(changed=False)
        # The API does not allow updating a message. Therefore, delete all the
        # matching messages and recreate only one.
        for message in match_messages:
            uuid = message.get("uuid", "")
            module.delete(
                True,
                "global message",
                uuid,
                "message/{uuid}",
                auto_exit=False,
                uuid=uuid,
            )
        # Use the existing message fields as defaults. If several messages
        # matched, then use the last one in the list :(
        message.update(new_fields)
        new_fields = message
        new_fields.pop("uuid")

    if "content" not in new_fields:
        new_fields["content"] = ""
    if "severity" not in new_fields:
        new_fields["severity"] = "info"
    if "media_type" not in new_fields:
        new_fields["media_type"] = "text/plain"
    module.create(
        "global message",
        "",
        "messages",
        {"message": new_fields},
    )


if __name__ == "__main__":
    main()
