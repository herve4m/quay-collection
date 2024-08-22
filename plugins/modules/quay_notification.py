#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, 2022, 2024 Hervé Quatremain <herve.quatremain@redhat.com>
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
module: quay_notification
short_description: Manage Quay Container Registry repository notifications
description:
  - Create and delete repository notifications.
version_added: '0.0.1'
author: Hervé Quatremain (@herve4m)
options:
  repository:
    description:
      - Name of the repository which contains the notifications to manage. The
        format for the name is C(namespace)/C(shortname). The namespace can be
        an organization or a personal namespace.
      - If you omit the namespace part in the name, then the module looks for
        the repository in your personal namespace.
    required: true
    type: str
  title:
    description:
      - Notification title.
    type: str
  event:
    description:
      - Event that triggers the notification.
      - Depending of the activated Quay components, not all events might be
        available on your system.
    type: str
    choices:
      - repo_push
      - build_failure
      - build_queued
      - build_start
      - build_success
      - build_cancelled
      - vulnerability_found
      - repo_mirror_sync_started
      - repo_mirror_sync_success
      - repo_mirror_sync_failed
      - repo_image_expiry
  method:
    description:
      - Notification method. Each method requires a specific set of options
        that you define by using the I(config) parameter.
      - The email notification method is only available on Quay installations
        where the mailing capability has been activated (C(FEATURE_MAILING) to
        C(true) in C(config.yaml)).
    type: str
    choices:
      - email
      - flowdock
      - hipchat
      - quay_notification
      - slack
      - webhook
  config:
    description:
      - Configuration parameters for the notification method.
    type: dict
    suboptions:
      type:
        description:
          - Specifies the type of the account defined in I(name).
          - Only applies to the Quay Notification method.
        type: str
        choices: [user, team, org]
        default: user
      name:
        description:
          - Name of the account, team, or organization. Robot accounts are not
            allowed.
          - Required by the Quay Notification method.
        type: str
      email:
        description:
          - Destination email address.
          - Required by the email notification method.
        type: str
      url:
        description:
          - Webhook URL for the Slack method or POST URL for the webhook POST
            method.
        type: str
      template:
        description:
          - JSON data for the body content of the webhook POST method.
        type: str
      room_id:
        description:
          - Chat room ID required for the HipChat notification method.
        type: str
      notification_token:
        description:
          - Notification token required for the HipChat notification method.
        type: str
      flow_api_token:
        description:
          - API token required for the Flowdock notification method.
        type: str
  vulnerability_level:
    description:
      - Only used when I(event) is C(vulnerability_found).
      - The notification is triggered when the vulnerability has a level equal
        or higher to the level you define is I(vulnerability_level).
    type: str
    choices:
      - critical
      - high
      - medium
      - low
      - negligible
      - unknown
  image_expiry_days:
    description:
      - Only used when I(event) is C(repo_image_expiry).
      - The notification is triggered when the image expires in the specified
        number of days.
    type: int
    default: 7
  regexp:
    description:
      - The regular expression to search in the title of the existing
        notifications. This does not have to match the entire title.
      - The module uses that regular expression to select the notifications to
        process.
      - For C(state=present), the module resets the failure counter (if
        I(reset_failcount) is C(true)) or initiates a test (if I(test) is
        C(true)) of all the matching notifications.
      - For C(state=absent), the module deletes all the notifications that
        match.
      - Uses Python regular expressions. See
        U(https://docs.python.org/3/library/re.html).
      - Mutually exclusive with I(search_string).
    type: str
    aliases: [regex]
  search_string:
    description:
      - The literal string to search in the title of the existing
        notifications. This does not have to match the entire line.
      - For C(state=present), the module resets the failure counter (if
        I(reset_failcount) is C(true)) or initiates a test (if I(test) is
        C(true)) of all the matching notifications.
      - For C(state=absent), the module deletes all the notifications that
        match.
      - Mutually exclusive with I(regexp).
    type: str
  reset_failcount:
    description:
      - Reset the notification failure counter.
    type: bool
    default: false
  test:
    description:
      - Initiate a test of the notification.
    type: bool
    default: false
  state:
    description:
      - If C(absent), then the module deletes the notification.
      - The module uses the I(title), I(regex), or I(search_string) parameters
        to select the notifications to process. You can also omit those
        parameters and use instead the I(event) and I(method) options to select
        all the notifications triggered by a specific event or using a specific
        method.
      - If C(present), then the module creates the notification if it does not
        already exist.
      - If the notification already exists and I(reset_failcount) or I(test)
        are set, then the module resets the failure counter or initiates a test
        of the notification.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - Your Quay administrator must enable the image garbage collection capability
    of your Quay installation (C(FEATURE_GARBAGE_COLLECTION) in C(config.yaml))
    to use the C(repo_image_expiry) event.
  - Using the C(repo_image_expiry) event and the I(image_expiry_days) parameter
    requires Quay version 3.12 or later.
  - The user account associated with the token that you provide in
    I(quay_token) must have administrator access to the repository.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.login
"""

EXAMPLES = r"""
- name: Ensure notification of type Quay Notification exists
  herve4m.quay.quay_notification:
    repository: production/smallimage
    title: Test Quay Notification on image push
    event: repo_push
    method: quay_notification
    config:
      name: operators
      type: team
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

# You must enable the security scanner capability of your Quay installation
# to use the vulnerability_found event.
- name: Ensure notification of type webhook exists
  herve4m.quay.quay_notification:
    repository: production/smallimage
    title: Webhook notification on critical image vulnerability
    event: vulnerability_found
    vulnerability_level: critical
    method: webhook
    config:
      url: https://webhook.example.com/webhook/12345
      template: "{{ lookup('file', 'post.json') | string }}"
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

# You must enable the image garbage collection capability of your Quay
# installation (3.12 or later) to use the repo_image_expiry event.
- name: Ensure notification exists for when an image is going to expire
  herve4m.quay.quay_notification:
    repository: production/smallimage
    title: Webhook notification 10 days before an image expires
    event: repo_image_expiry
    image_expiry_days: 10
    method: webhook
    config:
      url: https://webhook.example.com/webhook/12345
      template: "{{ lookup('file', 'post.json') | string }}"
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure notification of type Slack exists
  herve4m.quay.quay_notification:
    repository: production/smallimage
    title: Notify image push to Slack
    event: repo_push
    method: slack
    config:
      url: https://hooks.slack.com/services/XXX/YYY/ZZZ
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Test Slack notification
  herve4m.quay.quay_notification:
    repository: production/smallimage
    title: Notify image push to Slack
    test: true
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Reset the failure counter for the Quay Notification
  herve4m.quay.quay_notification:
    repository: production/smallimage
    regex: "Quay\\s+Notification\\s"
    reset_failcount: true
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Delete all the notifications triggered by canceled builds
  herve4m.quay.quay_notification:
    repository: production/smallimage
    event: build_cancelled
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Delete all the notifications where the title includes "Test"
  herve4m.quay.quay_notification:
    repository: production/smallimage
    search_string: Test
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

import re

from ..module_utils.api_module import APIModule


def main():
    # Ordered list of the vulnerability levels. This list is also used to map
    # each level name to its ID. The ID is the index the level in the list.
    # The ID is used in the POST request.
    vulnerability_level_names = [
        "critical",
        "high",
        "medium",
        "low",
        "negligible",
        "unknown",
    ]

    argument_spec = dict(
        repository=dict(required=True),
        title=dict(),
        event=dict(
            choices=[
                "repo_push",
                "build_failure",
                "build_queued",
                "build_start",
                "build_success",
                "build_cancelled",
                "vulnerability_found",
                "repo_mirror_sync_started",
                "repo_mirror_sync_success",
                "repo_mirror_sync_failed",
                "repo_image_expiry",
            ]
        ),
        method=dict(
            choices=[
                "email",
                "flowdock",
                "hipchat",
                "quay_notification",
                "slack",
                "webhook",
            ]
        ),
        vulnerability_level=dict(choices=vulnerability_level_names),
        image_expiry_days=dict(type="int", default=7),
        config=dict(
            type="dict",
            options=dict(
                # Quay notification
                name=dict(),
                type=dict(choices=["user", "team", "org"], default="user"),
                # E-Mail notification
                email=dict(),
                # Slack and webhook notification
                url=dict(),
                # webhook notification
                template=dict(),
                # HipChat notification
                room_id=dict(),
                notification_token=dict(no_log=True),
                # Flowdock notification
                flow_api_token=dict(no_log=True),
            ),
            required_together=[("room_id", "notification_token")],
            mutually_exclusive=[
                ("name", "email"),
                ("name", "url"),
                ("name", "template"),
                ("name", "room_id"),
                ("name", "notification_token"),
                ("name", "flow_api_token"),
                ("email", "url"),
                ("email", "template"),
                ("email", "room_id"),
                ("email", "notification_token"),
                ("email", "flow_api_token"),
                ("url", "room_id"),
                ("url", "notification_token"),
                ("url", "flow_api_token"),
                ("room_id", "flow_api_token"),
                ("room_id", "template"),
                ("flow_api_token", "template"),
            ],
        ),
        regexp=dict(aliases=["regex"]),
        search_string=dict(),
        test=dict(type="bool", default=False),
        reset_failcount=dict(type="bool", default=False),
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
    repository = module.params.get("repository").strip("/")
    title = module.params.get("title")
    event = module.params.get("event")
    method = module.params.get("method")
    config = module.params.get("config")
    regexp = module.params.get("regexp")
    search_string = module.params.get("search_string")
    test = module.params.get("test")
    reset_failcount = module.params.get("reset_failcount")
    state = module.params.get("state")
    vulnerability_level = module.params.get("vulnerability_level")
    image_expiry_days = module.params.get("image_expiry_days")

    # Extract namespace and repository from the repository parameter
    my_name = module.who_am_i()
    try:
        namespace, repo_shortname = repository.split("/", 1)
    except ValueError:
        # No namespace part in the repository name. Therefore, the repository
        # is in the user's personal namespace
        if my_name:
            namespace = my_name
            repo_shortname = repository
        else:
            module.fail_json(
                msg=(
                    "The `repository' parameter must include the"
                    " organization: <organization>/{name}."
                ).format(name=repository)
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

    # Get the repository notifications
    #
    # GET /api/v1/repository/{namespace}/{repository}/notification/
    # {
    #   "notifications": [
    #     {
    #       "uuid": "71a560b6-fd35-4ebb-a472-8e7acdba05b4",
    #       "title": "Send notification on push to team1",
    #       "event": "repo_push",
    #       "method": "quay_notification",
    #       "config": {
    #         "target": {
    #           "name": "team1",
    #           "kind": "team",
    #           "is_robot": false,
    #           "avatar": {
    #             "name": "team1",
    #             "hash": "5760...397e",
    #             "color": "#9c9ede",
    #             "kind": "team"
    #           },
    #           "is_org_member": true
    #         }
    #       },
    #       "event_config": {},
    #       "number_of_failures": 0
    #     },
    #     {
    #       "uuid": "6c07bb76-3026-45e8-b65c-f68720b27845",
    #       "title": "Send notification on push to Slack",
    #       "event": "repo_push",
    #       "method": "slack",
    #       "config": {
    #         "url": "https://hooks.slack.com/services/XXX/YYY/ZZZ"
    #       },
    #       "event_config": {},
    #       "number_of_failures": 0
    #     },
    #     {
    #       "uuid": "d5e8976c-0ac1-4792-be9e-58d4261b2cf8",
    #       "title": "Send notification on push to Slack 2",
    #       "event": "repo_image_expiry",
    #       "method": "slack",
    #       "config": {
    #         "url": "https://hooks.slack.com/services/AAA/BBB/CCC"
    #       },
    #       "event_config": {
    #         "days": 10
    #       },
    #       "number_of_failures": 0
    #     }
    #   ]
    # }
    notifications = module.get_object_path(
        "repository/{full_repo_name}/notification/",
        full_repo_name=full_repo_name,
    )

    # Search for the notifications to process.
    # To match notifications, use `search_string' or `regexp', or the provided
    # text in `title' if none of the two options are given.
    # If none of those options are given, then use the `event' and `method'
    # parameters to find a match
    if regexp is not None:
        bre_m = re.compile(regexp)

    match_notifications = []
    found = False
    for notification in notifications.get("notifications", []):
        notification_title = notification.get("title", "")
        if search_string is not None:
            if search_string in notification_title:
                found = True
                match_notifications.append(notification)
            continue
        if regexp is not None:
            if bre_m.search(notification_title):
                found = True
                match_notifications.append(notification)
            continue
        if title is not None:
            if title == notification_title:
                found = True
                match_notifications.append(notification)
            continue
        # None of the `search_string', `regexp', or `title' parameters are
        # provided. If `event' or `method' are, then all notifications matching
        # those parameters are selected.
        if event and notification.get("event") != event:
            continue
        if method and notification.get("method") != method:
            continue
        if event or method:
            found = True
            match_notifications.append(notification)

    # Remove the matching notifications
    if state == "absent":
        for notification in match_notifications:
            uuid = notification.get("uuid", "")
            module.delete(
                True,
                "notification",
                uuid,
                "repository/{full_repo_name}/notification/{uuid}",
                auto_exit=False,
                full_repo_name=full_repo_name,
                uuid=uuid,
            )
        module.exit_json(changed=found)

    changed = False

    # Create a notification
    if not match_notifications:
        # Verify that the repository exists
        repo_details = module.get_object_path(
            "repository/{full_repo_name}",
            full_repo_name=full_repo_name,
        )
        if not repo_details:
            module.fail_json(
                msg="The {repo} repository does not exist.".format(repo=full_repo_name)
            )

        # Gather and verify the parameters
        new_fields = {"eventConfig": {}, "event_config": {}, "config": {}}
        missing_parameters = []
        if title:
            new_fields["title"] = title
        else:
            missing_parameters.append("title")
        if event:
            new_fields["event"] = event
        else:
            missing_parameters.append("event")
        if method:
            new_fields["method"] = method
        else:
            missing_parameters.append("method")
        if not config:
            missing_parameters.append("config")
        if missing_parameters:
            module.fail_json(
                msg="Some required parameters are not provided: {params}".format(
                    params=", ".join(missing_parameters)
                )
            )

        if method == "email":
            email = config.get("email")
            if email:
                new_fields["config"]["email"] = email
            else:
                module.fail_json(
                    msg=(
                        "The email notification method requires the"
                        " `email' configuration option."
                    )
                )
        elif method == "flowdock":
            flow_api_token = config.get("flow_api_token")
            if flow_api_token:
                new_fields["config"]["flow_api_token"] = flow_api_token
            else:
                module.fail_json(
                    msg=(
                        "The Flowdock notification method requires the"
                        " `flow_api_token' configuration option."
                    )
                )
        elif method == "hipchat":
            room_id = config.get("room_id")
            if room_id:
                new_fields["config"]["room_id"] = room_id
            else:
                module.fail_json(
                    msg=(
                        "The HipChat notification method requires the"
                        " `room_id' and `notification_token' configuration options."
                    )
                )
            notification_token = config.get("notification_token")
            if notification_token:
                new_fields["config"]["notification_token"] = notification_token
            else:
                module.fail_json(
                    msg=(
                        "The HipChat notification method requires the"
                        " `room_id' and `notification_token' configuration options."
                    )
                )
        elif method == "slack":
            url = config.get("url")
            if url:
                new_fields["config"]["url"] = url
            else:
                module.fail_json(
                    msg=(
                        "The Slack notification method requires the"
                        " `url' configuration option."
                    )
                )
        elif method == "webhook":
            url = config.get("url")
            if url:
                new_fields["config"]["url"] = url
            else:
                module.fail_json(
                    msg=(
                        "The webhook POST notification method requires the"
                        " `url' configuration option."
                    )
                )
            template = config.get("template")
            if template:
                new_fields["config"]["template"] = template
        elif method == "quay_notification":
            name = config.get("name")
            if not name:
                module.fail_json(
                    msg=(
                        "The Quay notification method requires the"
                        " `name' configuration option."
                    )
                )
            kind = config.get("type")
            new_fields["config"]["target"] = {"name": name, "kind": kind}
            if kind == "user":
                user_details = module.get_account(name)
                if not user_details:
                    module.fail_json(
                        msg=(
                            "The {user} user account in the"
                            " `name' parameter does not exist."
                        ).format(user=name)
                    )
                if user_details.get("is_robot"):
                    module.fail_json(
                        msg=(
                            "{user} in the `name' parameter is a robot account."
                            " You cannot use robot accounts for notifications."
                        ).format(user=name)
                    )
            if kind == "team" and not module.get_team(namespace, name):
                module.fail_json(
                    msg=(
                        "The {team} team in the `name' parameter does not"
                        " exist in the {orgname} organization."
                    ).format(team=name, orgname=namespace)
                )
            if kind == "org" and not module.get_organization(name):
                module.fail_json(
                    msg=(
                        "The {orgname} organization in the `name' parameter"
                        " does not exist."
                    ).format(orgname=name)
                )

        if event == "vulnerability_found" and vulnerability_level is not None:
            new_fields["eventConfig"]["level"] = new_fields["event_config"]["level"] = str(
                vulnerability_level_names.index(vulnerability_level)
            )
        elif event == "repo_image_expiry":
            new_fields["eventConfig"]["days"] = new_fields["event_config"]["days"] = int(
                image_expiry_days
            )

        match_notifications.append(
            module.create(
                "notification",
                title,
                "repository/{full_repo_name}/notification/",
                new_fields,
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
        )
        changed = True

    # Existing notifications: test and reset
    if match_notifications:
        if test:
            for notification in match_notifications:
                uuid = notification.get("uuid", "")
                module.create(
                    "notification",
                    uuid,
                    "repository/{full_repo_name}/notification/{uuid}/test",
                    {},
                    auto_exit=False,
                    full_repo_name=full_repo_name,
                    uuid=uuid,
                )

        if reset_failcount:
            for notification in match_notifications:
                if notification.get("number_of_failures", 0):
                    uuid = notification.get("uuid", "")
                    module.create(
                        "notification",
                        uuid,
                        "repository/{full_repo_name}/notification/{uuid}",
                        {},
                        auto_exit=False,
                        full_repo_name=full_repo_name,
                        uuid=uuid,
                    )
                    changed = True

    module.exit_json(changed=changed)


if __name__ == "__main__":
    main()
