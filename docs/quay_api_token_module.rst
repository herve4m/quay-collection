
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.11.0

.. Anchors

.. _ansible_collections.herve4m.quay.quay_api_token_module:

.. Anchors: short name for ansible.builtin

.. Title

herve4m.quay.quay_api_token module -- Create OAuth access tokens for accessing the Quay Container Registry API
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/ui/repo/published/herve4m/quay/>`_ (version 1.3.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_api_token`.

.. version_added

.. rst-class:: ansible-version-added

New in herve4m.quay 0.0.12

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
      <p>See the <a href='../../herve4m/quay/quay_application_module.html' class='module'>herve4m.quay.quay_application</a> module to create an application object and to retrieve the associated client ID.</p>
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
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The password to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_PASSWORD</code> environment variable.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_username"></div>
      <p class="ansible-option-title"><strong>quay_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The username to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_USERNAME</code> environment variable.</p>
    </div></td>
  </tr>
  <tr class="row-even">
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
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;org:admin&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;repo:admin&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;repo:create&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>&#34;repo:read&#34;</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;repo:write&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;super:user&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;user:admin&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;user:read&#34;</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;all&#34;</code></p></li>
      </ul>

      <p class="ansible-option-line"><strong class="ansible-option-default-bold">Default:</strong> <code class="ansible-value literal notranslate ansible-option-default">[&#34;repo:read&#34;]</code></p>
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
   - The generated OAuth access token acts on behalf of the user account you use with the module (in \ :emphasis:`quay\_username`\ ).
   - The module is not idempotent. Every time you run it, an additional OAuth access token is produced. The other OAuth access tokens stay valid.
   - You cannot delete OAuth access tokens.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Generate an OAuth access token
      herve4m.quay.quay_api_token:
        quay_username: lvasquez
        quay_password: vs9mrD55NP
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
        quay_username: jziglar
        quay_password: i45fR38GhY
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
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;CywbRGkh1ttYkRRy9VL0Aw0yU9q7J62vIeo7WCFw&#34;</code></p>
    </div></td>
  </tr>
  </tbody>
  </table>



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

