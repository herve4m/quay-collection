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

herve4m.quay.quay_repository_mirror module -- Manage Quay Container Registry repository mirror configurations
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.1.1).

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

- Configure and synchronize repository mirrors in Quay Container Registry.


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
      <div class="ansibleOptionAnchor" id="parameter-external_reference"></div>
      <p class="ansible-option-title"><strong>external_reference</strong></p>
      <a class="ansibleOptionLink" href="#parameter-external_reference" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Path to the remote container repository to synchronize, such as quay.io/projectquay/quay for example.</p>
      <p>That parameter is required when creating the mirroring configuration.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-external_registry_password"></div>
      <p class="ansible-option-title"><strong>external_registry_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-external_registry_password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Password to use for pulling the image from the remote registry.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-external_registry_username"></div>
      <p class="ansible-option-title"><strong>external_registry_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-external_registry_username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Username to use for pulling the image from the remote registry.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-force_sync"></div>
      <p class="ansible-option-title"><strong>force_sync</strong></p>
      <a class="ansibleOptionLink" href="#parameter-force_sync" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Triggers an immediate image synchronization.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">no</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-http_proxy"></div>
      <p class="ansible-option-title"><strong>http_proxy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-http_proxy" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>HTTP proxy to use for accessing the remote container registry.</p>
      <p>See the <code class='docutils literal notranslate'>curl</code> documentation for more details.</p>
      <p>By default, no proxy is used.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-https_proxy"></div>
      <p class="ansible-option-title"><strong>https_proxy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-https_proxy" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>HTTPS proxy to use for accessing the remote container registry.</p>
      <p>See the <code class='docutils literal notranslate'>curl</code> documentation for more details.</p>
      <p>By default, no proxy is used.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-image_tags"></div>
      <p class="ansible-option-title"><strong>image_tags</strong></p>
      <a class="ansibleOptionLink" href="#parameter-image_tags" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of image tags to be synchronized from the remote repository.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-is_enabled"></div>
      <p class="ansible-option-title"><strong>is_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-is_enabled" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Defines whether the mirror configuration is active or inactive.</p>
      <p><code class='docutils literal notranslate'>false</code> by default.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
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
      <p>Name of the existing repository for which the mirror parameters are configured. The format for the name is <code class='docutils literal notranslate'>namespace</code>/<code class='docutils literal notranslate'>shortname</code>. The namespace can only be an organization namespace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-no_proxy"></div>
      <p class="ansible-option-title"><strong>no_proxy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-no_proxy" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Comma-separated list of hosts for which the proxy should not be used.</p>
      <p>Only relevant when you also specify a proxy configuration by setting the <em>http_proxy</em> or <em>https_proxy</em> variables.</p>
      <p>See the <code class='docutils literal notranslate'>curl</code> documentation for more details.</p>
    </div></td>
  </tr>
  <tr class="row-even">
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
      <p class="ansible-option-line"><span class="ansible-option-default-bold">Default:</span> <span class="ansible-option-default">"http://127.0.0.1"</span></p>
    </div></td>
  </tr>
  <tr class="row-odd">
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
  <tr class="row-even">
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
  <tr class="row-odd">
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
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-robot_username"></div>
      <p class="ansible-option-title"><strong>robot_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-robot_username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Username of the robot account that is used for synchronization.</p>
      <p>That parameter is required when creating the mirroring configuration.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-sync_interval"></div>
      <p class="ansible-option-title"><strong>sync_interval</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sync_interval" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Synchronization interval for this repository mirror in seconds.</p>
      <p>86400 (one day) by default.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-sync_start_date"></div>
      <p class="ansible-option-title"><strong>sync_start_date</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sync_start_date" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The date and time at which the first synchronization should be initiated.</p>
      <p>The format for the <em>sync_start_date</em> parameter is ISO 8601 UTC, such as 2021-12-02T21:06:00Z.</p>
      <p>If you do not provide the <em>sync_start_date</em> parameter when you configure a new repository mirror, then the synchronization is immediately active, and a synchronization is initiated if the <em>is_enabled</em> parameter is <code class='docutils literal notranslate'>true</code>.</p>
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
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-default-bold">yes</span> <span class="ansible-option-default">← (default)</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-verify_tls"></div>
      <p class="ansible-option-title"><strong>verify_tls</strong></p>
      <a class="ansibleOptionLink" href="#parameter-verify_tls" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Defines whether TLS of the external registry should be verified.</p>
      <p><code class='docutils literal notranslate'>true</code> by default.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
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
   - Your Quay administrator must enable the mirroring capability of your Quay installation (\ :literal:`FEATURE\_REPO\_MIRROR`\  in \ :literal:`config.yaml`\ ) to use that module.
   - You cannot modify a repository mirroring configuration if a synchronization is in progress.
   - There is no API function to remove the configuration. However, you can deactivate mirroring by setting the \ :emphasis:`is\_enabled`\  parameter to \ :literal:`false`\  or by changing the repository mirror state (see the \ :emphasis:`repo\_state`\  parameter in the M(quay_repository) module). The configuration is preserved when you disable mirroring.
   - Supports \ :literal:`check\_mode`\ .
   - The user account associated with the token that you provide in \ :emphasis:`quay\_token`\  must have administrator access to the repository.

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



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/herve4m/quay-collection/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/herve4m/quay-collection" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

