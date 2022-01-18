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

.. _ansible_collections.herve4m.quay.quay_repository_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_repository -- Manage Red Hat Quay repositories
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.9).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_repository`.

.. version_added

.. versionadded:: 0.0.1 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, delete, and update repositories in Red Hat Quay.


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
        <div class="ansibleOptionAnchor" id="parameter-append"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-append:

      .. rst-class:: ansible-option-title

      **append**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-append" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`yes`\ , then add the permission defined in \ :emphasis:`perms`\  to the repository.

      If \ :literal:`no`\ , then the module sets the permissions specified in \ :emphasis:`perms`\ , removing all others permissions from the repository.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-default-bold:`yes` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-description"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-description:

      .. rst-class:: ansible-option-title

      **description**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Text in Markdown format that describes the repository.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-name:

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

      Name of the repository to create, remove, or modify. The format for the name is \ :literal:`namespace`\ /\ :literal:`shortname`\ . The namespace can be an organization or a personal namespace.

      The name must be in lowercase and must not contain white spaces.

      If you omit the namespace part in the name, then the module uses your personal namespace.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-perms"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-perms:

      .. rst-class:: ansible-option-title

      **perms**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-perms" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User, robot, and team permissions to associate with the repository.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-perms/name"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-perms/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-perms/name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Name of the account. The format for robot accounts is \ :literal:`namespace`\ +\ :literal:`shortrobotname`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-perms/role"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-perms/role:

      .. rst-class:: ansible-option-title

      **role**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-perms/role" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Type of permission to grant.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`read` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`write`
      - :ansible-option-choices-entry:`admin`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-perms/type"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-perms/type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-perms/type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Specifies the type of the account. Choose \ :literal:`user`\  for both user and robot accounts.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`user` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`team`

      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quay_host"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-quay_host:

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

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-quay_token:

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
        <div class="ansibleOptionAnchor" id="parameter-repo_state"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-repo_state:

      .. rst-class:: ansible-option-title

      **repo_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-repo_state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`NORMAL`\ , then the repository is in the default state (read/write).

      If \ :literal:`READ\_ONLY`\ , then the repository is read-only.

      If \ :literal:`MIRROR`\ , then the repository is a mirror and you can configure it by using the M(quay_repository_mirror) module.

      You must enable the mirroring capability of your Quay installation to use this \ :emphasis:`repo\_state`\  parameter.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`NORMAL`
      - :ansible-option-choices-entry:`READ\_ONLY`
      - :ansible-option-choices-entry:`MIRROR`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-star"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-star:

      .. rst-class:: ansible-option-title

      **star**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-star" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`yes`\ , then add a star to the repository. If \ :literal:`no`\ , then remove the star.

      To star or unstar a repository you must provide the \ :emphasis:`quay\_token`\  parameter to authenticate. If you are not authenticated, then the module ignores the \ :emphasis:`star`\  parameter.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`absent`\ , then the module deletes the repository.

      The module does not fail if the repository does not exist because the state is already as expected.

      If \ :literal:`present`\ , then the module creates the repository if it does not already exist.

      If the repository already exists, then the module updates its state.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`absent`
      - :ansible-option-default-bold:`present` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
        <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-validate_certs:
      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-verify_ssl:

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
        <div class="ansibleOptionAnchor" id="parameter-visibility"></div>

      .. _ansible_collections.herve4m.quay.quay_repository_module__parameter-visibility:

      .. rst-class:: ansible-option-title

      **visibility**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-visibility" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`public`\ , then anyone can pull images from the repository.

      If \ :literal:`private`\ , then nobody can access the repository and you need to explicitly grant access to users, robots, and teams.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`public`
      - :ansible-option-choices-entry:`private`

      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - You must enable the mirroring capability of your Quay installation (\ :literal:`FEATURE\_REPO\_MIRROR`\  in \ :literal:`config.yaml`\ ) to use the \ :emphasis:`repo\_state`\  parameter.
   - Supports \ :literal:`check\_mode`\ .
   - The token that you provide in \ :emphasis:`quay\_token`\  must have the "Administer Repositories" and "Create Repositories" permissions.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Ensure repository smallimage exists in the production organization
      herve4m.quay.quay_repository:
        name: production/smallimage
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
          - name: production+automationrobot
            type: user
            role: admin
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure repository bigimage exists in my namespace
      herve4m.quay.quay_repository:
        name: bigimage
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
        name: development/testimg
        state: absent
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the repository has the exact set of permissions
      herve4m.quay.quay_repository:
        name: production/smallimage
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
          - name: production+auditrobot
            type: user
            role: read
        append: false
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the repository has a star
      herve4m.quay.quay_repository:
        name: production/smallimage
        star: true
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    # You must enable the mirroring capability of your Quay installation
    # to use the repo_state parameter.
    - name: Ensure the repository is prepared for mirroring
      herve4m.quay.quay_repository:
        name: production/smallimage
        repo_state: MIRROR
        state: present
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

