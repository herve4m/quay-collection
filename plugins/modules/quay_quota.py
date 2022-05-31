#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022 Herve Quatremain <rv4m@yahoo.co.uk>
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
module: quay_quota
short_description: Manage Red Hat Quay organizations quota
description:
  - Create, delete, and update storage quota for organizations.
version_added: '0.0.14'
author: Herve Quatremain (@herve4m)
options:
  organization:
    description:
      - Name of the organization. That organization must exist.
    required: true
    type: str
  quota:
    description:
      - Quota that Quay uses to compute the warning and reject limits for the
        organization.
      - You specify a quota in bytes, but you can also use the K[i]B, M[i]B,
        G[i]B, or T[i]B suffixes.
    required: false
    type: str
  warning_pct:
    description:
      - Warning (soft) limit as a percentage of the quota.
      - Quay notifies the users when the limit is reached.
      - Set I(warning_pct) to C(0) to remove the warning limit.
    required: false
    type: int
  reject_pct:
    description:
      - Reject (hard) limit as a percentage of the quota.
      - Quay terminates any image push in the organization when the limit is
        reached.
      - Set I(reject_pct) to C(0) to remove the reject limit.
    required: false
    type: int
  state:
    description:
      - If C(absent), then the module deletes the quota and limits for the
        given organization.
      - If C(present), then the module establishes the quota and limits for the
        given organization.
      - If quota and limits are already set, then the module updates them.
    type: str
    default: present
    choices: [absent, present]
notes:
  - The module requires Red Hat Quay 3.7 or later.
  - The module requires that your Quay administrator enables quota management
    for your installation (by setting C(FEATURE_QUOTA_MANAGEMENT) to C(True) in
    C(config.yaml)).
  - Supports C(check_mode).
  - The token that you provide in I(quay_token) must have the "Administer
    Organization" and "Administer User" permissions.
extends_documentation_fragment:
  - herve4m.quay.auth
  - herve4m.quay.auth.token
"""

EXAMPLES = r"""
- name: Ensure the organization has a 1.5 TiB quota with 80% and 95% limits
  herve4m.quay.quay_quota:
    organization: production
    quota: 1.5 TiB
    warning_pct: 80
    reject_pct: 95
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the production organization has no warning limit
  herve4m.quay.quay_quota:
    organization: production
    warning_pct: 0
    state: present
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

- name: Ensure the production organization has no quota
  herve4m.quay.quay_quota:
    organization: production
    state: absent
    quay_host: https://quay.example.com
    quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
"""

RETURN = r""" # """

from ..module_utils.api_module import APIModule


