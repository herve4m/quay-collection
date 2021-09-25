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
module: quay_repository
short_description: Manage Red Hat Quay repositories
description:
  - Create, delete, and update repositories in Red Hat Quay.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  name:
    description:
      - Name of the repository to create, remove, or modify.
      - The name must be in lowercase and must not contain white spaces.
    required: true
    type: str
  namespace:
    description:
      - Name of the organization or the user account that owns the repository.
      - Quay organizes repositories in namespaces. A namespace can use the name
        of an organization or the name of a user account.
      - The full repository name is C(namespace)/C(name).
      - You must be the owner of the user account to manage its repositories
        (the token you use in C(quay_token) must belong to that user).
    required: true
    type: str
  visibility:
    description:
      - If C(public), then anyone can pull images from the repository.
      - If C(private), then nobody can access the repository and you need to
        explicitly grant access to users and teams.
    type: str
    choices: [public, private]
  description:
    description:
      - Text in Markdown format that describes the repository.
    type: str
  perms:
    description:
      - User and team permissions to associate with the repository.
    type: list
    elements: dict
    suboptions:
      type:
        description:
          - Specifies if the permission is granted for a user or a team.
        type: str
        choices: [user, team]
        default: user
      name:
        description:
          - Name of the user account or the team.
        type: str
      role:
        description:
          - Type of permission to grant to the user or the team.
        type: str
        choices: [read, write, admin]
        default: read
  append:
    description:
      - If C(yes), then add the permission defined in C(perms) to the
        repository.
      - If C(no), then the module sets the permissions specified in C(perms),
        removing all others permissions from the repository.
    type: bool
    default: yes
  state:
    description:
      - If C(absent), then the module deletes the repository.
      - The module does not fail if the repository does not exist because the
        state is already as expected.
      - If C(present), then the module creates the repository if it does not
        already exist.
      - If the repository already exists, then the module updates its state.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in C(quay_token) must have the "Administer
    Repositories" and "Create Repositories" permissions.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure repository smallimage exists in the production organization
  herve4m.quay.quay_repository:
    # Full repository name: production/smallimage
    name: smallimage
    namespace: production
    visibility: private
    description: |
      # My first repository

      * smallimage is a small GNU/linux container image
      * Use podman to start a container using that image
    perms:
      - name: operators
        type: team
        role: read
      - name: lvasquez
        type: user
        role: read
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure repository bigimage exists in my (lvasquez) namespace
  herve4m.quay.quay_repository:
    # Full repository name: lvasquez/bigimage
    name: bigimage
    namespace: lvasquez
    visibility: public
    perms:
      - name: dwilde
        type: user
        role: write
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure repository development/testimg does not exist
  herve4m.quay.quay_repository:
    name: testimg
    namespace: development
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure repository has the exact set of permissions
  herve4m.quay.quay_repository:
    name: smallimage
    namespace: production
    perms:
      - name: operators
        type: team
        role: admin
      - name: managers
        type: team
        role: read
      - name: developers
        type: team
        role: read
    append: false
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        name=dict(required=True),
        namespace=dict(required=True),
        visibility=dict(choices=["public", "private"]),
        description=dict(),
        perms=dict(
            type="list",
            elements="dict",
            options=dict(
                type=dict(choices=["user", "team"], default="user"),
                name=dict(required=True),
                role=dict(choices=["read", "write", "admin"], default="read"),
            ),
        ),
        append=dict(type="bool", default=True),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    name = module.params.get("name")
    namespace = module.params.get("namespace")
    visibility = module.params.get("visibility")
    description = module.params.get("description")
    perms = module.params.get("perms")
    append = module.params.get("append")
    state = module.params.get("state")

    full_repo_name = "{namespace}/{repository}".format(namespace=namespace, repository=name)

    # Get the repository details
    #
    # GET /api/v1/repository/{namespace}/{repository}
    # {
    #   "namespace": "production",
    #   "name": "busybox",
    #   "kind": "image",
    #   "description": "Busybox images",
    #   "is_public": true,
    #   "is_organization": true,
    #   "is_starred": false,
    #   "status_token": "",
    #   "trust_enabled": false,
    #   "tag_expiration_s": 86400,
    #   "is_free_account": true,
    #   "state": "NORMAL",
    #   "tags": {},
    #   "can_write": true,
    #   "can_admin": true
    # }
    repo_details = module.get_object_path(
        "repository/{full_repo_name}", full_repo_name=full_repo_name
    )

    # Remove the repository
    if state == "absent":
        module.delete(
            repo_details,
            "repository",
            full_repo_name,
            "repository/{full_repo_name}",
            full_repo_name=full_repo_name,
        )

    # Check whether namespace exists (organization or user account).
    #
    # GET /api/v1/organization/{orgname}
    # GET /api/v1/users/{username}
    if not module.get_object_path(
        "organization/{orgname}", orgname=namespace
    ) and not module.get_object_path("users/{username}", username=namespace):
        module.fail_json(
            msg="The {namespace} namespace does not exist.".format(namespace=namespace)
        )

    changed = False
    if not repo_details:
        # Create the repository
        new_fields = {"namespace": namespace, "repository": name, "repo_kind": "image"}
        new_fields["description"] = description if description else ""
        new_fields["visibility"] = visibility if visibility else "private"
        module.create("repository", full_repo_name, "repository", new_fields, auto_exit=False)
        changed = True
    else:
        # Update description
        if description is not None and module.update(
            repo_details,
            "repository",
            full_repo_name,
            "repository/{full_repo_name}",
            {"description": description},
            auto_exit=False,
            full_repo_name=full_repo_name,
        ):
            changed = True
        # Update visibility
        if (
            visibility
            and "is_public" in repo_details
            and (
                repo_details["is_public"]
                and visibility == "private"
                or not repo_details["is_public"]
                and visibility == "public"
            )
        ):
            module.create(
                "repository",
                full_repo_name,
                "repository/{full_repo_name}/changevisibility",
                {"visibility": visibility},
                auto_exit=False,
                full_repo_name=full_repo_name,
            )
            changed = True

    # No permission to change. Exit
    if perms is None:
        module.exit_json(changed=changed)

    # Get the team permissions
    #
    # GET /api/v1/repository/{namespace}/{repository}/permissions/team/
    # {
    #   "permissions": {
    #     "developers": {
    #       "role": "write",
    #       "name": "developers",
    #       "avatar": {
    #         "name": "developers",
    #         "hash": "5760...397e",
    #         "color": "#9c9ede",
    #         "kind": "team"
    #       }
    #     }
    #   }
    # }
    team_perms = module.get_object_path(
        "repository/{full_repo_name}/permissions/team/", full_repo_name=full_repo_name
    )

    # Set of (<team>, <perm>) tuples
    current_team_perms = set(
        [(p["name"], p["role"]) for _, p in team_perms.get("permissions", {}).items()]
    )
    new_team_perms = set(
        [(p["name"], p["role"]) for p in perms if p.get("type", "user") == "team"]
    )

    to_add = new_team_perms - current_team_perms
    if append:
        to_delete = set()
    else:
        to_delete = current_team_perms - new_team_perms

    for perm in to_delete:
        module.delete(
            True,
            "team repository permission",
            perm[0],
            "repository/{full_repo_name}/permissions/team/{team}",
            auto_exit=False,
            full_repo_name=full_repo_name,
            team=perm[0],
        )
        changed = True

    for perm in to_add:
        module.unconditional_update(
            "team repository permission",
            perm[0],
            "repository/{full_repo_name}/permissions/team/{team}",
            {"role": perm[1]},
            full_repo_name=full_repo_name,
            team=perm[0],
        )
        changed = True

    # Get the user permissions
    #
    # GET /api/v1/repository/{namespace}/{repository}/permissions/user/
    # {
    #   "permissions": {
    #     "admin": {
    #       "role": "admin",
    #       "name": "admin",
    #       "is_robot": false,
    #       "avatar": {
    #         "name": "admin",
    #         "hash": "258d...da4f",
    #         "color": "#98df8a",
    #         "kind": "user"
    #       },
    #       "is_org_member": true
    #     },
    #     "operator2": {
    #       "role": "write",
    #       "name": "operator2",
    #       "is_robot": false,
    #       "avatar": {
    #         "name": "operator2",
    #         "hash": "4eaf...94b0",
    #         "color": "#7f7f7f",
    #         "kind": "user"
    #       },
    #       "is_org_member": false
    #     }
    #   }
    # }
    user_perms = module.get_object_path(
        "repository/{full_repo_name}/permissions/user/", full_repo_name=full_repo_name
    )

    # Set of (<user>, <perm>) tuples
    current_user_perms = set(
        [(p["name"], p["role"]) for _, p in user_perms.get("permissions", {}).items()]
    )
    new_user_perms = set(
        [(p["name"], p["role"]) for p in perms if p.get("type", "user") == "user"]
    )

    to_add = new_user_perms - current_user_perms
    if append:
        to_delete = set()
    else:
        to_delete = current_user_perms - new_user_perms

    for perm in to_delete:
        module.delete(
            True,
            "user repository permission",
            perm[0],
            "repository/{full_repo_name}/permissions/user/{user}",
            auto_exit=False,
            full_repo_name=full_repo_name,
            user=perm[0],
        )
        changed = True

    for perm in to_add:
        module.unconditional_update(
            "user repository permission",
            perm[0],
            "repository/{full_repo_name}/permissions/user/{user}",
            {"role": perm[1]},
            full_repo_name=full_repo_name,
            user=perm[0],
        )
        changed = True

    module.exit_json(changed=changed)


if __name__ == "__main__":
    main()
