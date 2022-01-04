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

.. _ansible_collections.herve4m.quay.quay_first_user_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_first_user -- Create the first user account
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.8).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_first_user`.

.. version_added

.. versionadded:: 0.0.7 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create the first user just after installing Red Hat Quay.


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
                    <div class="ansibleOptionAnchor" id="parameter-create_token"></div>
                    <b>create_token</b>
                    <a class="ansibleOptionLink" href="#parameter-create_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If <code>yes</code>, then an OAuth access token is created and returned. You can use that returned token with the other Quay modules, by setting it in the <em>quay_token</em> parameter.</div>
                                            <div>If <code>no</code>, then no access token is created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-email"></div>
                    <b>email</b>
                    <a class="ansibleOptionLink" href="#parameter-email" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User&#x27;s email address.</div>
                                            <div>If you have enabled the mailing capability of your Quay installation, then this <em>email</em> parameter is mandatory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User&#x27;s password as a clear string.</div>
                                            <div>The password must be at least eight characters long and must not contain white spaces.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the user account to create.</div>
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
   - The module requires Red Hat Quay 3.6 or later.
   - To use the module, you must enable the first user creation feature of your Quay installation (``FEATURE_USER_INITIALIZE`` in ``config.yaml``).
   - You must also use the internal database of your Quay installation for authentication (``AUTHENTICATION_TYPE`` to ``Database`` in ``config.yaml``).
   - Use the module just after installing Quay, when the database is empty. The module fails if user accounts are already defined in the database.
   - Supports ``check_mode``.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja


    - name: Ensure the initial user exists
      herve4m.quay.quay_first_user:
        username: admin
        email: admin@example.com
        password: S6tGwo13
        create_token: true
        quay_host: https://quay.example.com
      register: result

    - debug:
        msg: "Access token: {{ result['access_token'] }}"




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-access_token"></div>
                    <b>access_token</b>
                    <a class="ansibleOptionLink" href="#return-access_token" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>only when you set the <em>create_token</em> parameter to <code>yes</code></td>
                <td>
                                            <div>The access token that you can use for subsequent module calls.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">W2YX0V838JZ5FHHUH82Q25FZZMRX8YTB1MTN56P3</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-email"></div>
                    <b>email</b>
                    <a class="ansibleOptionLink" href="#return-email" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>User&#x27;s email address.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">admin@example.com</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-encrypted_password"></div>
                    <b>encrypted_password</b>
                    <a class="ansibleOptionLink" href="#return-encrypted_password" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Encrypted user&#x27;s password.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">/pbR5LPYx4Y3w/SSf2dAwNxCCNgwmmZk+x04TKn6xEKL2At5wblOy7wA1tNZEhRc</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#return-username" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Name of the created user account.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">admin</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Herve Quatremain (@herve4m)



.. Parsing errors
