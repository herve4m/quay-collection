
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.11.0

.. Anchors

.. _ansible_collections.herve4m.quay.quay_repository_module:

.. Anchors: short name for ansible.builtin

.. Title

herve4m.quay.quay_repository module -- Manage Quay Container Registry repositories
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/ui/repo/published/herve4m/quay/>`_ (version 1.3.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_repository`.

.. version_added

.. rst-class:: ansible-version-added

New in herve4m.quay 0.0.1

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, delete, and update repositories in Quay Container Registry.


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Parameter</p></th>
    <th class="head"><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-append"></div>
      <p class="ansible-option-title"><strong>append</strong></p>
      <a class="ansibleOptionLink" href="#parameter-append" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>yes</code>, then add the permission defined in <em>perms</em> to the repository.</p>
      <p>If <code class='docutils literal notranslate'>no</code>, then the module sets the permissions specified in <em>perms</em>, removing all others permissions from the repository.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">false</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>true</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-auto_prune_method"></div>
      <p class="ansible-option-title"><strong>auto_prune_method</strong></p>
      <a class="ansibleOptionLink" href="#parameter-auto_prune_method" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Method to use for the auto-pruning tags policy.</p>
      <p>If <code class='docutils literal notranslate'>none</code>, then the module ensures that no policy is in place. The tags are not pruned.</p>
      <p>If <code class='docutils literal notranslate'>tags</code>, then the policy keeps only the number of tags that you specify in <em>auto_prune_value</em>.</p>
      <p>If <code class='docutils literal notranslate'>date</code>, then the policy deletes the tags older than the time period that you specify in <em>auto_prune_value</em>.</p>
      <p><em>auto_prune_value</em> is required when <em>auto_prune_method</em> is <code class='docutils literal notranslate'>tags</code> or <code class='docutils literal notranslate'>date</code>.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;none&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;tags&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;date&#34;</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-auto_prune_value"></div>
      <p class="ansible-option-title"><strong>auto_prune_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-auto_prune_value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Number of tags to keep when <em>auto_prune_value</em> is <code class='docutils literal notranslate'>tags</code>. The value must be 1 or more.</p>
      <p>Period of time when <em>auto_prune_value</em> is <code class='docutils literal notranslate'>date</code>. The value must be 1 or more, and must be followed by a suffix; s (for second), m (for minute), h (for hour), d (for day), or w (for week).</p>
      <p><em>auto_prune_method</em> is required when <em>auto_prune_value</em> is set.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Text in Markdown format that describes the repository.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the repository to create, remove, or modify. The format for the name is <code class='docutils literal notranslate'>namespace</code>/<code class='docutils literal notranslate'>shortname</code>. The namespace can be an organization or a personal namespace.</p>
      <p>The name must be in lowercase and must not contain white spaces.</p>
      <p>If you omit the namespace part in the name, then the module uses your personal namespace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-perms"></div>
      <p class="ansible-option-title"><strong>perms</strong></p>
      <a class="ansibleOptionLink" href="#parameter-perms" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>User, robot, and team permissions to associate with the repository.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-perms/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-perms/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the account. The format for robot accounts is <code class='docutils literal notranslate'>namespace</code>+<code class='docutils literal notranslate'>shortrobotname</code>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-perms/role"></div>
      <p class="ansible-option-title"><strong>role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-perms/role" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Type of permission to grant.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>&#34;read&#34;</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;write&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;admin&#34;</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-perms/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-perms/type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Specifies the type of the account. Choose <code class='docutils literal notranslate'>user</code> for both user and robot accounts.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>&#34;user&#34;</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;team&#34;</code></p></li>
      </ul>

    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_host"></div>
      <p class="ansible-option-title"><strong>quay_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_host" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>URL for accessing the API. <a href='https://quay.example.com:8443'>https://quay.example.com:8443</a> for example.</p>
      <p>If you do not set the parameter, then the module uses the <code class='docutils literal notranslate'>QUAY_HOST</code> environment variable.</p>
      <p>If you do no set the environment variable either, then the module uses the <a href='http://127.0.0.1'>http://127.0.0.1</a> URL.</p>
      <p class="ansible-option-line"><strong class="ansible-option-default-bold">Default:</strong> <code class="ansible-value literal notranslate ansible-option-default">&#34;http://127.0.0.1&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_password"></div>
      <p class="ansible-option-title"><strong>quay_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The password to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_PASSWORD</code> environment variable.</p>
      <p>If you set <em>quay_password</em>, then you also need to set <em>quay_username</em>.</p>
      <p>Mutually exclusive with <em>quay_token</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_token"></div>
      <p class="ansible-option-title"><strong>quay_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>OAuth access token for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_TOKEN</code> environment variable.</p>
      <p>Mutually exclusive with <em>quay_username</em> and <em>quay_password</em>.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_username"></div>
      <p class="ansible-option-title"><strong>quay_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The username to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_USERNAME</code> environment variable.</p>
      <p>If you set <em>quay_username</em>, then you also need to set <em>quay_password</em>.</p>
      <p>Mutually exclusive with <em>quay_token</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-repo_state"></div>
      <p class="ansible-option-title"><strong>repo_state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-repo_state" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>NORMAL</code>, then the repository is in the default state (read/write).</p>
      <p>If <code class='docutils literal notranslate'>READ_ONLY</code>, then the repository is read-only.</p>
      <p>If <code class='docutils literal notranslate'>MIRROR</code>, then the repository is a mirror and you can configure it by using the <a href='../../herve4m/quay/quay_repository_mirror_module.html' class='module'>herve4m.quay.quay_repository_mirror</a> module.</p>
      <p>You must enable the mirroring capability of your Quay installation to use this <em>repo_state</em> parameter.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;NORMAL&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;READ_ONLY&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;MIRROR&#34;</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-star"></div>
      <p class="ansible-option-title"><strong>star</strong></p>
      <a class="ansibleOptionLink" href="#parameter-star" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>yes</code>, then add a star to the repository. If <code class='docutils literal notranslate'>no</code>, then remove the star.</p>
      <p>To star or unstar a repository you must provide the <em>quay_token</em> parameter to authenticate. If you are not authenticated, then the module ignores the <em>star</em> parameter.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">false</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">true</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p class="ansible-option-title"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>absent</code>, then the module deletes the repository.</p>
      <p>The module does not fail if the repository does not exist, because the state is already as expected.</p>
      <p>If <code class='docutils literal notranslate'>present</code>, then the module creates the repository if it does not already exist.</p>
      <p>If the repository already exists, then the module updates its state.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;absent&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>&#34;present&#34;</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>
      <p class="ansible-option-title"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p class="ansible-option-type-line"><span class="ansible-option-aliases">aliases: verify_ssl</span></p>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Whether to allow insecure connections to the API.</p>
      <p>If <code class='docutils literal notranslate'>no</code>, then the module does not validate SSL certificates.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_VERIFY_SSL</code> environment variable (<code class='docutils literal notranslate'>yes</code>, <code class='docutils literal notranslate'>1</code>, and <code class='docutils literal notranslate'>True</code> mean yes, and <code class='docutils literal notranslate'>no</code>, <code class='docutils literal notranslate'>0</code>, <code class='docutils literal notranslate'>False</code>, and no value mean no).</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">false</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>true</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-visibility"></div>
      <p class="ansible-option-title"><strong>visibility</strong></p>
      <a class="ansibleOptionLink" href="#parameter-visibility" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>public</code>, then anyone can pull images from the repository.</p>
      <p>If <code class='docutils literal notranslate'>private</code>, then nobody can access the repository and you need to explicitly grant access to users, robots, and teams.</p>
      <p>If you do not set the parameter when you create a repository, then it defaults to <code class='docutils literal notranslate'>private</code>.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;public&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;private&#34;</code></p></li>
      </ul>

    </div></td>
  </tr>
  </tbody>
  </table>



