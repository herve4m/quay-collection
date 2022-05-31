herve4m.quay.quay_org
=========

This role creates an organization in Red Hat Quay.
In addition, it can creates user accounts, robot accounts, teams, default permissions, applications, and repositories for that organization.


Requirements
------------

The role accesses Red Hat Quay through its REST API.
To use the API, Red Hat Quay requires an OAuth access token.

Before using the role, you must generate that access token.
In addition, the user account associated with the access token must have superuser permissions.

To do so, follow those steps:

1. Log in to the Red Hat Quay web UI with a user account that has superuser permissions.
2. Use an existing organization or create a new one.
3. In the organization, create an application.
4. In the application, select the `Generate Token` menu.
5. Select the permissions to associate to the token.
   To be able to use all the role in the collection, select `Administer Organization`, `Administer Repositories`, `Create Repositories`, `Super User Access`, and `Administer User`.
6. Click `Generate Token`.
7. Copy and then paste the token string into the `quay_token` role variable.


Role Variables
--------------

You can access the documentation of all the role variables by running the `ansible-doc -t role herve4m.quay.quay_org` command.

The following list gives a short descriptions of the variables:

* `quay_host`: URL for access the Red Hat Quay API.
* `quay_token`: OAuth access token for authenticating with the API.
* `quay_validate_certs`: Whether to allow insecure connections to the API.
* `quay_org_name`: Name of the organization to create.
* `quay_org_email`: Email address to associate with the organization.
* `quay_org_users`: List of user accounts to create.
* `quay_org_robots`: List of robot accounts to create in the organization.
* `quay_org_teams`: List of the teams to create in the organization.
* `quay_org_default_perms`: List of the default permissions to assign to repositories when they are created.
* `quay_org_applications`: List of the OAuth applications to create in the organization.
* `quay_org_repositories`: List of the repositories to create in the organization.
* `quay_org_quota`: Quota that Quay uses to compute the warning and reject limits for the organization.
  You specify a quota in bytes, but you can also use the K[i]B, M[i]B, G[i]B, or T[i]B suffixes.
* `quay_org_warning_pct`: Warning (soft) limit as a percentage of the quota.
* `quay_org_reject_pct`: Reject (hard) limit as a percentage of the quota.


Example Playbook
----------------

```yaml
---
- name: Creating a production organization
  hosts: localhost
  become: false
  gather_facts: false

  tasks:
    - name: Ensure the organization exists
      include_role:
        name: herve4m.quay.quay_org
      vars:
        # Connection parameters
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
        quay_validate_certs: true
        # Organization name and email
        quay_org_name: production
        quay_org_email: production@example.com
        # Quota
        quay_org_quota: 1.5 TiB
        quay_org_warning_pct: 90
        quay_org_reject_pct: 97
        # User accounts to create
        quay_org_users:
          - username: lvasquez
            email: lvasquez@example.com
            password: vs9mrD55NP
          - username: dwilde
            email: dwilde@example.com
        # Robot accounts to create in the organization
        quay_org_robots:
          - name: robotprod
        # Teams to create and configure
        quay_org_teams:
          - name: qa
            role: member
            members:
              - lvasquez
          - name: ops
            description: Operators
            role: creator
            members:
              - dwilde
              - production+robotprod
        # Permissions to apply to new repositories in the organization
        quay_org_default_perms:
          - name: ops
            type: team
            role: write
          - name: lvasquez
            type: user
            role: read
        # OAuth applications
        quay_org_applications:
          - name: oauth_app
        # Repositories to create in the organization
        quay_org_repositories:
          - name: small_image
            visibility: private
            perms:
              - name: qa
                type: team
                role: read
...
```

The `tests/` directory provides an additional example.


License
-------

GPL 3.0 or later.


Author Information
------------------

This role was created in 2022 by Hervé Quatremain <rv4m@yahoo.co.uk>
