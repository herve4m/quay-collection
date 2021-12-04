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

.. _ansible_collections.herve4m.quay.quay_repository_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_repository -- Manage Red Hat Quay repositories
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.5).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_repository`.

.. version_added

.. versionadded:: 0.0.1 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, delete, and update repositories in Red Hat Quay.


.. Aliases


.. Requirements


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
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
                                            <div>If <code>yes</code>, then add the permission defined in <em>perms</em> to the repository.</div>
                                            <div>If <code>no</code>, then the module sets the permissions specified in <em>perms</em>, removing all others permissions from the repository.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>Text in Markdown format that describes the repository.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>Name of the repository to create, remove, or modify. The format for the name is <code>namespace</code>/<code>shortname</code>. The namespace can be an organization or a personal namespace.</div>
                                            <div>The name must be in lowercase and must not contain white spaces.</div>
                                            <div>If you omit the namespace part in the name, then the module uses your personal namespace.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-perms"></div>
                    <b>perms</b>
                    <a class="ansibleOptionLink" href="#parameter-perms" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User, robot, and team permissions to associate with the repository.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-perms/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-perms/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the account. The format for robot accounts is <code>namespace</code>+<code>shortrobotname</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-perms/role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#parameter-perms/role" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>read</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>write</li>
                                                                                                                                                                                                <li>admin</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of permission to grant.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-perms/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-perms/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>user</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>team</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the type of the account. Choose <code>user</code> for both user and robot accounts.</div>
                                                        </td>
            </tr>

                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-repo_state"></div>
                    <b>repo_state</b>
                    <a class="ansibleOptionLink" href="#parameter-repo_state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NORMAL</li>
                                                                                                                                                                                                <li>READ_ONLY</li>
                                                                                                                                                                                                <li>MIRROR</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If <code>NORMAL</code>, then the repository is in the default state (read/write).</div>
                                            <div>If <code>READ_ONLY</code>, then the repository is read-only.</div>
                                            <div>If <code>MIRROR</code>, then the repository is a mirror and you can configure it by using the M(quay_repository_mirror) module.</div>
                                            <div>You must enable the mirroring capability of your Quay installation to use this <em>repo_state</em> parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-star"></div>
                    <b>star</b>
                    <a class="ansibleOptionLink" href="#parameter-star" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If <code>yes</code>, then add a star to the repository. If <code>no</code>, then remove the star.</div>
                                            <div>To star or unstar a repository you must provide the <em>quay_token</em> parameter to authenticate. If you are not authenticated, then the module ignores the <em>star</em> parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>If <code>absent</code>, then the module deletes the repository.</div>
                                            <div>The module does not fail if the repository does not exist because the state is already as expected.</div>
                                            <div>If <code>present</code>, then the module creates the repository if it does not already exist.</div>
                                            <div>If the repository already exists, then the module updates its state.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-visibility"></div>
                    <b>visibility</b>
                    <a class="ansibleOptionLink" href="#parameter-visibility" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>public</li>
                                                                                                                                                                                                <li>private</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If <code>public</code>, then anyone can pull images from the repository.</div>
                                            <div>If <code>private</code>, then nobody can access the repository and you need to explicitly grant access to users, robots, and teams.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


.. Notes

Notes
-----

.. note::
   - You must enable the mirroring capability of your Quay installation (``FEATURE_REPO_MIRROR`` in ``config.yaml``) to use the *repo_state* parameter.
   - Supports ``check_mode``.
   - The token that you provide in *quay_token* must have the "Administer Repositories" and "Create Repositories" permissions.

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

    - name: Ensure the repository has a star
      herve4m.quay.quay_repository:
        name: production/smallimage
        star: true
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



.. Parsing errors
