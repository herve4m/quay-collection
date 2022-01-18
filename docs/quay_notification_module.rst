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

.. _ansible_collections.herve4m.quay.quay_notification_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_notification -- Manage Red Hat Quay repository notifications
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.9).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

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
      <div class="ansibleOptionAnchor" id="parameter-config"></div>
      <p class="ansible-option-title"><strong>config</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Configuration parameters for the notification method.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/email"></div>
      <p class="ansible-option-title"><strong>email</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/email" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Destination email address.</p>
      <p>Required by the email notification method.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/flow_api_token"></div>
      <p class="ansible-option-title"><strong>flow_api_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/flow_api_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>API token required for the Flowdock notification method.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the account, team, or organization. Robot accounts are not allowed.</p>
      <p>Required by the Quay Notification method.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/notification_token"></div>
      <p class="ansible-option-title"><strong>notification_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/notification_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Notification token required for the HipChat notification method.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/room_id"></div>
      <p class="ansible-option-title"><strong>room_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/room_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Chat room ID required for the HipChat notification method.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/template"></div>
      <p class="ansible-option-title"><strong>template</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/template" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>JSON data for the body content of the webhook POST method.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Specifies the type of the account defined in <em>name</em>.</p>
      <p>Only applies to the Quay Notification method.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">user</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">team</span></p></li>
        <li><p><span class="ansible-option-choices-entry">org</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-config/url"></div>
      <p class="ansible-option-title"><strong>url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Webhook URL for the Slack method or POST URL for the webhook POST method.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-event"></div>
      <p class="ansible-option-title"><strong>event</strong></p>
      <a class="ansibleOptionLink" href="#parameter-event" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Event that triggers the notification.</p>
      <p>Depending of the activated Quay components, not all events might be available on your system.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">repo_push</span></p></li>
        <li><p><span class="ansible-option-choices-entry">build_failure</span></p></li>
        <li><p><span class="ansible-option-choices-entry">build_queued</span></p></li>
        <li><p><span class="ansible-option-choices-entry">build_start</span></p></li>
        <li><p><span class="ansible-option-choices-entry">build_success</span></p></li>
        <li><p><span class="ansible-option-choices-entry">build_cancelled</span></p></li>
        <li><p><span class="ansible-option-choices-entry">vulnerability_found</span></p></li>
        <li><p><span class="ansible-option-choices-entry">repo_mirror_sync_started</span></p></li>
        <li><p><span class="ansible-option-choices-entry">repo_mirror_sync_success</span></p></li>
        <li><p><span class="ansible-option-choices-entry">repo_mirror_sync_failed</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-method"></div>
      <p class="ansible-option-title"><strong>method</strong></p>
      <a class="ansibleOptionLink" href="#parameter-method" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Notification method. Each method requires a specific set of options that you define by using the <em>config</em> parameter.</p>
      <p>The email notification method is only available on Quay installations where the mailing capability has been activated.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">email</span></p></li>
        <li><p><span class="ansible-option-choices-entry">flowdock</span></p></li>
        <li><p><span class="ansible-option-choices-entry">hipchat</span></p></li>
        <li><p><span class="ansible-option-choices-entry">quay_notification</span></p></li>
        <li><p><span class="ansible-option-choices-entry">slack</span></p></li>
        <li><p><span class="ansible-option-choices-entry">webhook</span></p></li>
      </ul>
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
  <tr class="row-odd">
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
      <p>The regular expression to search in the title of the existing notifications. This does not have to match the entire title.</p>
      <p>The module uses that regular expression to select the notifications to process.</p>
      <p>For <code class='docutils literal notranslate'>state=present</code>, the module resets the failure counter (if <em>reset_failcount</em> is <code class='docutils literal notranslate'>true</code>) or initiates a test (if <em>test</em> is <code class='docutils literal notranslate'>true</code>) of all the matching notifications.</p>
      <p>For <code class='docutils literal notranslate'>state=absent</code>, the module deletes all the notifications that match.</p>
      <p>Uses Python regular expressions. See <a href='https://docs.python.org/3/library/re.html'>https://docs.python.org/3/library/re.html</a>.</p>
      <p>Mutually exclusive with <em>search_string</em>.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-repository"></div>
      <p class="ansible-option-title"><strong>repository</strong></p>
      <a class="ansibleOptionLink" href="#parameter-repository" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the repository which contains the notifications to manage. The format for the name is <code class='docutils literal notranslate'>namespace</code>/<code class='docutils literal notranslate'>shortname</code>. The namespace can be an organization or a personal namespace.</p>
      <p>If you omit the namespace part in the name, then the module looks for the repository in your personal namespace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-reset_failcount"></div>
      <p class="ansible-option-title"><strong>reset_failcount</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reset_failcount" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Reset the notification failure counter.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">no</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
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
      <p>The literal string to search in the title of the existing notifications. This does not have to match the entire line.</p>
      <p>For <code class='docutils literal notranslate'>state=present</code>, the module resets the failure counter (if <em>reset_failcount</em> is <code class='docutils literal notranslate'>true</code>) or initiates a test (if <em>test</em> is <code class='docutils literal notranslate'>true</code>) of all the matching notifications.</p>
      <p>For <code class='docutils literal notranslate'>state=absent</code>, the module deletes all the notifications that match.</p>
      <p>Mutually exclusive with <em>regexp</em>.</p>
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
      <p>If <code class='docutils literal notranslate'>absent</code>, then the module deletes the notification.</p>
      <p>The module uses the <em>title</em>, <em>regex</em>, or <em>search_string</em> parameters to select the notifications to process. You can also omit those parameters and use instead the <em>event</em> and <em>method</em> options to select all the notifications triggered by a specific event or using a specific method.</p>
      <p>If <code class='docutils literal notranslate'>present</code>, then the module creates the notification if it does not already exist.</p>
      <p>If the notification already exists and <em>reset_failcount</em> or <em>test</em> are set, then the module resets the failure counter or initiates a test of the notification.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">absent</span></p></li>
        <li><p><span class="ansible-option-default-bold">present</span> <span class="ansible-option-default">← (default)</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-test"></div>
      <p class="ansible-option-title"><strong>test</strong></p>
      <a class="ansibleOptionLink" href="#parameter-test" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Initiate a test of the notification.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">no</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-title"></div>
      <p class="ansible-option-title"><strong>title</strong></p>
      <a class="ansibleOptionLink" href="#parameter-title" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Notification title.</p>
    </div></td>
  </tr>
  <tr class="row-even">
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
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-vulnerability_level"></div>
      <p class="ansible-option-title"><strong>vulnerability_level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vulnerability_level" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Only used when <em>event</em> is <code class='docutils literal notranslate'>vulnerability_found</code>.</p>
      <p>The notification is triggered when the vulnerability has a level equal or higher to the level you define is <em>vulnerability_level</em>.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">critical</span></p></li>
        <li><p><span class="ansible-option-choices-entry">high</span></p></li>
        <li><p><span class="ansible-option-choices-entry">medium</span></p></li>
        <li><p><span class="ansible-option-choices-entry">low</span></p></li>
        <li><p><span class="ansible-option-choices-entry">negligible</span></p></li>
        <li><p><span class="ansible-option-choices-entry">unknown</span></p></li>
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
   - The token that you provide in \ :emphasis:`quay\_token`\  must have the "Administer Repositories" and "Create Repositories" permissions.

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

    # You must enable the security scanner capability of your Quay installation
    # to use the vulnerability_found event.
    - name: Ensure notification of type webhook exists
      herve4m.quay.quay_notification:
        repository: production/smallimage
        title: Webhook notification on critical image vulnerability
        event: vulnerability_found
        vulnerability_level: critical
        method: webhook
        config:
          url: https://webhook.example.com/webhook/12345
          template: "{{ lookup('file', 'post.json') | string }}"
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

