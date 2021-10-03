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

.. _ansible_collections.herve4m.quay.quay_notification_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_notification -- Manage Red Hat Quay repository notifications
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.1).

    To install it use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_notification`.

.. version_added

.. versionadded:: 0.0.1 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create and delete repository notifications.


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
                    <div class="ansibleOptionAnchor" id="parameter-config"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Configuration parameters for the notification method.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/email"></div>
                    <b>email</b>
                    <a class="ansibleOptionLink" href="#parameter-config/email" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Destination email address.</div>
                                            <div>Required by the email notification method.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/flow_api_token"></div>
                    <b>flow_api_token</b>
                    <a class="ansibleOptionLink" href="#parameter-config/flow_api_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>API token required for the Flowdock notification method.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-config/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the account, team, or organization. Robot accounts are not allowed.</div>
                                            <div>Required by the Quay Notification method.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/notification_token"></div>
                    <b>notification_token</b>
                    <a class="ansibleOptionLink" href="#parameter-config/notification_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Notification token required for the HipChat notification method.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/room_id"></div>
                    <b>room_id</b>
                    <a class="ansibleOptionLink" href="#parameter-config/room_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Chat room ID required for the HipChat notification method.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/template"></div>
                    <b>template</b>
                    <a class="ansibleOptionLink" href="#parameter-config/template" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>JSON data for the body content of the webhook POST method.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-config/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>user</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>team</li>
                                                                                                                                                                                                <li>org</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the type of the account defined in <em>name</em>.</div>
                                            <div>Only applies to the Quay Notification method.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config/url"></div>
                    <b>url</b>
                    <a class="ansibleOptionLink" href="#parameter-config/url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Webhook URL for the Slack method or POST URL for the webhook POST method.</div>
                                                        </td>
            </tr>

                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-event"></div>
                    <b>event</b>
                    <a class="ansibleOptionLink" href="#parameter-event" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>repo_push</li>
                                                                                                                                                                                                <li>build_failure</li>
                                                                                                                                                                                                <li>build_queued</li>
                                                                                                                                                                                                <li>build_start</li>
                                                                                                                                                                                                <li>build_success</li>
                                                                                                                                                                                                <li>build_cancelled</li>
                                                                                                                                                                                                <li>vulnerability_found</li>
                                                                                                                                                                                                <li>repo_mirror_sync_started</li>
                                                                                                                                                                                                <li>repo_mirror_sync_success</li>
                                                                                                                                                                                                <li>repo_mirror_sync_failed</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Event that triggers the notification.</div>
                                            <div>Depending of the activated Quay components, not all events might be available on your system.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-method"></div>
                    <b>method</b>
                    <a class="ansibleOptionLink" href="#parameter-method" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>email</li>
                                                                                                                                                                                                <li>flowdock</li>
                                                                                                                                                                                                <li>hipchat</li>
                                                                                                                                                                                                <li>quay_notification</li>
                                                                                                                                                                                                <li>slack</li>
                                                                                                                                                                                                <li>webhook</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Notification method. Each method requires a specific set of options that you define by using the <em>config</em> parameter.</div>
                                            <div>The email notification method is only available on Quay installations where the mailing capability has been activated.</div>
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
                                            <div>The regular expression to search in the title of the existing notifications. This does not have to match the entire title.</div>
                                            <div>The module uses that regular expression to select the notifications to process.</div>
                                            <div>For <code>state=present</code>, the module resets the failure counter (if <em>reset_failcount</em> is <code>true</code>) or initiates a test (if <em>test</em> is <code>true</code>) of all the matching notifications.</div>
                                            <div>For <code>state=absent</code>, the module deletes all the notifications that match.</div>
                                            <div>Uses Python regular expressions. See <a href='https://docs.python.org/3/library/re.html'>https://docs.python.org/3/library/re.html</a>.</div>
                                            <div>Mutually exclusive with <em>search_string</em>.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: regex</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-repository"></div>
                    <b>repository</b>
                    <a class="ansibleOptionLink" href="#parameter-repository" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the repository which contains the notifications to manage. The format for the name is <code>namespace</code>/<code>shortname</code>. The namespace can be an organization or a personal namespace.</div>
                                            <div>If you omit the namespace part in the name, then the module looks for the repository in your personal namespace.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-reset_failcount"></div>
                    <b>reset_failcount</b>
                    <a class="ansibleOptionLink" href="#parameter-reset_failcount" title="Permalink to this option"></a>
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
                                            <div>Reset the notification failure counter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>The literal string to search in the title of the existing notifications. This does not have to match the entire line.</div>
                                            <div>For <code>state=present</code>, the module resets the failure counter (if <em>reset_failcount</em> is <code>true</code>) or initiates a test (if <em>test</em> is <code>true</code>) of all the matching notifications.</div>
                                            <div>For <code>state=absent</code>, the module deletes all the notifications that match.</div>
                                            <div>Mutually exclusive with <em>regexp</em>.</div>
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
                                            <div>If <code>absent</code>, then the module deletes the notification.</div>
                                            <div>The module uses the <em>title</em>, <em>regex</em>, or <em>search_string</em> parameters to select the notifications to process. You can also omit those parameters and use instead the <em>event</em> and <em>method</em> options to select all the notifications triggered by a specific event or using a specific method.</div>
                                            <div>If <code>present</code>, then the module creates the notification if it does not already exist.</div>
                                            <div>If the notification already exists and <em>reset_failcount</em> or <em>test</em> are set, then the module resets the failure counter or initiates a test of the notification.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-test"></div>
                    <b>test</b>
                    <a class="ansibleOptionLink" href="#parameter-test" title="Permalink to this option"></a>
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
                                            <div>Initiate a test of the notification.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-title"></div>
                    <b>title</b>
                    <a class="ansibleOptionLink" href="#parameter-title" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Notification title.</div>
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
                        </table>
    <br/>

.. Attributes


.. Notes

Notes
-----

.. note::
   - Supports ``check_mode``.
   - The token that you provide in *quay_token* must have the "Administer Repositories" and "Create Repositories" permissions.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja


    - name: Ensure notification of type Quay Notification exists
      herve4m.quay.quay_notification:
        repository: production/smallimage
        title: Test Quay Notification on image push
        event: repo_push
        method: quay_notification
        config:
          name: operators
          type: team
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Ensure notification of type Slack exists
      herve4m.quay.quay_notification:
        repository: production/smallimage
        title: Notify image push to Slack
        event: repo_push
        method: slack
        config:
          url: https://hooks.slack.com/services/XXX/YYY/ZZZ
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Test Slack notification
      herve4m.quay.quay_notification:
        repository: production/smallimage
        title: Notify image push to Slack
        test: true
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Reset the failure counter for the Quay Notification
      herve4m.quay.quay_notification:
        repository: production/smallimage
        regex: "Quay\\s+Notification\\s"
        reset_failcount: true
        state: present
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Delete all the notifications triggered by canceled builds
      herve4m.quay.quay_notification:
        repository: production/smallimage
        event: build_cancelled
        state: absent
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7

    - name: Delete all the notifications where the title includes "Test"
      herve4m.quay.quay_notification:
        repository: production/smallimage
        search_string: Test
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
