# Red Hat Quay Collection for Ansible

[![Code linting](https://github.com/herve4m/quay-collection/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/herve4m/quay-collection/actions/workflows/pre-commit.yml)

The collection provides modules for managing your Red Hat Quay deployment.

## Included Content

The modules have been tested against versions 3.5.6, 3.6.1, and 3.6.2 of Red Hat Quay.

### Modules
Name | Description
---: | :---
[quay_application](https://github.com/herve4m/quay-collection/blob/main/docs/quay_application_module.rst) |  Manage Red Hat Quay applications
[quay_default_perm](https://github.com/herve4m/quay-collection/blob/main/docs/quay_default_perm_module.rst) |  Manage Red Hat Quay default repository permissions
[quay_first_user](https://github.com/herve4m/quay-collection/blob/main/docs/quay_first_user_module.rst) |  Create the first user account
[quay_layer_info](https://github.com/herve4m/quay-collection/blob/main/docs/quay_layer_info_module.rst) |  Gather information about image layers in Red Hat Quay
[quay_message](https://github.com/herve4m/quay-collection/blob/main/docs/quay_message_module.rst) |  Manage Red Hat Quay global messages
[quay_notification](https://github.com/herve4m/quay-collection/blob/main/docs/quay_notification_module.rst) |  Manage Red Hat Quay repository notifications
[quay_organization](https://github.com/herve4m/quay-collection/blob/main/docs/quay_organization_module.rst) |  Manage Red Hat Quay organizations
[quay_repository](https://github.com/herve4m/quay-collection/blob/main/docs/quay_repository_module.rst) |  Manage Red Hat Quay repositories
[quay_repository_mirror](https://github.com/herve4m/quay-collection/blob/main/docs/quay_repository_mirror_module.rst) |  Manage Red Hat Quay repositories mirrors
[quay_robot](https://github.com/herve4m/quay-collection/blob/main/docs/quay_robot_module.rst) |  Manage Red Hat Quay robot accounts
[quay_tag](https://github.com/herve4m/quay-collection/blob/main/docs/quay_tag_module.rst) | Manage Red Hat Quay image tags
[quay_tag_info](https://github.com/herve4m/quay-collection/blob/main/docs/quay_tag_info_module.rst) |  Gather information about tags in a Red Hat Quay repository
[quay_team](https://github.com/herve4m/quay-collection/blob/main/docs/quay_team_module.rst) |  Manage Red Hat Quay teams
[quay_user](https://github.com/herve4m/quay-collection/blob/main/docs/quay_user_module.rst) |  Manage Red Hat Quay users
[quay_vulnerability_info](https://github.com/herve4m/quay-collection/blob/main/docs/quay_vulnerability_info_module.rst) | Gather information about image vulnerabilities in Red Hat Quay


## Installing the Collection

Before using the Red Hat Quay collection, install it by using the Ansible Galaxy command-line tool:

```bash
ansible-galaxy collection install herve4m.quay
```

As an alternative, you can declare the collection in a `collections/requirements.yml` file inside your Ansible project:

```yaml
---
collections:
  - name: herve4m.quay
```

Use the `ansible-galaxy collection install -r collections/requirements.yml` command to install the collection from that file.
If you manage your Ansible project in automation controller, then automation controller detects that `collections/requirements.yml` file and automatically installs the collection.

You can also download the tar archive from [Ansible Galaxy](https://galaxy.ansible.com/herve4m/quay) and then manually install the collection.

See [Ansible -- Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.


## Using the Collection

The modules in the collection access Red Hat Quay through its REST API.
To use the API, Red Hat Quay requires an OAuth 2 access token.
You cannot use a user name and a password for authenticating.

There are two ways to get an OAuth 2 access token:

* Use the Red Hat Quay web UI.
* Use the `herve4m.quay.quay_first_user` Ansible module to create the first user account just after you installed Red Hat Quay.
  The module creates and then returns the OAuth 2 access token for the user.


### Creating an OAuth 2 Access Token by Using the Web UI

Before you can use the collection, you must generate an OAuth 2 access token.
To do so, follow those steps:

1. Log in to the Red Hat Quay web UI.
2. Use an existing organization or create a new one.
3. In the organization, create an application.
4. In the application, select the `Generate Token` menu.
5. Select the permissions to associate to the token.
   To be able to use all the modules in the collection, select `Administer Organization`, `Administer Repositories`, `Create Repositories`, `Super User Access`, and `Administer User`.
6. Click `Generate Token`.
7. Copy and then paste the token string into the `quay_token` module parameter.

The OAuth 2 access token is linked to the user account you use to create it.
Your user account needs to have superuser permissions for some modules to operate correctly.
For example, to manage user accounts, the `herve4m.quay.quay_user` module needs a token created by a user that have superuser permissions.

See the [Quay.io API](https://docs.quay.io/api/) documentation for more details.


### Getting an OAuth 2 Access Token when Creating the First User

Just after you installed Red Hat Quay, and before you do anything else, you can create the first user and generate an OAuth 2 Access Token for that user.

The following playbook example uses the `herve4m.quay.quay_first_user` module to create the first user:

```yaml
---
- name: Bootstrapping a fresh Red Hat Quay installation
  hosts: localhost

  tasks:
    - name: Ensure the initial user exists
      herve4m.quay.quay_first_user:
        username: admin
        email: admin@example.com
        password: S6tGwo13
        create_token: true
        quay_host: https://quay.example.com
        validate_certs: true
      register: result

    - name: Display the generated OAuth 2 access token
      debug:
        msg: "Access token: {{ result['access_token'] }}"

    # Using the OAuth 2 access token to continue configuring Red Hat Quay
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

* You must use Red Hat Quay 3.6 or later.
* You must enable the first user creation feature (`FEATURE_USER_INITIALIZE` in `config.yaml`).
* You must use the internal database for user authentication (`AUTHENTICATION_TYPE` to `Database` in `config.yaml` or `Internal Authentication` to `Local Database` in the configuration web UI).


## Contributing to the Collection

We welcome community contributions to this collection.
If you find problems, then please open an [issue](https://github.com/herve4m/quay-collection/issues) or create a [pull request](https://github.com/herve4m/quay-collection/pulls).

More information about contributing can be found in the [Contribution Guidelines](https://github.com/herve4m/quay-collection/blob/main/CONTRIBUTING.md).


## Release Notes

See the [changelog](https://github.com/herve4m/quay-collection/blob/main/CHANGELOG.rst).


## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to read the full text.
