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
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.13).

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
      <div class="ansibleOptionAnchor" id="parameter-image"></div>
      <p class="ansible-option-title"><strong>image</strong></p>
      <a class="ansibleOptionLink" href="#parameter-image" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the image. The format is <code class='docutils literal notranslate'>namespace</code>/<code class='docutils literal notranslate'>repository</code>:<code class='docutils literal notranslate'>tag</code>. The namespace can be an organization or a personal namespace.</p>
      <p>If you omit the namespace part, then the module looks for the repository in your personal namespace.</p>
      <p>If you omit the tag, then it defaults to <code class='docutils literal notranslate'>latest</code>.</p>
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

.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Key</p></th>
    <th class="head"><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers"></div>
      <p class="ansible-option-title"><strong>layers</strong></p>
      <a class="ansibleOptionLink" href="#return-layers" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Sorted list of the image layers. The top layer is listed first.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> [{"ancestors": "/f757...6b36/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh", "-c", "#(nop) ", "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:13 -0000", "id": "3f7885b48af404b0b9fffb2120e5907929504b33a104894762e4e192f5db9e63", "size": 32, "sort_index": 6, "uploading": false}, {"ancestors": "/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:12 -0000", "id": "f7573df3a79319ce013ada220edea02c4def0bb2938d059313ca3b50c22c6b36", "size": 32, "sort_index": 5, "uploading": false}, {"ancestors": "/e619...cc21/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot "], "comment": null, "created": "Thu, 16 Nov 2017 22:24:11 -0000", "id": "e6f4fbbb429f4a42e138489b72fc451df7567750bfb28dfa81a4f93fb31b4f62", "size": 848185, "sort_index": 4, "uploading": false}, {"ancestors": "/f243...b231/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c apk -U add dnsmasq curl"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:10 -0000", "id": "e6197fd52d52021b186662d4477d11db4520cbca280883245ef31cc4e2b3cc21", "size": 2010338, "sort_index": 3, "uploading": false}, {"ancestors": "/15e0...2e36/a52c...327c/", "command": ["/bin/sh -c #(nop)  MAINTAINER Dalton Hubble \u003cdalton.hubble@coreos.com\u003e"], "comment": null, "created": "Thu, 16 Nov 2017 22:24:04 -0000", "id": "f2435a32f659b4a4568fbad867e9b88fa421586ab171ee2cd8096217e7ecb231", "size": 32, "sort_index": 2, "uploading": false}, {"ancestors": "/a52c...327c/", "command": ["/bin/sh -c #(nop)  CMD [\"/bin/sh\"]"], "comment": null, "created": "Wed, 13 Sep 2017 14:32:26 -0000", "id": "15e0dc04655d169bbdc7e942756a594e808c6c50214aca9b97deb36715ec2e36", "size": 32, "sort_index": 1, "uploading": false}, {"ancestors": "//", "command": ["/bin/sh -c #(nop) ADD file:4583...9e45 in / "], "comment": null, "created": "Wed, 13 Sep 2017 14:32:26 -0000", "id": "a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c", "size": 1990402, "sort_index": 0, "uploading": false}]</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers/ancestors"></div>
      <p class="ansible-option-title"><strong>ancestors</strong></p>
      <a class="ansibleOptionLink" href="#return-layers/ancestors" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Forward slash separated list of the parent layer identifiers.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "/f243...b231/15e0...2e36/a52c...327c/"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers/command"></div>
      <p class="ansible-option-title"><strong>command</strong></p>
      <a class="ansibleOptionLink" href="#return-layers/command" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command that was used to build the layer.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> ["/bin/sh", "-c", "#(nop) ", "ENTRYPOINT [\"/usr/sbin/dnsmasq\"]"]</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers/created"></div>
      <p class="ansible-option-title"><strong>created</strong></p>
      <a class="ansibleOptionLink" href="#return-layers/created" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Layer creation date and time.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Thu, 30 Sep 2021 07:18:56 -0000"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers/id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#return-layers/id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Internal identifier of the layer.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers/sort_index"></div>
      <p class="ansible-option-title"><strong>sort_index</strong></p>
      <a class="ansibleOptionLink" href="#return-layers/sort_index" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Index of the layer in the image.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 4</p>
    </div></td>
  </tr>

  </tbody>
  </table>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Herve Quatremain (@herve4m)



.. Parsing errors

