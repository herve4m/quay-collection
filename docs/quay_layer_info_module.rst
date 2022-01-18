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

.. _ansible_collections.herve4m.quay.quay_layer_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_layer_info -- Gather information about image layers in Red Hat Quay
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.9).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_layer_info`.

.. version_added

.. versionadded:: 0.0.1 of herve4m.quay

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Gather information about the layers of an image in a repository.


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
        <div class="ansibleOptionAnchor" id="parameter-image"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__parameter-image:

      .. rst-class:: ansible-option-title

      **image**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-image" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the image. The format is \ :literal:`namespace`\ /\ :literal:`repository`\ :\ :literal:`tag`\ . The namespace can be an organization or a personal namespace.

      If you omit the namespace part, then the module looks for the repository in your personal namespace.

      If you omit the tag, then it defaults to \ :literal:`latest`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quay_host"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__parameter-quay_host:

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

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__parameter-quay_token:

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
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
        <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__parameter-validate_certs:
      .. _ansible_collections.herve4m.quay.quay_layer_info_module__parameter-verify_ssl:

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

    
    - name: Retrieve the layers of the coreos/dnsmasq:latest image
      herve4m.quay.quay_layer_info:
        image: coreos/dnsmasq:latest
        quay_host: quay.io
      register: layers




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
        <div class="ansibleOptionAnchor" id="return-layers"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__return-layers:

      .. rst-class:: ansible-option-title

      **layers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-layers" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sorted list of the image layers. The top layer is listed first.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` [{"ancestors": "/f757...6b36/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh", "-c", "#(nop) ", "ENTRYPOINT [\\"/usr/sbin/dnsmasq\\"]"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:13 -0000", "id": "3f7885b48af404b0b9fffb2120e5907929504b33a104894762e4e192f5db9e63", "size": 32, "sort\_index": 6, "uploading": false}, {"ancestors": "/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:12 -0000", "id": "f7573df3a79319ce013ada220edea02c4def0bb2938d059313ca3b50c22c6b36", "size": 32, "sort\_index": 5, "uploading": false}, {"ancestors": "/e619...cc21/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot "], "comment": null, "created": "Thu, 16 Nov 2017 22:24:11 -0000", "id": "e6f4fbbb429f4a42e138489b72fc451df7567750bfb28dfa81a4f93fb31b4f62", "size": 848185, "sort\_index": 4, "uploading": false}, {"ancestors": "/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c apk -U add dnsmasq curl"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:10 -0000", "id": "e6197fd52d52021b186662d4477d11db4520cbca280883245ef31cc4e2b3cc21", "size": 2010338, "sort\_index": 3, "uploading": false}, {"ancestors": "/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c #(nop)  MAINTAINER Dalton Hubble \\u003cdalton.hubble@coreos.com\\u003e"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:04 -0000", "id": "f2435a32f659b4a4568fbad867e9b88fa421586ab171ee2cd8096217e7ecb231", "size": 32, "sort\_index": 2, "uploading": false}, {"ancestors": "/a52c...327c/", "command": ["/bin/sh -c #(nop)  CMD [\\"/bin/sh\\"]"], "comment": null, "created": "Wed, 13 Sep 2017 14:32:26 -0000", "id": "15e0dc04655d169bbdc7e942756a594e808c6c50214aca9b97deb36715ec2e36", "size": 32, "sort\_index": 1, "uploading": false}, {"ancestors": "//", "command": ["/bin/sh -c #(nop) ADD file:4583...9e45 in / "], "comment": null, "created": "Wed, 13 Sep 2017 14:32:26 -0000", "id": "a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c", "size": 1990402, "sort\_index": 0, "uploading": false}]


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-layers/ancestors"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__return-layers/ancestors:

      .. rst-class:: ansible-option-title

      **ancestors**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-layers/ancestors" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Forward slash separated list of the parent layer identifiers.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "/f243...b231/15e0...2e36/a52c...327c/"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-layers/command"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__return-layers/command:

      .. rst-class:: ansible-option-title

      **command**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-layers/command" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The command that was used to build the layer.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` ["/bin/sh", "-c", "#(nop) ", "ENTRYPOINT [\\"/usr/sbin/dnsmasq\\"]"]


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-layers/created"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__return-layers/created:

      .. rst-class:: ansible-option-title

      **created**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-layers/created" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Layer creation date and time.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Thu, 30 Sep 2021 07:18:56 -0000"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-layers/id"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__return-layers/id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-layers/id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Internal identifier of the layer.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-layers/sort_index"></div>

      .. _ansible_collections.herve4m.quay.quay_layer_info_module__return-layers/sort_index:

      .. rst-class:: ansible-option-title

      **sort_index**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-layers/sort_index" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Index of the layer in the image.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 4


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Herve Quatremain (@herve4m)



.. Parsing errors

