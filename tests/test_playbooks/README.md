# Tests for the Red Hat Quay Collection

The playbooks in this directory test the collection modules.
Use a fresh Quay installation to perform the tests.


## Preparing for Running the Tests

Edit the `variables.yml` file to provide the connection parameters to your Quay installation.

If you are using a fresh Quay installation that you have not configured yet, then you only need to modify the `quay_url` variable.
The test framework will try to create the first user account and use its OAuth token for later authentications.
This mechanism requires:

* Red Hat Quay version 3.6 or later.
* A pristine Quay installation (an empty database).
* The `FEATURE_USER_INITIALIZE` parameter set to `true` in the `config.yaml` file.
* User authentication performed against the internal database (the `AUTHENTICATION_TYPE` parameter must be set to `Database` in `config.yaml`, or `Internal Authentication` to `Local Database` in the configuration web UI)
* The `SUPER_USERS` parameter in `config.yaml` must include the `admin` user.
  The test playbooks use that user account.

Otherwise, you need to create an OAuth 2 token by using the Quay web UI and paste that token into the `default_token` variable.

## Running the Tests

The tests are independent.
You can run a test by using the `ansible-playbook` command.
