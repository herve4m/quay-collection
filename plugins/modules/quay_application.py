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
module: quay_application
short_description: Manage Red Hat Quay organizations
description:
  - Create, delete, and update organizations in Red Hat Quay.
version_added: '0.0.1'
author: Herve Quatremain (@herve4m)
options:
  organization:
    description:
      - Name of the organization in which to manage the application.
    required: true
    type: str
  name:
    description:
      - Name of the application to create, update, or delete. Application
        names must be at least two characters long.
    required: true
    type: str
  new_name:
    description:
      - New name for the application.
      - Setting this option changes the name of the application which current
        name is provided in C(name).
    type: str
  description:
    description:
      - Description for the application.
    type: str
  application_uri:
    description:
      - URL to the application home page.
    type: str
  redirect_uri:
    description:
      - Prefix of the application's OAuth redirection/callback URLs.
    type: str
  avatar_email:
    description:
      - Email address that represents the avatar for the application.
    type: str
  state:
    description:
      - If C(absent), then the module deletes the application.
      - The module does not fail if the application does not exist because the
        state is already as expected.
      - If C(present), then the module creates the application if it does not
        already exist.
      - If the application already exists, then the module updates its state.
    type: str
    default: present
    choices: [absent, present]
notes:
  - Supports C(check_mode).
  - The token that you provide in C(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
extends_documentation_fragment: herve4m.quay.auth
"""

EXAMPLES = r"""
- name: Ensure the application extapp exists
  herve4m.quay.quay_application:
    organization: production
    name: extapp
    description: External application
    application_uri: http://applicationuri.example.com
    redirect_uri: http://redirecturi.example.com
    avatar_email: avatarextapp@example.com
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the application is renamed
  herve4m.quay.quay_application:
    organization: production
    name: extapp
    new_name: apiaccess
    description: Application dedicated to API access
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the application is removed
  herve4m.quay.quay_application:
    organization: production
    name: apiaccess
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        organization=dict(required=True),
        name=dict(required=True),
        new_name=dict(),
        description=dict(),
        application_uri=dict(),
        redirect_uri=dict(),
        avatar_email=dict(),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    organization = module.params.get("organization")
    name = module.params.get("name")
    new_name = module.params.get("new_name")
    description = module.params.get("description")
    application_uri = module.params.get("application_uri")
    redirect_uri = module.params.get("redirect_uri")
    avatar_email = module.params.get("avatar_email")
    state = module.params.get("state")

    # Verifying if the organization exists
    if not module.get_organization(organization):
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {orgname} organization does not exist.".format(orgname=organization)
        )

    # Getting the applications for the given organization
    #
    # GET /api/v1/organization/{orgname}/applications
    # {
    #   "applications": [
    #     {
    #       "name": "myapp1",
    #       "description": "",
    #       "application_uri": "",
    #       "client_id": "JCRTNN1H6HJSP174FAQE",
    #       "client_secret": "Z7VY5A6NOFR51BQ7MR0L7QDYOXKXAXAGU1VAS2QT",
    #       "redirect_uri": "",
    #       "avatar_email": null
    #     }
    #   ]
    # }
    application_list = module.get_object_path(
        "organization/{orgname}/applications", orgname=organization
    )

    # Looking for the applications
    app_details = None
    new_app_details = None
    for application in application_list.get("applications", []):
        application_name = application.get("name", "")
        if name == application_name:
            app_details = application
        elif new_name == application_name:
            new_app_details = application

    # The destination application already exists
    if app_details and new_app_details:
        module.fail_json(
            msg="The {app} application (`new_name') already exists.".format(app=new_name)
        )

    # Remove the application
    if state == "absent":
        if new_app_details:
            module.delete(
                new_app_details,
                "application",
                new_name,
                "organization/{orgname}/applications/{id}",
                orgname=organization,
                id=new_app_details.get("client_id", ""),
            )
        else:
            module.delete(
                app_details,
                "application",
                name,
                "organization/{orgname}/applications/{id}",
                orgname=organization,
                id=app_details.get("client_id", "") if app_details else "",
            )

    # Prepare the data that gets set for update or create
    new_fields = {}
    if description is not None:
        new_fields["description"] = description

    if application_uri is not None:
        new_fields["application_uri"] = application_uri
    elif new_app_details:
        new_fields["application_uri"] = new_app_details.get("application_uri", "")
    elif app_details:
        new_fields["application_uri"] = app_details.get("application_uri", "")

    if redirect_uri is not None:
        new_fields["redirect_uri"] = redirect_uri
    elif new_app_details:
        new_fields["redirect_uri"] = new_app_details.get("redirect_uri", "")
    elif app_details:
        new_fields["redirect_uri"] = app_details.get("redirect_uri", "")

    if avatar_email is not None:
        new_fields["avatar_email"] = avatar_email
    elif new_app_details:
        new_fields["avatar_email"] = new_app_details.get("avatar_email", "")
    elif app_details:
        new_fields["avatar_email"] = app_details.get("avatar_email", "")

    # Renaming the application
    if new_name:
        new_fields["name"] = new_name
        # The original application does not exists...
        if not app_details:
            # and neither the new organization. Create that new organization.
            if not new_app_details:
                module.create(
                    "application",
                    new_name,
                    "organization/{orgname}/applications",
                    new_fields,
                    orgname=organization,
                )

            # The original organization does not exists but the new one does.
            # Update that new organization.
            module.update(
                new_app_details,
                "application",
                new_name,
                "organization/{orgname}/applications/{id}",
                new_fields,
                orgname=organization,
                id=new_app_details.get("client_id", ""),
            )
        # The original organization exists. Rename it.
        module.update(
            app_details,
            "application",
            new_name,
            "organization/{orgname}/applications/{id}",
            new_fields,
            orgname=organization,
            id=app_details.get("client_id", ""),
        )

    new_fields["name"] = name

    if app_details:
        module.update(
            app_details,
            "application",
            name,
            "organization/{orgname}/applications/{id}",
            new_fields,
            orgname=organization,
            id=app_details.get("client_id", ""),
        )

    module.create(
        "application",
        name,
        "organization/{orgname}/applications",
        new_fields,
        orgname=organization,
    )


if __name__ == "__main__":
    main()