.. Attributes


.. Notes

Notes
-----

.. note::
   - Your Quay administrator must enable the mirroring capability of your Quay installation (\ :literal:`FEATURE\_REPO\_MIRROR`\  in \ :literal:`config.yaml`\ ) to use the \ :emphasis:`repo\_state`\  parameter.
   - Supports \ :literal:`check\_mode`\ .
   - The token that you provide in \ :emphasis:`quay\_token`\  must have the "Administer Repositories" and "Create Repositories" permissions.
   - Your Quay administrator must enable the auto-prune capability of your Quay installation (\ :literal:`FEATURE\_AUTO\_PRUNE`\  in \ :literal:`config.yaml`\ ) to use the \ :emphasis:`auto\_prune\_method`\  and \ :emphasis:`auto\_prune\_value`\  parameters.
   - Using \ :emphasis:`auto\_prune\_method`\  and \ :emphasis:`auto\_prune\_value`\  requires Quay version 3.11 or later.

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

    - name: Ensure the repository has a star and tags older that 4 weeks are pruned
      herve4m.quay.quay_repository:
        name: production/smallimage
        star: true
        auto_prune_method: date
        auto_prune_value: 4w
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



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/herve4m/quay-collection/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/herve4m/quay-collection"
    external: true


.. Parsing errors

