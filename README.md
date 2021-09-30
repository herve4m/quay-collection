# Red Hat Quay Collection for Ansible

The collection provides modules for managing your Red Hat Quay deployment.

## Included Content

The modules have been tested against version 3.5.6 of Red Quay.

### Modules
Name | Description
---: | :---
quay_application |  Manage Red Hat Quay organizations
quay_default_perm |  Manage Red Hat Quay default repository permissions
quay_image_info |  Gather information about images in a Red Hat Quay repository
quay_message |  Manage Red Hat Quay global messages
quay_notification |  Manage Red Hat Quay repository notifications
quay_organization |  Manage Red Hat Quay organizations
quay_repository |  Manage Red Hat Quay repositories
quay_robot |  Manage Red Hat Quay robot accounts
quay_tag_info |  Gather information about tags in a Red Hat Quay repository
quay_team |  Manage Red Hat Quay teams
quay_user |  Manage Red Hat Quay users


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

## Contributing to the Collection

We welcome community contributions to this collection.
If you find problems, then please open an [issue](https://github.com/herve4m/quay-collection/issues) or create a [pull request](https://github.com/herve4m/quay-collection/pulls).

More information about contributing can be found in the [Contribution Guidelines](https://github.com/herve4m/quay-collection/blob/main/CONTRIBUTING.md).


## Release Notes

See the [changelog](https://github.com/herve4m/quay-collection/blob/main/CHANGELOG.rst).


## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to read the full text.
