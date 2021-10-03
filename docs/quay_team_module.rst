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

.. _ansible_collections.herve4m.quay.quay_team_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_team -- Manage Red Hat Quay teams
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.1).

    To install it use: :code:`ansible-galaxy collection install herve4m.quay`.

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

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-append"></div>
                    <b>append</b>
                    <a class="ansibleOptionLink" href="#parameter-append" title="Permalink to this option"></a>
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
                                            <div>If <code>yes</code>, then add the users specified in <em>members</em> to the team.</div>
                                            <div>If <code>no</code>, then the module sets the team members to users specified in <em>members</em>, removing all others users from the team.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Text in Markdown format that describes the team.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-members"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-members" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of the user or robot accounts in the team. Use the syntax <code>organization</code>+<code>robotshortname</code> for robot accounts.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the team to create, remove, or modify.</div>
                                            <div>The name must be in lowercase, must not contain white spaces, must not start by a digit, and must be at least two characters long.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-organization"></div>
                    <b>organization</b>
                    <a class="ansibleOptionLink" href="#parameter-organization" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the organization for the team. That organization must exist.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>member</li>
                                                                                                                                                                                                <li>creator</li>
                                                                                                                                                                                                <li>admin</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Role of the team within the organization.</div>
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
                                            <div>If <code>absent</code>, then the module deletes the team.</div>
                                            <div>The module does not fail if the team does not exist because the state is already as expected.</div>
                                            <div>If <code>present</code>, then the module creates the team if it does not already exist.</div>
                                            <div>If the team already exists, then the module updates its state.</div>
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
   - The token that you provide in *quay_token* must have the "Administer Organization" and "Administer User" permissions.

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

    - name: Ensure team operators has additionnal members
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



.. Parsing errors
