.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-entry
.. role:: ansible-option-default
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.herve4m.quay.quay_repository_mirror_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_repository_mirror -- Manage Red Hat Quay repository mirror configurations
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.9).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_repository_mirror`.

.. version_added

.. versionadded:: 0.0.4 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Configure and synchronize repository mirrors in Red Hat Quay.


.. Aliases


.. Requirements


.. Options

Parameters
----------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-external_reference"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-external_reference:

      .. rst-class:: ansible-option-title

      **external_reference**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-external_reference" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Path to the remote container repository to synchronize, such as quay.io/projectquay/quay for example.

      That parameter is required when creating the mirroring configuration.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-external_registry_password"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-external_registry_password:

      .. rst-class:: ansible-option-title

      **external_registry_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-external_registry_password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password to use for pulling the image from the remote registry.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-external_registry_username"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-external_registry_username:

      .. rst-class:: ansible-option-title

      **external_registry_username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-external_registry_username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Username to use for pulling the image from the remote registry.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-force_sync"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-force_sync:

      .. rst-class:: ansible-option-title

      **force_sync**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-force_sync" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Triggers an immediate image synchronization.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-http_proxy"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-http_proxy:

      .. rst-class:: ansible-option-title

      **http_proxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-http_proxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      HTTP proxy to use for accessing the remote container registry.

      See the \ :literal:`curl`\  documentation for more details.

      By default, no proxy is used.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-https_proxy"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-https_proxy:

      .. rst-class:: ansible-option-title

      **https_proxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-https_proxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      HTTPS proxy to use for accessing the remote container registry.

      See the \ :literal:`curl`\  documentation for more details.

      By default, no proxy is used.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-image_tags"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-image_tags:

      .. rst-class:: ansible-option-title

      **image_tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-image_tags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of image tags to be synchronized from the remote repository.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_enabled"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-is_enabled:

      .. rst-class:: ansible-option-title

      **is_enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-is_enabled" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines whether the mirror configuration is active or inactive.

      \ :literal:`false`\  by default.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the existing repository for which the mirror parameters are configured. The format for the name is \ :literal:`namespace`\ /\ :literal:`shortname`\ . The namespace can only be an organization namespace.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-no_proxy"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-no_proxy:

      .. rst-class:: ansible-option-title

      **no_proxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-no_proxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Comma-separated list of hosts for which the proxy should not be used.

      Only relevant when you also specify a proxy configuration by setting the \ :emphasis:`http\_proxy`\  or \ :emphasis:`https\_proxy`\  variables.

      See the \ :literal:`curl`\  documentation for more details.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quay_host"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-quay_host:

      .. rst-class:: ansible-option-title

      **quay_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-quay_host" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL for accessing the API. \ https://quay.example.com:8443\  for example.

      If you do not set the parameter, then the module uses the \ :literal:`QUAY\_HOST`\  environment variable.

      If you do no set the environment variable either, then the module uses the \ http://127.0.0.1\  URL.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"http://127.0.0.1"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quay_token"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-quay_token:

      .. rst-class:: ansible-option-title

      **quay_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-quay_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      OAuth access token for authenticating with the API.

      If you do not set the parameter, then the module tries the \ :literal:`QUAY\_TOKEN`\  environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-robot_username"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-robot_username:

      .. rst-class:: ansible-option-title

      **robot_username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-robot_username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Username of the robot account that is used for synchronization.

      That parameter is required when creating the mirroring configuration.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sync_interval"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-sync_interval:

      .. rst-class:: ansible-option-title

      **sync_interval**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sync_interval" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Synchronization interval for this repository mirror in seconds.

      86400 (one day) by default.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sync_start_date"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-sync_start_date:

      .. rst-class:: ansible-option-title

      **sync_start_date**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sync_start_date" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The date and time at which the first synchronization should be initiated.

      The format for the \ :emphasis:`sync\_start\_date`\  parameter is ISO 8601 UTC, such as 2021-12-02T21:06:00Z.

      If you do not provide the \ :emphasis:`sync\_start\_date`\  parameter when you configure a new repository mirror, then the synchronization is immediately active, and a synchronization is initiated if the \ :emphasis:`is\_enabled`\  parameter is \ :literal:`true`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
        <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-validate_certs:
      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-verify_ssl:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: verify_ssl`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to allow insecure connections to the API.

      If \ :literal:`no`\ , then the module does not validate SSL certificates.

      If you do not set the parameter, then the module tries the \ :literal:`QUAY\_VERIFY\_SSL`\  environment variable (\ :literal:`yes`\ , \ :literal:`1`\ , and \ :literal:`True`\  mean yes, and \ :literal:`no`\ , \ :literal:`0`\ , \ :literal:`False`\ , and no value mean no).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-default-bold:`yes` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-verify_tls"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_mirror_module__parameter-verify_tls:

      .. rst-class:: ansible-option-title

      **verify_tls**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-verify_tls" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines whether TLS of the external registry should be verified.

      \ :literal:`true`\  by default.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - You must enable the mirroring capability of your Quay installation (\ :literal:`FEATURE\_REPO\_MIRROR`\  in \ :literal:`config.yaml`\ ) to use that module.
   - You cannot modify a repository mirroring configuration if a synchronization is in progress.
   - There is no API function to remove the configuration. However, you can deactivate mirroring by setting the \ :emphasis:`is\_enabled`\  parameter to \ :literal:`false`\  or by changing the repository mirror state (see the \ :emphasis:`repo\_state`\  parameter in the M(quay_repository) module). The configuration is preserved when you disable mirroring.
   - Supports \ :literal:`check\_mode`\ .
   - The token that you provide in \ :emphasis:`quay\_token`\  must have the "Administer Repositories" and "Create Repositories" permissions.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Ensure mirroring configuration is set for the existing production/smallimage repo
      herve4m.quay.quay_repository_mirror:
        name: production/smallimage
        external_reference: quay.io/projectquay/quay
        http_proxy: http://proxy.example.com:3128
        robot_username: production+auditrobot
        is_enabled: true
        image_tags:
          - latest
          - v3.5.2
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure mirroring is disabled for the production/smallimage repository
      herve4m.quay.quay_repository_mirror:
        name: production/smallimage
        is_enabled: false
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Immediate trigger a synchronization of the repository
      herve4m.quay.quay_repository_mirror:
        name: production/smallimage
        force_sync: true
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7





.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Herve Quatremain (@herve4m)



.. Parsing errors

