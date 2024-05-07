
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.11.0

.. Anchors

.. _ansible_collections.herve4m.quay.quay_organization_module:

.. Anchors: short name for ansible.builtin

.. Title

herve4m.quay.quay_organization module -- Manage Quay Container Registry organizations
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/ui/repo/published/herve4m/quay/>`_ (version 1.3.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_organization`.

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

- Create, delete, and update organizations in Quay Container Registry.


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
  <tr class="row-odd">
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
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-email"></div>
      <p class="ansible-option-title"><strong>email</strong></p>
      <a class="ansibleOptionLink" href="#parameter-email" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Email address to associate with the new organization.</p>
      <p>If your Quay administrator has enabled the mailing capability of your Quay installation (<code class='docutils literal notranslate'>FEATURE_MAILING</code> to <code class='docutils literal notranslate'>true</code> in <code class='docutils literal notranslate'>config.yaml</code>), then this <em>email</em> parameter is mandatory.</p>
      <p>You cannot use the same address as your account email.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
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
      <p>Name of the organization to create, remove, or modify.</p>
      <p>The name must be in lowercase and must not contain white spaces. For compatibility with earlier versions of Docker, the name must be at least four characters long.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-new_name"></div>
      <p class="ansible-option-title"><strong>new_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-new_name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>New name for the organization.</p>
      <p>Setting this option changes the name of the organization which current name is provided in <em>name</em>.</p>
      <p>The token you use to connect to the API (in <em>quay_token</em>) must have the "Super User Access" permission.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p class="ansible-option-title"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>absent</code>, then the module deletes the organization.</p>
      <p>The module does not fail if the organization does not exist, because the state is already as expected.</p>
      <p>If <code class='docutils literal notranslate'>present</code>, then the module creates the organization if it does not already exist.</p>
      <p>If the organization already exists, then the module updates its state.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;absent&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>&#34;present&#34;</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-time_machine_expiration"></div>
      <p class="ansible-option-title"><strong>time_machine_expiration</strong></p>
      <a class="ansibleOptionLink" href="#parameter-time_machine_expiration" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The amount of time, after a tag is deleted, that the tag is accessible in time machine before being garbage collected.</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;0s&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;1d&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;7d&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;14d&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;1month&#34;</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-odd">
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
  </tbody>
  </table>



.. Attributes


.. Notes

Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .
   - Your Quay administrator must enable the auto-prune capability of your Quay installation (\ :literal:`FEATURE\_AUTO\_PRUNE`\  in \ :literal:`config.yaml`\ ) to use the \ :emphasis:`auto\_prune\_method`\  and \ :emphasis:`auto\_prune\_value`\  parameters.
   - Using \ :emphasis:`auto\_prune\_method`\  and \ :emphasis:`auto\_prune\_value`\  requires Quay version 3.11 or later.
   - The token that you provide in \ :emphasis:`quay\_token`\  must have the "Administer Organization" and "Administer User" permissions.
   - To rename organizations, the token must also have the "Super User Access" permission.
   - Your Quay administrator must enable the auto-prune capability of your Quay installation (\ :literal:`FEATURE\_AUTO\_PRUNE`\  in \ :literal:`config.yaml`\ ) to use the \ :emphasis:`auto\_prune\_method`\  and \ :emphasis:`auto\_prune\_value`\  parameters.
   - Using \ :emphasis:`auto\_prune\_method`\  and \ :emphasis:`auto\_prune\_value`\  requires Quay version 3.11 or later.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Ensure the organization exists
      herve4m.quay.quay_organization:
        name: production
        email: prodlist@example.com
        time_machine_expiration: "7d"
        auto_prune_method: tags
        auto_prune_value: 20
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    # Renaming requires superuser permissions
    - name: Ensure the organization has a new name
      herve4m.quay.quay_organization:
        name: production
        new_name: development
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the organization is removed
      herve4m.quay.quay_organization:
        name: development
        state: absent
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

