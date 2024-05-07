
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.11.0

.. Anchors

.. _ansible_collections.herve4m.quay.quay_docker_token_module:

.. Anchors: short name for ansible.builtin

.. Title

herve4m.quay.quay_docker_token module -- Manage tokens for accessing Quay Container Registry repositories
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/ui/repo/published/herve4m/quay/>`_ (version 1.3.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_docker_token`.

.. version_added

.. rst-class:: ansible-version-added

New in herve4m.quay 0.0.11

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create or delete tokens for client tools to access repositories.
- For example, the \ :literal:`docker`\ , \ :literal:`podman`\ , and \ :literal:`skopeo`\  command-line tools can use such tokens.
- Kubernetes can also use those tokens, declared is Kubernetes secret objects, to pull images and deploy pods.
- Using tokens is an alternative to using your user login and password.
- The tokens you create are for the user account you are logged in. You cannot create tokens for other users, even if you are logged in with a super user account.


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
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the token to create or delete.</p>
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
      <p>If <code class='docutils literal notranslate'>absent</code>, then the module deletes the token.</p>
      <p>The module does not fail if the token does not exist, because the state is already as expected.</p>
      <p>If <code class='docutils literal notranslate'>present</code>, then the module creates the token if it does not already exist.</p>
      <p>If the token already exists, then the module returns its details.</p>
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
  </tbody>
  </table>



.. Attributes


.. Notes

Notes
-----

.. note::
   - Supports \ :literal:`check\_mode`\ .
   - The tokens you create with this module are unrelated to OAUth access tokens that you use to access the Quay API.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Ensure the token exists for my account
      herve4m.quay.quay_docker_token:
        name: token_for_pull
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
      register: token_details

    - name: Ensure the image is pulled
      containers.podman.podman_image:
        name: quay.example.com/production/smallimage:v1.0.0
        username: "{{ token_details['username'] }}"
        password: "{{ token_details['token_code'] }}"

    - name: Ensure the token does not exist
      herve4m.quay.quay_docker_token:
        name: token_for_pull
        state: absent
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7




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
      <div class="ansibleOptionAnchor" id="return-auth_b64"></div>
      <p class="ansible-option-title"><strong>auth_b64</strong></p>
      <a class="ansibleOptionLink" href="#return-auth_b64" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Base64 encoding of the username and the token (<code class='docutils literal notranslate'>I(username</code>:<em>token_code</em>)).</p>
      <p>Some client configuration files, such as the <code class='docutils literal notranslate'>~/.docker/config.json</code> Docker configuration file, require that you provide the username and the token in that format.</p>
      <p>You can decode the string by using the <code class='docutils literal notranslate'>base64 --decode</code> command. See the <code class='docutils literal notranslate'>base64</code>(1) man page.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;JGFw...NzBK&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-created"></div>
      <p class="ansible-option-title"><strong>created</strong></p>
      <a class="ansibleOptionLink" href="#return-created" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Token creation date and time.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;Wed, 25 May 2022 12:46:41 -0000&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-dockerconfigjson_b64"></div>
      <p class="ansible-option-title"><strong>dockerconfigjson_b64</strong></p>
      <a class="ansibleOptionLink" href="#return-dockerconfigjson_b64" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Base64 encoding of the <code class='docutils literal notranslate'>~/.docker/config.json</code> configuration file.</p>
      <p>The <code class='docutils literal notranslate'>containers-auth.json</code>(5) man page describe the format of the file.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;ewog...Cn0=&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-expiration"></div>
      <p class="ansible-option-title"><strong>expiration</strong></p>
      <a class="ansibleOptionLink" href="#return-expiration" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Expiration date and time of the token.</p>
      <p>By default, tokens do not expire. In that case <em>expiration</em> is <code class='docutils literal notranslate'>null</code>.</p>
      <p>Your Quay administrator might have activated expiration by setting the <code class='docutils literal notranslate'>APP_SPECIFIC_TOKEN_EXPIRATION</code> directive in the <code class='docutils literal notranslate'>config.yaml</code> configuration file.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;Fri, 29 Apr 2023 13:31:05 -0000&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-last_accessed"></div>
      <p class="ansible-option-title"><strong>last_accessed</strong></p>
      <a class="ansibleOptionLink" href="#return-last_accessed" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Last date and time the token was used.</p>
      <p>If the token has not been used yet, then <em>last_accessed</em> is <code class='docutils literal notranslate'>null</code>.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;Wed, 25 May 2022 12:49:45 -0000&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#return-name" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the application token.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;my_push_token&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-token_code"></div>
      <p class="ansible-option-title"><strong>token_code</strong></p>
      <a class="ansibleOptionLink" href="#return-token_code" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Token to use as the password.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;OVKFT8YJBTQYG4Z30YHDOPJBU4M2VPMCQJ5IYW4BAQGZD8T5V70JORLJBJHFYVVFQ89K7&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-username"></div>
      <p class="ansible-option-title"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#return-username" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Username to use with client commands such as <code class='docutils literal notranslate'>docker</code> or <code class='docutils literal notranslate'>podman</code>.</p>
      <p>When you use a token with those commands, do not use your login name but use this username instead.</p>
      <p>For Quay, that username is always <code class='docutils literal notranslate'>$app</code>.</p>
      <p>Because the <code class='docutils literal notranslate'>$</code> character is a special shell character, you might have to protect it with a backslash or by using single quotation marks.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;$app&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-uuid"></div>
      <p class="ansible-option-title"><strong>uuid</strong></p>
      <a class="ansibleOptionLink" href="#return-uuid" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Internal ID of the application token.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;31b32343-e974-4f8c-bd9c-db5a0406f211&#34;</code></p>
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

