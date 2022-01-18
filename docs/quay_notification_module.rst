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

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config:

      .. rst-class:: ansible-option-title

      **config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Configuration parameters for the notification method.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/email"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/email:

      .. rst-class:: ansible-option-title

      **email**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/email" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Destination email address.

      Required by the email notification method.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/flow_api_token"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/flow_api_token:

      .. rst-class:: ansible-option-title

      **flow_api_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/flow_api_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      API token required for the Flowdock notification method.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/name"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Name of the account, team, or organization. Robot accounts are not allowed.

      Required by the Quay Notification method.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/notification_token"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/notification_token:

      .. rst-class:: ansible-option-title

      **notification_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/notification_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Notification token required for the HipChat notification method.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/room_id"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/room_id:

      .. rst-class:: ansible-option-title

      **room_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/room_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Chat room ID required for the HipChat notification method.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/template"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/template:

      .. rst-class:: ansible-option-title

      **template**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/template" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      JSON data for the body content of the webhook POST method.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/type"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Specifies the type of the account defined in \ :emphasis:`name`\ .

      Only applies to the Quay Notification method.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`user` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`team`
      - :ansible-option-choices-entry:`org`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config/url"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-config/url:

      .. rst-class:: ansible-option-title

      **url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config/url" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Webhook URL for the Slack method or POST URL for the webhook POST method.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-event"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-event:

      .. rst-class:: ansible-option-title

      **event**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-event" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Event that triggers the notification.

      Depending of the activated Quay components, not all events might be available on your system.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`repo\_push`
      - :ansible-option-choices-entry:`build\_failure`
      - :ansible-option-choices-entry:`build\_queued`
      - :ansible-option-choices-entry:`build\_start`
      - :ansible-option-choices-entry:`build\_success`
      - :ansible-option-choices-entry:`build\_cancelled`
      - :ansible-option-choices-entry:`vulnerability\_found`
      - :ansible-option-choices-entry:`repo\_mirror\_sync\_started`
      - :ansible-option-choices-entry:`repo\_mirror\_sync\_success`
      - :ansible-option-choices-entry:`repo\_mirror\_sync\_failed`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-method"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-method:

      .. rst-class:: ansible-option-title

      **method**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-method" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Notification method. Each method requires a specific set of options that you define by using the \ :emphasis:`config`\  parameter.

      The email notification method is only available on Quay installations where the mailing capability has been activated.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`email`
      - :ansible-option-choices-entry:`flowdock`
      - :ansible-option-choices-entry:`hipchat`
      - :ansible-option-choices-entry:`quay\_notification`
      - :ansible-option-choices-entry:`slack`
      - :ansible-option-choices-entry:`webhook`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quay_host"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-quay_host:

      .. rst-class:: ansible-option-title

      **quay_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-quay_host" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL for accessing the API. \ https://quay.example.com:8443\  for example.

      If you do not set the parameter, then the module uses the \ :literal:`QUAY\_HOST`\  environment variable.

      If you do no set the environment variable either, then the module uses the \ http://127.0.0.1\  URL.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"http://127.0.0.1"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quay_token"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-quay_token:

      .. rst-class:: ansible-option-title

      **quay_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-quay_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      OAuth access token for authenticating with the API.

      If you do not set the parameter, then the module tries the \ :literal:`QUAY\_TOKEN`\  environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-regexp"></div>
        <div class="ansibleOptionAnchor" id="parameter-regex"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-regexp:
      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-regex:

      .. rst-class:: ansible-option-title

      **regexp**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-regexp" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: regex`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The regular expression to search in the title of the existing notifications. This does not have to match the entire title.

      The module uses that regular expression to select the notifications to process.

      For \ :literal:`state=present`\ , the module resets the failure counter (if \ :emphasis:`reset\_failcount`\  is \ :literal:`true`\ ) or initiates a test (if \ :emphasis:`test`\  is \ :literal:`true`\ ) of all the matching notifications.

      For \ :literal:`state=absent`\ , the module deletes all the notifications that match.

      Uses Python regular expressions. See \ https://docs.python.org/3/library/re.html\ .

      Mutually exclusive with \ :emphasis:`search\_string`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-repository"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-repository:

      .. rst-class:: ansible-option-title

      **repository**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-repository" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the repository which contains the notifications to manage. The format for the name is \ :literal:`namespace`\ /\ :literal:`shortname`\ . The namespace can be an organization or a personal namespace.

      If you omit the namespace part in the name, then the module looks for the repository in your personal namespace.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-reset_failcount"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-reset_failcount:

      .. rst-class:: ansible-option-title

      **reset_failcount**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-reset_failcount" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reset the notification failure counter.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-search_string"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-search_string:

      .. rst-class:: ansible-option-title

      **search_string**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-search_string" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The literal string to search in the title of the existing notifications. This does not have to match the entire line.

      For \ :literal:`state=present`\ , the module resets the failure counter (if \ :emphasis:`reset\_failcount`\  is \ :literal:`true`\ ) or initiates a test (if \ :emphasis:`test`\  is \ :literal:`true`\ ) of all the matching notifications.

      For \ :literal:`state=absent`\ , the module deletes all the notifications that match.

      Mutually exclusive with \ :emphasis:`regexp`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`absent`\ , then the module deletes the notification.

      The module uses the \ :emphasis:`title`\ , \ :emphasis:`regex`\ , or \ :emphasis:`search\_string`\  parameters to select the notifications to process. You can also omit those parameters and use instead the \ :emphasis:`event`\  and \ :emphasis:`method`\  options to select all the notifications triggered by a specific event or using a specific method.

      If \ :literal:`present`\ , then the module creates the notification if it does not already exist.

      If the notification already exists and \ :emphasis:`reset\_failcount`\  or \ :emphasis:`test`\  are set, then the module resets the failure counter or initiates a test of the notification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`absent`
      - :ansible-option-default-bold:`present` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-test"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-test:

      .. rst-class:: ansible-option-title

      **test**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-test" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Initiate a test of the notification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-title"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-title:

      .. rst-class:: ansible-option-title

      **title**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-title" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Notification title.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
        <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-validate_certs:
      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-verify_ssl:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: verify_ssl`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to allow insecure connections to the API.

      If \ :literal:`no`\ , then the module does not validate SSL certificates.

      If you do not set the parameter, then the module tries the \ :literal:`QUAY\_VERIFY\_SSL`\  environment variable (\ :literal:`yes`\ , \ :literal:`1`\ , and \ :literal:`True`\  mean yes, and \ :literal:`no`\ , \ :literal:`0`\ , \ :literal:`False`\ , and no value mean no).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-default-bold:`yes` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vulnerability_level"></div>

      .. _ansible_collections.herve4m.quay.quay_notification_module__parameter-vulnerability_level:

      .. rst-class:: ansible-option-title

      **vulnerability_level**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vulnerability_level" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Only used when \ :emphasis:`event`\  is \ :literal:`vulnerability\_found`\ .

      The notification is triggered when the vulnerability has a level equal or higher to the level you define is \ :emphasis:`vulnerability\_level`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`critical`
      - :ansible-option-choices-entry:`high`
      - :ansible-option-choices-entry:`medium`
      - :ansible-option-choices-entry:`low`
      - :ansible-option-choices-entry:`negligible`
      - :ansible-option-choices-entry:`unknown`

      .. raw:: html

        </div>


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

