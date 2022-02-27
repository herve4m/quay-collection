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

.. _ansible_collections.herve4m.quay.quay_api_token_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_api_token -- Create OAuth access tokens for accessing the Red Hat Quay API
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.13).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_api_token`.

.. version_added

.. versionadded:: 0.0.12 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create OAuth access tokens for authenticating with the API.


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
      <div class="ansibleOptionAnchor" id="parameter-client_id"></div>
      <p class="ansible-option-title"><strong>client_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The client ID associated with the OAuth application to use for generating the OAuth access token.</p>
      <p>See the M(quay_application) module to create an application object and to retrieve the associated client ID.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <p class="ansible-option-title"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The password to use for authentication against the API.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-rights"></div>
      <p class="ansible-option-title"><strong>rights</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rights" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of permissions to grant to the user account. <code class='docutils literal notranslate'>all</code> means all the permissions.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">org:admin</span></p></li>
        <li><p><span class="ansible-option-choices-entry">repo:admin</span></p></li>
        <li><p><span class="ansible-option-choices-entry">repo:create</span></p></li>
        <li><p><span class="ansible-option-default-bold">repo:read</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">repo:write</span></p></li>
        <li><p><span class="ansible-option-choices-entry">super:user</span></p></li>
        <li><p><span class="ansible-option-choices-entry">user:admin</span></p></li>
        <li><p><span class="ansible-option-choices-entry">user:read</span></p></li>
        <li><p><span class="ansible-option-choices-entry">all</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <p class="ansible-option-title"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The username to use for authentication against the API.</p>
      <p>The OAuth access token that the module generates acts on behalf of that user account.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>
      <p class="ansible-option-title"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p class="ansible-option-type-line"><span class="ansible-option-aliases">aliases: verify_ssl</p>
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
   - Supports \ :literal:`check\_mode`\ .
   - The module is not idempotent. Every time you run it, an additional OAuth access token is produced. The other OAuth access tokens stay valid.
   - You cannot delete OAuth access tokens.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Generate an OAuth access token
      herve4m.quay.quay_api_token:
        username: lvasquez
        password: vs9mrD55NP
        # The OAuth application must exist. See the following example that shows
        # how to create an organization and an application.
        client_id: PZ6F80R1LCVPGYNZGSZQ
        rights:
          - org:admin
          - user:admin
        quay_host: https://quay.example.com
      register: token_details

    - name: Display the new OAuth access token
      debug:
        msg: "The OAuth access token is: {{ token_details['access_token'] }}"

    # The following example creates an organization, an OAuth application, a user
    # account, and then generates an OAuth access token for that user account.
    # The OAuth access token of an existing super user is required to create the
    # organization, the application, and the user account.
    - name: Ensure the organization exists
      herve4m.quay.quay_organization:
        name: production
        email: prodlist@example.com
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the application extapp exists
      herve4m.quay.quay_application:
        organization: production
        name: extapp
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
      register: app_details

    - name: Ensure the user exists
      herve4m.quay.quay_user:
        username: jziglar
        password: i45fR38GhY
        email: jziglar@example.com
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Generate an OAuth access token for the user
      herve4m.quay.quay_api_token:
        username: jziglar
        password: i45fR38GhY
        client_id: "{{ app_details['client_id'] }}"
        rights:
          - all
        quay_host: https://quay.example.com
      register: token_details

    - name: Display the new OAuth access token
      debug:
        msg: "The OAuth access token is: {{ token_details['access_token'] }}"




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Key</p></th>
    <th class="head"><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-access_token"></div>
      <p class="ansible-option-title"><strong>access_token</strong></p>
      <a class="ansibleOptionLink" href="#return-access_token" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The OAuth access token.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "CywbRGkh1ttYkRRy9VL0Aw0yU9q7J62vIeo7WCFw"</p>
    </div></td>
  </tr>
  </tbody>
  </table>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Herve Quatremain (@herve4m)



.. Parsing errors

