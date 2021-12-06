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

.. Anchors

.. _ansible_collections.herve4m.quay.quay_message_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_message -- Manage Red Hat Quay global messages
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.6).

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

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-content"></div>
                    <b>content</b>
                    <a class="ansibleOptionLink" href="#parameter-content" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Text of the message to display on each web UI page.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-format"></div>
                    <b>format</b>
                    <a class="ansibleOptionLink" href="#parameter-format" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>markdown</li>
                                                                                                                                                                                                <li>plain</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Format of the text in <em>content</em>.</div>
                                            <div>If you do not set this parameter, then the module uses the <code>plain</code> format.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: media_type</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-quay_host"></div>
                    <b>quay_host</b>
                    <a class="ansibleOptionLink" href="#parameter-quay_host" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"http://127.0.0.1"</div>
                                    </td>
                                                                <td>
                                            <div>URL for accessing the API. <a href='https://quay.example.com:8443'>https://quay.example.com:8443</a> for example.</div>
                                            <div>If you do not set the parameter, then the module uses the <code>QUAY_HOST</code> environment variable.</div>
                                            <div>If you do no set the environment variable either, then the module uses the <a href='http://127.0.0.1'>http://127.0.0.1</a> URL.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-quay_token"></div>
                    <b>quay_token</b>
                    <a class="ansibleOptionLink" href="#parameter-quay_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Token for authenticating with the API.</div>
                                            <div>If you do not set the parameter, then the module tries the <code>QUAY_TOKEN</code> environment variable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-regexp"></div>
                    <b>regexp</b>
                    <a class="ansibleOptionLink" href="#parameter-regexp" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The regular expression to look for in the existing messages. This does not have to match an entire line.</div>
                                            <div>For <code>state=present</code>, if several messages match then the module updates one and deletes the others.</div>
                                            <div>For <code>state=absent</code>, the module deletes all the messages that match.</div>
                                            <div>Uses Python regular expressions. See <a href='https://docs.python.org/3/library/re.html'>https://docs.python.org/3/library/re.html</a>.</div>
                                            <div>Mutually exclusive with <em>search_string</em>.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: regex</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-search_severity"></div>
                    <b>search_severity</b>
                    <a class="ansibleOptionLink" href="#parameter-search_severity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>info</li>
                                                                                                                                                                                                <li>warning</li>
                                                                                                                                                                                                <li>error</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Search messages by their severity level.</div>
                                            <div>If you also set <em>search_string</em>, <em>regexp</em>, or <em>content</em>, messages must match all those criteria.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-search_string"></div>
                    <b>search_string</b>
                    <a class="ansibleOptionLink" href="#parameter-search_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The literal string to look for in the existing messages. This does not have to match an entire line.</div>
                                            <div>For <code>state=present</code>, if several messages match then the module updates one and deletes the others.</div>
                                            <div>For <code>state=absent</code>, the module deletes all the messages that match.</div>
                                            <div>Mutually exclusive with <em>regexp</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-severity"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-severity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>info</li>
                                                                                                                                                                                                <li>warning</li>
                                                                                                                                                                                                <li>error</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Severity of the message.</div>
                                            <div>If you do not set this parameter, then the module creates the message with the <code>info</code> severity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>absent</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If <code>absent</code>, then the module deletes all the messages which content matches <em>search_string</em>, <em>regexp</em>, <em>content</em>, or <em>search_severity</em>.</div>
                                            <div>If <code>present</code>, then the module creates the message if it does not already exist (that is, if no message matches <em>search_string</em>, <em>regexp</em>, or <em>content</em>). Is several messages match, only one is updated and the others are deleted.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to allow insecure connections to the API.</div>
                                            <div>If <code>no</code>, then the module does not validate SSL certificates.</div>
                                            <div>If you do not set the parameter, then the module tries the <code>QUAY_VERIFY_SSL</code> environment variable (<code>yes</code>, <code>1</code>, and <code>True</code> mean yes, and <code>no</code>, <code>0</code>, <code>False</code>, and no value mean no).</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: verify_ssl</div>
                                    </td>
            </tr>
                        </table>
    <br/>

.. Attributes


.. Notes

Notes
-----

.. note::
   - Supports ``check_mode``.
   - The token that you provide in *quay_token* must have the "Super User Access" permission.

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