def main():
    argument_spec = dict(
        organization=dict(required=True),
        quota=dict(),
        warning_pct=dict(type="int"),
        reject_pct=dict(type="int"),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = APIModule(argument_spec=argument_spec, supports_check_mode=True)

    # Extract our parameters
    organization = module.params.get("organization")
    quota = module.params.get("quota")
    warning_pct = module.params.get("warning_pct")
    reject_pct = module.params.get("reject_pct")
    state = module.params.get("state")

    # Get the organization details from the given name.
    #
    # GET /api/v1/organization/{orgname}
    # {
    #   "name": "production",
    #   "email": "c402dbcb-31d4-46e2-a07b-d72dbebcbd3c",
    #   "avatar": {
    #     "name": "production",
    #     "hash": "9f26...4cca",
    #     "color": "#a55194",
    #     "kind": "user"
    #   },
    #   "is_admin": true,
    #   "is_member": true,
    #   "teams": {
    #     "owners": {
    #       "name": "owners",
    #       "description": "",
    #       "role": "admin",
    #       "avatar": {
    #         "name": "owners",
    #         "hash": "6f0e...8d90",
    #         "color": "#c7c7c7",
    #         "kind": "team"
    #       },
    #       "can_view": true,
    #       "repo_count": 0,
    #       "member_count": 1,
    #       "is_synced": false
    #     }
    #   },
    #   "ordered_teams": [
    #     "owners"
    #   ],
    #   "invoice_email": false,
    #   "invoice_email_address": null,
    #   "tag_expiration_s": 1209600,
    #   "is_free_account": true,
    #   "quotas": [
    #     {
    #       "id": 2,
    #       "limit_bytes": 200000000,
    #       "limits": [
    #         {
    #           "id": 1,
    #           "type": "Warning",
    #           "limit_percent": 80
    #         },
    #         {
    #           "id": 4,
    #           "type": "Reject",
    #           "limit_percent": 95
    #         }
    #       ]
    #     }
    #   ],
    #   "quota_report": {
    #     "quota_bytes": 0,
    #     "configured_quota": 200000000
    #   }
    # }
    org_details = module.get_organization(organization)
    if not org_details:
        if state == "absent":
            module.exit_json(changed=False)
        module.fail_json(
            msg="The {orgname} organization does not exist.".format(orgname=organization)
        )

    # Get the quota details
    quota_details = org_details["quotas"][0] if len(org_details.get("quotas", [])) else {}
    qid = str(quota_details.get("id", 0))

    # Remove the quota
    if state == "absent":
        module.delete(
            quota_details if quota_details else None,
            "quota",
            organization,
            "organization/{orgname}/quota/{qid}",
            orgname=organization,
            qid=qid,
        )

    updated = False

    # User gave `warning_pct' and `reject_pct' but did not set `quota' and no
    # quota exists yet for the organization.
    # Set the quota to 8 TB by default
    if (
        quota is None
        and not quota_details
        and (warning_pct is not None or reject_pct is not None)
    ):
        quota = "8000000 TB"

    # Convert the given quota in bytes
    if quota is not None:
        mult = 1
        q = quota.lower()
        if "tib" in q:
            q = q.replace("tib", "")
            mult = 1024 * 1024 * 1024 * 1024
        elif "tb" in q:
            q = q.replace("tb", "")
            mult = 1000 * 1000 * 1000 * 1000
        elif "gib" in q:
            q = q.replace("gib", "")
            mult = 1024 * 1024 * 1024
        elif "gb" in q:
            q = q.replace("gb", "")
            mult = 1000 * 1000 * 1000
        elif "mib" in q:
            q = q.replace("mib", "")
            mult = 1024 * 1024
        elif "mb" in q:
            q = q.replace("mb", "")
            mult = 1000 * 1000
        elif "kib" in q:
            q = q.replace("kib", "")
            mult = 1024
        elif "kb" in q:
            q = q.replace("kb", "")
            mult = 1000
        try:
            q = int(float(q.replace(" ", "")) * mult)
        except ValueError:
            module.fail_json(
                msg="Wrong format for the `quota' parameter: {quota} is not a float.".format(
                    quota=quota
                )
            )

        new_fields = {"limit_bytes": q}
        if quota_details:
            updated, _not_used = module.update(
                quota_details,
                "quota",
                organization,
                "organization/{orgname}/quota/{qid}",
                new_fields,
                auto_exit=False,
                orgname=organization,
                qid=qid,
            )
        else:
            module.create(
                "quota",
                organization,
                "organization/{orgname}/quota",
                new_fields,
                auto_exit=False,
                orgname=organization,
            )
            updated = True

            # Retrieve the new quota object
            obj = module.get_object_path("organization/{orgname}/quota", orgname=organization)
            try:
                quota_details = obj[0]
                qid = str(quota_details["id"])
            except (TypeError, IndexError):
                module.fail_json(
                    msg="Cannot retrieve the new quota for the {org} organization.".format(
                        org=organization
                    )
                )

    # Retrieve the current limits
    current_warning = None
    current_warning_id = None
    current_reject = None
    current_reject_id = None
    for limit in quota_details.get("limits", []):
        if limit.get("type") == "Warning":
            current_warning_id = str(limit.get("id"))
            current_warning = limit.get("limit_percent")
        if limit.get("type") == "Reject":
            current_reject_id = str(limit.get("id"))
            current_reject = limit.get("limit_percent")

    #
    # Warning limit
    #

    # Remove the limit when the given parameter is 0
    if warning_pct == 0:
        upd = module.delete(
            current_warning_id,
            "warning limit",
            organization,
            "organization/{orgname}/quota/{qid}/limit/{lid}",
            auto_exit=False,
            orgname=organization,
            qid=qid,
            lid=current_warning_id,
        )
        if upd:
            updated = True
    elif warning_pct and warning_pct != current_warning:
        # Create the new limit
        new_fields = {"type": "Warning", "threshold_percent": warning_pct}
        if current_warning_id is None:
            module.create(
                "warning limit",
                organization,
                "organization/{orgname}/quota/{qid}/limit",
                new_fields,
                auto_exit=False,
                orgname=organization,
                qid=qid,
            )
        else:
            module.unconditional_update(
                "warning limit",
                organization,
                "organization/{orgname}/quota/{qid}/limit/{lid}",
                new_fields,
                orgname=organization,
                qid=qid,
                lid=current_warning_id,
            )
        updated = True

    #
    # Reject limit
    #

    # Remove the limit when the given parameter is 0
    if reject_pct == 0:
        upd = module.delete(
            current_reject_id,
            "reject limit",
            organization,
            "organization/{orgname}/quota/{qid}/limit/{lid}",
            auto_exit=False,
            orgname=organization,
            qid=qid,
            lid=current_reject_id,
        )
        if upd:
            updated = True
    elif reject_pct and reject_pct != current_reject:
        # Create the new limit
        new_fields = {"type": "Reject", "threshold_percent": reject_pct}
        if current_reject_id is None:
            module.create(
                "reject limit",
                organization,
                "organization/{orgname}/quota/{qid}/limit",
                new_fields,
                auto_exit=False,
                orgname=organization,
                qid=qid,
            )
        else:
            module.unconditional_update(
                "reject limit",
                organization,
                "organization/{orgname}/quota/{qid}/limit/{lid}",
                new_fields,
                orgname=organization,
                qid=qid,
                lid=current_reject_id,
            )
        updated = True

    module.exit_json(changed=updated)


if __name__ == "__main__":
    main()
