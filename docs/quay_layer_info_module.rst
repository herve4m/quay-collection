
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.7.0

.. Anchors

.. _ansible_collections.herve4m.quay.quay_layer_info_module:

.. Anchors: short name for ansible.builtin

.. Title

herve4m.quay.quay_layer_info module -- Gather information about image layers in Quay Container Registry
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/ui/repo/published/herve4m/quay/>`_ (version 1.2.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_layer_info`.

.. version_added

.. rst-class:: ansible-version-added

New in herve4m.quay 0.0.1

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
      <p>Name of the image. The format is <code class='docutils literal notranslate'>namespace</code>/<code class='docutils literal notranslate'>repository</code>:<code class='docutils literal notranslate'>tag</code> or <code class='docutils literal notranslate'>namespace</code>/<code class='docutils literal notranslate'>repository</code>@<code class='docutils literal notranslate'>digest</code>. The namespace can be an organization or a personal namespace.</p>
      <p>If you omit the namespace part, then the module looks for the repository in your personal namespace.</p>
      <p>If you omit the tag and the digest part, then <code class='docutils literal notranslate'>latest</code> is assumed.</p>
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
      <p class="ansible-option-line"><strong class="ansible-option-default-bold">Default:</strong> <code class="ansible-value literal notranslate ansible-option-default">&#34;http://127.0.0.1&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_password"></div>
      <p class="ansible-option-title"><strong>quay_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The password to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_PASSWORD</code> environment variable.</p>
      <p>If you set <em>quay_password</em>, then you also need to set <em>quay_username</em>.</p>
      <p>Mutually exclusive with <em>quay_token</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_token"></div>
      <p class="ansible-option-title"><strong>quay_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>OAuth access token for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_TOKEN</code> environment variable.</p>
      <p>Mutually exclusive with <em>quay_username</em> and <em>quay_password</em>.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-quay_username"></div>
      <p class="ansible-option-title"><strong>quay_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quay_username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The username to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_USERNAME</code> environment variable.</p>
      <p>If you set <em>quay_username</em>, then you also need to set <em>quay_password</em>.</p>
      <p>Mutually exclusive with <em>quay_token</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>
      <p class="ansible-option-title"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p class="ansible-option-type-line"><span class="ansible-option-aliases">aliases: verify_ssl</span></p>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Whether to allow insecure connections to the API.</p>
      <p>If <code class='docutils literal notranslate'>no</code>, then the module does not validate SSL certificates.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_VERIFY_SSL</code> environment variable (<code class='docutils literal notranslate'>yes</code>, <code class='docutils literal notranslate'>1</code>, and <code class='docutils literal notranslate'>True</code> mean yes, and <code class='docutils literal notranslate'>no</code>, <code class='docutils literal notranslate'>0</code>, <code class='docutils literal notranslate'>False</code>, and no value mean no).</p>
      <p class="ansible-option-line"><strong class="ansible-option-choices">Choices:</strong></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">false</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold"><strong>true</strong></code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
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
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">[{&#34;author&#34;: &#34;Dalton Hubble &lt;...&gt;&#34;, &#34;blob_digest&#34;: &#34;sha256:a3ed...46d4&#34;, &#34;command&#34;: [&#34;/bin/sh&#34;, &#34;-c&#34;, &#34;#(nop) &#34;, &#34;ENTRYPOINT [\&#34;/usr/sbin/dnsmasq\&#34;]&#34;], &#34;comment&#34;: null, &#34;compressed_size&#34;: null, &#34;created_datetime&#34;: &#34;Thu, 16 Nov 2017 22:24:12 -0000&#34;, &#34;index&#34;: 6, &#34;is_remote&#34;: false, &#34;urls&#34;: null}, {&#34;author&#34;: &#34;Dalton Hubble &lt;...&gt;&#34;, &#34;blob_digest&#34;: &#34;sha256:a3e...46d4&#34;, &#34;command&#34;: [&#34;/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp&#34;], &#34;comment&#34;: null, &#34;compressed_size&#34;: null, &#34;created_datetime&#34;: &#34;Thu, 16 Nov 2017 22:24:12 -0000&#34;, &#34;index&#34;: 5, &#34;is_remote&#34;: false, &#34;urls&#34;: null}, {&#34;author&#34;: &#34;Dalton Hubble &lt;...&gt;&#34;, &#34;blob_digest&#34;: &#34;sha256:e40d...0351&#34;, &#34;command&#34;: [&#34;/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot &#34;], &#34;comment&#34;: null, &#34;compressed_size&#34;: null, &#34;created_datetime&#34;: &#34;Thu, 16 Nov 2017 22:24:11 -0000&#34;, &#34;index&#34;: 4, &#34;is_remote&#34;: false, &#34;urls&#34;: null}, {&#34;author&#34;: &#34;Dalton Hubble &lt;...&gt;&#34;, &#34;blob_digest&#34;: &#34;sha256:7ef3...3a74&#34;, &#34;command&#34;: [&#34;/bin/sh -c apk -U add dnsmasq curl&#34;], &#34;comment&#34;: null, &#34;compressed_size&#34;: null, &#34;created_datetime&#34;: &#34;Thu, 16 Nov 2017 22:24:09 -0000&#34;, &#34;index&#34;: 3, &#34;is_remote&#34;: false, &#34;urls&#34;: null}, {&#34;author&#34;: &#34;Dalton Hubble &lt;...&gt;&#34;, &#34;blob_digest&#34;: &#34;sha256:a3ed...46d4&#34;, &#34;command&#34;: [&#34;/bin/sh -c #(nop)  MAINTAINER Dalton Hubble &lt;...&gt;&#34;], &#34;comment&#34;: null, &#34;compressed_size&#34;: null, &#34;created_datetime&#34;: &#34;Thu, 16 Nov 2017 22:24:04 -0000&#34;, &#34;index&#34;: 2, &#34;is_remote&#34;: false, &#34;urls&#34;: null}, {&#34;author&#34;: null, &#34;blob_digest&#34;: &#34;sha256:a3ed...46d4&#34;, &#34;command&#34;: [&#34;/bin/sh -c #(nop)  CMD [\&#34;/bin/sh\&#34;]&#34;], &#34;comment&#34;: null, &#34;compressed_size&#34;: null, &#34;created_datetime&#34;: &#34;Wed, 13 Sep 2017 14:32:26 -0000&#34;, &#34;index&#34;: 1, &#34;is_remote&#34;: false, &#34;urls&#34;: null}, {&#34;author&#34;: null, &#34;blob_digest&#34;: &#34;sha256:6d98...d913&#34;, &#34;command&#34;: [&#34;/bin/sh -c #(nop) ADD file:4583...9e45 in / &#34;], &#34;comment&#34;: null, &#34;compressed_size&#34;: null, &#34;created_datetime&#34;: &#34;Wed, 13 Sep 2017 14:32:25 -0000&#34;, &#34;index&#34;: 0, &#34;is_remote&#34;: false, &#34;urls&#34;: null}]</code></p>
    </div></td>
  </tr>
  <tr class="row-odd">
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
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">[&#34;/bin/sh&#34;, &#34;-c&#34;, &#34;#(nop) &#34;, &#34;ENTRYPOINT [\&#34;/usr/sbin/dnsmasq\&#34;]&#34;]</code></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers/created_datetime"></div>
      <p class="ansible-option-title"><strong>created_datetime</strong></p>
      <a class="ansibleOptionLink" href="#return-layers/created_datetime" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Layer creation date and time.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">&#34;Thu, 30 Sep 2021 07:18:56 -0000&#34;</code></p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-layers/index"></div>
      <p class="ansible-option-title"><strong>index</strong></p>
      <a class="ansibleOptionLink" href="#return-layers/index" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Index of the layer in the image.</p>
      <p class="ansible-option-line"><strong class="ansible-option-returned-bold">Returned:</strong> always</p>
      <p class="ansible-option-line ansible-option-sample"><strong class="ansible-option-sample-bold">Sample:</strong> <code class="ansible-value literal notranslate ansible-option-sample">4</code></p>
    </div></td>
  </tr>

  </tbody>
  </table>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Herve Quatremain (@herve4m)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/herve4m/quay-collection/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/herve4m/quay-collection"
    external: true


.. Parsing errors

