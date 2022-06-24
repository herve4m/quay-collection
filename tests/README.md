# Tests for the Quay Container Registry Collection

GitHub Actions trigger the tests in this directory.
The GitHub Actions workflow YAML files are defined in the [GitHub Actions workflow directory](https://github.com/herve4m/quay-collection/tree/main/.github/workflows).

The workflow uses the `docker-compose.yml` file to deploy a testing Quay environment, and then the `ansible-test integration` command to perform the integration tests.
Those tests consist of running the roles (playbooks) defined under the `integration/targets` directory.

## Running a Test Manually

If you want to run one of these playbooks manually against your Quay installation, then prepare your environment as follows:

* Make a copy of the `sample_manual_test.yml` playbook model and then update your copy.
  Change the role to run and provide the connection parameters to your Quay installation.
* Install the Quay Container Registry collection in your environment by using the `ansible-galaxy collection install` command.
* Run your copy of the playbook with the `ansible-playbook` command.

If you are using a fresh Quay installation that you have not configured yet, then you do not need to set the `default_token` variable in your copy of the playbook.
The test framework will try to create the first user account and use its OAuth access token for later authentications.
This mechanism requires:

* Quay version 3.6 or later.
* A pristine Quay installation (an empty database).
* The `FEATURE_USER_INITIALIZE` parameter set to `true` in the `config.yaml` file.
* User authentication performed against the internal database (the `AUTHENTICATION_TYPE` parameter must be set to `Database` in `config.yaml`, or `Internal Authentication` to `Local Database` in the configuration web UI)
* The `SUPER_USERS` parameter in `config.yaml` must include the `admin` user.
  The test playbooks use that user account.

Otherwise, you need to create an OAuth access token by using the Quay web UI and paste that token into the `default_token` variable.
