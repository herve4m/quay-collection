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

.. _ansible_collections.herve4m.quay.quay_team_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_team module -- Manage Quay Container Registry teams
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.1.1).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_team`.

.. version_added

.. versionadded:: 0.0.1 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, delete, and update teams in organizations.


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
      <p>If <code class='docutils literal notranslate'>yes</code>, then add the users specified in <em>members</em> to the team.</p>
      <p>If <code class='docutils literal notranslate'>no</code>, then the module sets the team members to users specified in <em>members</em>, removing all others users from the team.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-default-bold">yes</span> <span class="ansible-option-default">← (default)</span></p></li>
      </ul>
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
      <p>Text in Markdown format that describes the team.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-members"></div>
      <p class="ansible-option-title"><strong>members</strong></p>
      <a class="ansibleOptionLink" href="#parameter-members" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of the user or robot accounts in the team. Use the syntax <code class='docutils literal notranslate'>organization</code>+<code class='docutils literal notranslate'>robotshortname</code> for robot accounts.</p>
      <p>If the team is synchronized with an LDAP group (see the M(quay_team_ldap) module), then you can only add or remove robot accounts.</p>
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
      <p>Name of the team to create, remove, or modify.</p>
      <p>The name must be in lowercase, must not contain white spaces, must not start by a digit, and must be at least two characters long.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-organization"></div>
      <p class="ansible-option-title"><strong>organization</strong></p>
      <a class="ansibleOptionLink" href="#parameter-organization" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the organization for the team. That organization must exist.</p>
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
      <p class="ansible-option-line"><span class="ansible-option-default-bold">Default:</span> <span class="ansible-option-default">"http://127.0.0.1"</span></p>
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
      <div class="ansibleOptionAnchor" id="parameter-role"></div>
      <p class="ansible-option-title"><strong>role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Role of the team within the organization. If not set, then the new team has the <code class='docutils literal notranslate'>member</code> role.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">member</span></p></li>
        <li><p><span class="ansible-option-choices-entry">creator</span></p></li>
        <li><p><span class="ansible-option-choices-entry">admin</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p class="ansible-option-title"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>absent</code>, then the module deletes the team.</p>
      <p>The module does not fail if the team does not exist because the state is already as expected.</p>
      <p>If <code class='docutils literal notranslate'>present</code>, then the module creates the team if it does not already exist.</p>
      <p>If the team already exists, then the module updates its state.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">absent</span></p></li>
        <li><p><span class="ansible-option-default-bold">present</span> <span class="ansible-option-default">← (default)</span></p></li>
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
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-default-bold">yes</span> <span class="ansible-option-default">← (default)</span></p></li>
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
   - To synchronize teams with LDAP groups, see the M(quay_team_ldap) module.
   - Supports \ :literal:`check\_mode`\ .
   - The token that you provide in \ :emphasis:`quay\_token`\  must have the "Administer Organization" and "Administer User" permissions.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Ensure team operators exists in the production organization
      herve4m.quay.quay_team:
        name: operators
        organization: production
        description: |
            # Operation Team

            * Operators can create repositories
            * Operators can store their images in those repositories
        role: creator
        members:
          - lvasquez
          - dwilde
          - production+automationrobot
        append: false
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure team developers does not exist in the production organization
      herve4m.quay.quay_team:
        name: developers
        organization: production
        state: absent
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure team administrators has no members
      herve4m.quay.quay_team:
        name: administrators
        organization: production
        members: []
        append: false
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure team operators has additional members
      herve4m.quay.quay_team:
        name: operators
        organization: production
        members:
          - jziglar
          - chorwitz
        append: true
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

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/herve4m/quay-collection/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/herve4m/quay-collection" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

