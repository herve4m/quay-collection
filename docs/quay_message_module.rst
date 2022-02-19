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

.. _ansible_collections.herve4m.quay.quay_message_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_message -- Manage Red Hat Quay global messages
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.11).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_message`.

.. version_added

.. versionadded:: 0.0.1 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, delete, and update global messages (message of the day) that display on the web UI pages.


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
      <div class="ansibleOptionAnchor" id="parameter-content"></div>
      <p class="ansible-option-title"><strong>content</strong></p>
      <a class="ansibleOptionLink" href="#parameter-content" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Text of the message to display on each web UI page.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-format"></div>
      <div class="ansibleOptionAnchor" id="parameter-media_type"></div>
      <p class="ansible-option-title"><strong>format</strong></p>
      <a class="ansibleOptionLink" href="#parameter-format" title="Permalink to this option"></a>
      <p class="ansible-option-type-line"><span class="ansible-option-aliases">aliases: media_type</p>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Format of the text in <em>content</em>.</p>
      <p>If you do not set this parameter, then the module uses the <code class='docutils literal notranslate'>plain</code> format.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">markdown</span></p></li>
        <li><p><span class="ansible-option-choices-entry">plain</span></p></li>
      </ul>
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
      <div class="ansibleOptionAnchor" id="parameter-quay_token"></div>
      <p class="ansible-option-title"><strong>quay_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>OAuth access token for authenticating with the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_TOKEN</code> environment variable.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-regexp"></div>
      <div class="ansibleOptionAnchor" id="parameter-regex"></div>
      <p class="ansible-option-title"><strong>regexp</strong></p>
      <a class="ansibleOptionLink" href="#parameter-regexp" title="Permalink to this option"></a>
      <p class="ansible-option-type-line"><span class="ansible-option-aliases">aliases: regex</p>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The regular expression to look for in the existing messages. This does not have to match an entire line.</p>
      <p>For <code class='docutils literal notranslate'>state=present</code>, if several messages match, then the module updates one and deletes the others.</p>
      <p>For <code class='docutils literal notranslate'>state=absent</code>, the module deletes all the messages that match.</p>
      <p>Uses Python regular expressions. See <a href='https://docs.python.org/3/library/re.html'>https://docs.python.org/3/library/re.html</a>.</p>
      <p>Mutually exclusive with <em>search_string</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-search_severity"></div>
      <p class="ansible-option-title"><strong>search_severity</strong></p>
      <a class="ansibleOptionLink" href="#parameter-search_severity" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Search messages by their severity level.</p>
      <p>If you also set <em>search_string</em>, <em>regexp</em>, or <em>content</em>, messages must match all those criteria.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">info</span></p></li>
        <li><p><span class="ansible-option-choices-entry">warning</span></p></li>
        <li><p><span class="ansible-option-choices-entry">error</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-search_string"></div>
      <p class="ansible-option-title"><strong>search_string</strong></p>
      <a class="ansibleOptionLink" href="#parameter-search_string" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The literal string to look for in the existing messages. This does not have to match an entire line.</p>
      <p>For <code class='docutils literal notranslate'>state=present</code>, if several messages match, then the module updates one and deletes the others.</p>
      <p>For <code class='docutils literal notranslate'>state=absent</code>, the module deletes all the messages that match.</p>
      <p>Mutually exclusive with <em>regexp</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-severity"></div>
      <p class="ansible-option-title"><strong>severity</strong></p>
      <a class="ansibleOptionLink" href="#parameter-severity" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Severity of the message.</p>
      <p>If you do not set this parameter, then the module creates the message with the <code class='docutils literal notranslate'>info</code> severity.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">info</span></p></li>
        <li><p><span class="ansible-option-choices-entry">warning</span></p></li>
        <li><p><span class="ansible-option-choices-entry">error</span></p></li>
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
      <p>If <code class='docutils literal notranslate'>absent</code>, then the module deletes all the messages which content matches <em>search_string</em>, <em>regexp</em>, <em>content</em>, or <em>search_severity</em>.</p>
      <p>If <code class='docutils literal notranslate'>present</code>, then the module creates the message if it does not already exist (that is, if no message matches <em>search_string</em>, <em>regexp</em>, or <em>content</em>). Is several messages match, only one is updated and the others are deleted.</p>
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
   - The token that you provide in \ :emphasis:`quay\_token`\  must have the "Super User Access" permission.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Ensure the message of the day is published
      herve4m.quay.quay_message:
        content: |
          # Information message

          Lorem **ipsum** dolor sit amet, `consectetur` adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua:

          * Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
            ut aliquip ex ea commodo consequat.
          *  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
             dolore eu fugiat nulla pariatur
        format: markdown
        severity: info
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure a message in plain text is published
      herve4m.quay.quay_message:
        content: System maintenance tomorrow at 6 AM
        format: plain
        severity: info
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the message severity is upgraded to warning
      herve4m.quay.quay_message:
        content: System maintenance tomorrow at 6 AM
        severity: warning
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the message content is updated
      herve4m.quay.quay_message:
        content: System maintenance tomorrow at 7 AM
        # Find the message to update by a matching string
        search_string: tomorrow at 6 AM
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the existing message as an error priority now
      herve4m.quay.quay_message:
        # Find the message to update by a matching string
        search_string: incididunt ut labore et dolore
        severity: error
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the warning message is removed
      herve4m.quay.quay_message:
        # Find the message to delete by its exact content
        content: System maintenance tomorrow at 7 AM
        state: absent
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the messages of the day are removed
      herve4m.quay.quay_message:
        # Find the messages to delete by a matching regular expression
        regexp: 'message\s+of\s+the\s+day'
        state: absent
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure the lorem ipsum error messages are removed
      herve4m.quay.quay_message:
        # Find the messages to delete by a matching string and severity
        search_string: lorem ipsum
        search_severity: error
        state: absent
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure all the warning messages are removed
      herve4m.quay.quay_message:
        search_severity: warning
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



.. Parsing errors

