# Quay Container Registry Collection for Ansible

[![Code Linting](https://github.com/herve4m/quay-collection/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/herve4m/quay-collection/actions/workflows/pre-commit.yml)
[![Sanity Test](https://github.com/herve4m/quay-collection/actions/workflows/ansible-sanity.yml/badge.svg)](https://github.com/herve4m/quay-collection/actions/workflows/ansible-sanity.yml)
[![Integration Test](https://github.com/herve4m/quay-collection/actions/workflows/ansible-integration.yml/badge.svg)](https://github.com/herve4m/quay-collection/actions/workflows/ansible-integration.yml)


The collection provides modules for managing your Quay Container Registry deployment.

## Included Content

The modules have been tested against versions 3.10, 3.11, and 3.12 of Quay Container Registry.

### Modules
Name | Description
---: | :---
[quay_api_token](https://github.com/herve4m/quay-collection/blob/main/docs/quay_api_token_module.rst) |  Create OAuth access tokens for accessing the Quay Container Registry API
[quay_application](https://github.com/herve4m/quay-collection/blob/main/docs/quay_application_module.rst) |  Manage Quay Container Registry applications
[quay_default_perm](https://github.com/herve4m/quay-collection/blob/main/docs/quay_default_perm_module.rst) |  Manage Quay Container Registry default repository permissions
[quay_docker_token](https://github.com/herve4m/quay-collection/blob/main/docs/quay_docker_token_module.rst) |  Manage tokens for accessing Quay Container Registry repositories
[quay_first_user](https://github.com/herve4m/quay-collection/blob/main/docs/quay_first_user_module.rst) |  Create the first user account
[quay_layer_info](https://github.com/herve4m/quay-collection/blob/main/docs/quay_layer_info_module.rst) |  Gather information about image layers in Quay Container Registry
[quay_manifest_label](https://github.com/herve4m/quay-collection/blob/main/docs/quay_manifest_label_module.rst) |  Manage Quay Container Registry image manifest labels
[quay_manifest_label_info](https://github.com/herve4m/quay-collection/blob/main/docs/quay_manifest_label_info_module.rst) |  Gather information about manifest labels in Quay Container Registry
[quay_message](https://github.com/herve4m/quay-collection/blob/main/docs/quay_message_module.rst) |  Manage Quay Container Registry global messages
[quay_notification](https://github.com/herve4m/quay-collection/blob/main/docs/quay_notification_module.rst) |  Manage Quay Container Registry repository notifications
[quay_organization](https://github.com/herve4m/quay-collection/blob/main/docs/quay_organization_module.rst) |  Manage Quay Container Registry organizations
[quay_proxy_cache](https://github.com/herve4m/quay-collection/blob/main/docs/quay_proxy_cache_module.rst) |  Manage Quay Container Registry proxy cache configurations
[quay_quota](https://github.com/herve4m/quay-collection/blob/main/docs/quay_quota_module.rst) |  Manage Quay Container Registry organizations quota
[quay_repository](https://github.com/herve4m/quay-collection/blob/main/docs/quay_repository_module.rst) |  Manage Quay Container Registry repositories
[quay_repository_mirror](https://github.com/herve4m/quay-collection/blob/main/docs/quay_repository_mirror_module.rst) |  Manage Quay Container Registry repository mirrors
[quay_robot](https://github.com/herve4m/quay-collection/blob/main/docs/quay_robot_module.rst) |  Manage Quay Container Registry robot accounts
[quay_tag](https://github.com/herve4m/quay-collection/blob/main/docs/quay_tag_module.rst) | Manage Quay Container Registry image tags
[quay_tag_info](https://github.com/herve4m/quay-collection/blob/main/docs/quay_tag_info_module.rst) |  Gather information about tags in a Quay Container Registry repository
[quay_team](https://github.com/herve4m/quay-collection/blob/main/docs/quay_team_module.rst) |  Manage Quay Container Registry teams
[quay_team_ldap](https://github.com/herve4m/quay-collection/blob/main/docs/quay_team_ldap_module.rst) |  Synchronize Quay Container Registry teams with LDAP groups
[quay_team_oidc](https://github.com/herve4m/quay-collection/blob/main/docs/quay_team_oidc_module.rst) |  Synchronize Quay Container Registry teams with OIDC groups
[quay_user](https://github.com/herve4m/quay-collection/blob/main/docs/quay_user_module.rst) |  Manage Quay Container Registry users
[quay_vulnerability_info](https://github.com/herve4m/quay-collection/blob/main/docs/quay_vulnerability_info_module.rst) | Gather information about image vulnerabilities in Quay Container Registry

### Jinja2 Filters
Name | Description
---: | :---
[quay_docker_config](https://github.com/herve4m/quay-collection/blob/main/docs/quay_docker_config_filter.rst) |  Build a Docker configuration in JSON format

### Roles
Name | Description
---: | :---
[quay_org](https://github.com/herve4m/quay-collection/blob/main/roles/quay_org/README.md) ([variables](https://github.com/herve4m/quay-collection/blob/main/docs/quay_org_role.rst)) | Create and configure a Quay Container Registry organization | [quay_org](https://github.com/herve4m/quay-collection/blob/main/docs/quay_org_role.rst)


## Installing the Collection

Before using the Quay collection, install it by using the Ansible Galaxy command-line tool:

```bash
ansible-galaxy collection install herve4m.quay
```

As an alternative, you can declare the collection in a `collections/requirements.yml` file inside your Ansible project:

```yaml
---
collections:
  - name: herve4m.quay
```

Use the `ansible-galaxy collection install -r collections/requirements.yml` command to install the collection from this file.
If you manage your Ansible project in automation controller, then automation controller detects this `collections/requirements.yml` file, and automatically installs the collection.

You can also download the tar archive from [Ansible Galaxy](https://galaxy.ansible.com/herve4m/quay), and then manually install the collection.

See [Ansible -- Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.


## Using the Collection

The modules in the collection access Quay through its REST API.
The modules can connect to the API by using a username and a password, or by using an OAuth access token.

There are two ways to get an OAuth access token:

* Use the Quay Container Registry web UI.
* Use the `herve4m.quay.quay_first_user` Ansible module to create the first user account just after you installed Quay Container Registry.
  The module creates and then returns an OAuth access token for the user.
  This token is only valid for 2 hours and 30 minutes.


### Creating an OAuth Access Token by Using the Web UI

Before you can use the collection, you must generate an OAuth access token.
To do so, follow these steps:

1. Log in to the Quay Container Registry web UI.
2. Use an existing organization or create a new one.
3. In the organization, create an application.
4. In the application, select the `Generate Token` menu.
5. Select the permissions to associate to the token.
   To be able to use all the modules in the collection, select `Administer Organization`, `Administer Repositories`, `Create Repositories`, `Super User Access`, and `Administer User`.
6. Click `Generate Token`.
7. Copy and then paste the token string into the `quay_token` module parameter.

The OAuth access token is linked to the user account you use to create it.
Your user account needs to have superuser permissions for some modules to operate correctly.
For example, to manage user accounts, the `herve4m.quay.quay_user` module needs a token created by a user that have superuser permissions.

See the [Quay.io API](https://docs.quay.io/api/) documentation for more details.


### Getting an OAuth Access Token when Creating the First User

Just after you installed Quay Container Registry, and before you do anything else, you can create the first user and generate an OAuth access token for that user.

After this initial operation, you can create additional user accounts by using the `herve4m.quay.quay_user` module and generate OAuth access tokens for these additional accounts by using the `herve4m.quay.quay_api_token` module.

The following playbook example uses the `herve4m.quay.quay_first_user` module to create the first user:

```yaml
---
- name: Bootstrapping a fresh Quay Container Registry installation
  hosts: localhost

  tasks:
    # You must probably ensure that the user account you create, admin in this
    # example, has superuser permissions so that you can use the generated
    # token to create additional objects.
    # To give the user superuser permissions, add its name to the SUPER_USERS
    # section in the config.yaml file.
    - name: Ensure the initial user exists
      herve4m.quay.quay_first_user:
        username: admin
        email: admin@example.com
        password: S6tGwo13
        create_token: true
        quay_host: https://quay.example.com
        validate_certs: true
      register: result

    # The token is valid for 2 hours and 30 minutes
    - name: Display the generated OAuth access token
      debug:
        msg: "Access token: {{ result['access_token'] }}"

    # Using the OAuth access token to continue configuring Quay
    - name: Ensure the user exists
      herve4m.quay.quay_user:
        username: lvasquez
        email: lvasquez@example.com
        password: vs9mrD55NP
        state: present
        quay_token: "{{ result['access_token'] }}"
        quay_host: https://quay.example.com
        validate_certs: true
```

The requirements for the `herve4m.quay.quay_first_user` module are as follows:

* You must use Quay version 3.6 or later.
* You must enable the first user creation feature (`FEATURE_USER_INITIALIZE` in `config.yaml`).
* You must use the internal database for user authentication (`AUTHENTICATION_TYPE` to `Database` in `config.yaml` or `Internal Authentication` to `Local Database` in the configuration web UI).
* You probably want the first user to have superuser permissions.
  To do so, add this user account to the `SUPER_USERS` section in the `config.yaml` file.


### Grouping Common Module Parameters

When your play calls multiple modules from the collection, you can group common module parameters in the `module_defaults` section, under the `group/herve4m.quay.quay` subsection.
For example, instead of repeating the `quay_host`, `quay_username`, and `quay_password` parameters in each task, you can declare them at the top of your play:

```yaml
- name: Creating the development organization and the developers team
  hosts: localhost

  module_defaults:
    group/herve4m.quay.quay:
      quay_host: https://quay.example.com
      quay_username: admin
      quay_password: S6tGwo13

  tasks:
    - name: Ensure the organization exists
      herve4m.quay.quay_organization:
        name: development
        email: devorg@example.com
        time_machine_expiration: "1d"
        state: present

    - name: Ensure the additional user exists
      herve4m.quay.quay_user:
        username: dwilde
        email: dwilde@example.com
        password: 7BbB8T6c
        state: present

    - name: Ensure the team exists in the development organization
      herve4m.quay.quay_team:
        name: developers
        organization: development
        role: creator
        members:
          - lvasquez
          - dwilde
        append: false
        state: present
```


## Contributing to the Collection

We welcome community contributions to this collection.
If you find problems, then please open an [issue](https://github.com/herve4m/quay-collection/issues) or create a [pull request](https://github.com/herve4m/quay-collection/pulls).

More information about contributing can be found in the [Contribution Guidelines](https://github.com/herve4m/quay-collection/blob/main/CONTRIBUTING.md).


## Release Notes

See the [changelog](https://github.com/herve4m/quay-collection/blob/main/CHANGELOG.rst).


## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to read the full text.
