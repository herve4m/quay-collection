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

.. _ansible_collections.herve4m.quay.quay_tag_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_tag_info -- Gather information about tags in a Red Hat Quay repository
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.9).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_tag_info`.

.. version_added

.. versionadded:: 0.0.1 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Gather information about the tags in a repository.


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
        <div class="ansibleOptionAnchor" id="parameter-only_active_tags"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__parameter-only_active_tags:

      .. rst-class:: ansible-option-title

      **only_active_tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-only_active_tags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`yes`\ , then the module only collects information on tags that have not expired. If \ :literal:`no`\ , then the module returns information on all the tags.

      You can identify expired tags (when \ :emphasis:`only\_active\_tags`\  is \ :literal:`no`\ ) in the returned data by inspecting the \ :literal:`end\_ts`\  or \ :literal:`expiration`\  tag attributes. Those attributes provide the expiration date.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quay_host"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__parameter-quay_host:

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

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__parameter-quay_token:

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
        <div class="ansibleOptionAnchor" id="parameter-repository"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__parameter-repository:

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

      Name of the repository that contains the tags to list. The format is \ :literal:`namespace`\ /\ :literal:`shortname`\ . The namespace can be an organization or a personal namespace.

      If you omit the namespace part, then the module looks for the repository in your personal namespace.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tag"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__parameter-tag:

      .. rst-class:: ansible-option-title

      **tag**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tag" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Gather information on that specific tag instead of returning data on all the tags in the repository.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
        <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__parameter-validate_certs:
      .. _ansible_collections.herve4m.quay.quay_tag_info_module__parameter-verify_ssl:

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


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Retrieve the tags in the production/smallimage repository
      herve4m.quay.quay_tag_info:
        repository: production/smallimage
        only_active_tags: true
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
      register: tags

    - name: Gather info on tag 0.1.2 of the testing image in my personal namespace
      herve4m.quay.quay_tag_info:
        repository: testimg
        tag: "0.1.2"
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
      register: tag_info




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags:

      .. rst-class:: ansible-option-title

      **tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of the tags in the repository.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` [{"docker\_image\_id": "be3e...29d4", "image\_id": "be3e...29d4", "is\_manifest\_list": false, "last\_modified": "Thu, 30 Sep 2021 06:10:23 -0000", "manifest\_digest": "sha256:9ce9...f3c7", "name": "1.33.1", "reversion": false, "size": 784538, "start\_ts": 1632982223}, {"docker\_image\_id": "be3e...29d4", "image\_id": "be3e...29d4", "is\_manifest\_list": false, "last\_modified": "Thu, 30 Sep 2021 06:10:22 -0000", "manifest\_digest": "sha256:9ce9...f3c7", "name": "latest", "reversion": false, "size": 784538, "start\_ts": 1632982222}, {"docker\_image\_id": "bda4...29b2", "end\_ts": 1640336040, "expiration": "Fri, 24 Dec 2021 08:54:00 -0000", "image\_id": "bda4...29b2", "is\_manifest\_list": false, "last\_modified": "Thu, 30 Sep 2021 06:10:21 -0000", "manifest\_digest": "sha256:a8f2...5ea7", "name": "1.34.0", "reversion": false, "size": 802700, "start\_ts": 1632982221}]


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/end_ts"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/end_ts:

      .. rst-class:: ansible-option-title

      **end_ts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/end_ts" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Time in seconds since the epoch of the tag expiration.

      The module only returns expired tags when the \ :emphasis:`only\_active\_tags`\  parameter is \ :literal:`no`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` only when an expiration date has been explicitly assigned.

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 1640336040


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/expiration"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/expiration:

      .. rst-class:: ansible-option-title

      **expiration**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/expiration" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Expiration date and time in a human readable format.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` only when an expiration date has been explicitly assigned.

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Fri, 24 Dec 2021 08:54:00 -0000"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/image_id"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/image_id:

      .. rst-class:: ansible-option-title

      **image_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/image_id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Identifier of the image associated with the tag.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "d53469b7e6ba9295a4b7a7d9e29537ab879e1582e64d534b6ed2637453dade25"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/last_modified"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/last_modified:

      .. rst-class:: ansible-option-title

      **last_modified**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/last_modified" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Date and time of the last tag modification in a human readable format.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Thu, 30 Sep 2021 06:10:22 -0000"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/manifest_digest"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/manifest_digest:

      .. rst-class:: ansible-option-title

      **manifest_digest**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/manifest_digest" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      SHA256 digest for the tag.

      You can use that digest to pull the image instead of using the tag name. For example, \ :literal:`podman pull quay.example.com/production/smallimage@sha256:a8f2...5ea7`\ 


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "sha256:a8f231c07da40107543d74ed1e9a1938a004b498377dbefcf29082c7a9e55ea7"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/name"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/name" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Tag identifier.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "0.1.2"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/size"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/size:

      .. rst-class:: ansible-option-title

      **size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/size" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Size of the associated image in bytes.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 802700


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags/start_ts"></div>

      .. _ansible_collections.herve4m.quay.quay_tag_info_module__return-tags/start_ts:

      .. rst-class:: ansible-option-title

      **start_ts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags/start_ts" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Time in seconds since the epoch of the last tag modification.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 1632982222


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Herve Quatremain (@herve4m)



.. Parsing errors

