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

herve4m.quay.quay_tag_info module -- Gather information about tags in a Red Hat Quay repository
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.1.0).

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
      <div class="ansibleOptionAnchor" id="parameter-digest"></div>
      <p class="ansible-option-title"><strong>digest</strong></p>
      <a class="ansibleOptionLink" href="#parameter-digest" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Gather information on the images with that digest instead of returning data on all the tags in the repository.</p>
      <p>Mutually exclusive with <em>tag</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-only_active_tags"></div>
      <p class="ansible-option-title"><strong>only_active_tags</strong></p>
      <a class="ansibleOptionLink" href="#parameter-only_active_tags" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>yes</code>, then the module only collects information on tags that have not expired and have not been deleted. If <code class='docutils literal notranslate'>no</code>, then the module returns information on all the tags.</p>
      <p>You can identify expired and deleted tags (when <em>only_active_tags</em> is <code class='docutils literal notranslate'>no</code>) in the returned data by inspecting the <code class='docutils literal notranslate'>end_ts</code> or <code class='docutils literal notranslate'>expiration</code> tag attributes. Those attributes provide the expiration or deletion date.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">no</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
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
  <tr class="row-odd">
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
      <p>OAuth access token for authenticating against the API.</p>
      <p>If you do not set the parameter, then the module tries the <code class='docutils literal notranslate'>QUAY_TOKEN</code> environment variable.</p>
      <p>Mutually exclusive with <em>quay_username</em> and <em>quay_password</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
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
      <p>Name of the repository that contains the tags to list. The format is <code class='docutils literal notranslate'>namespace</code>/<code class='docutils literal notranslate'>shortname</code>. The namespace can be an organization or a personal namespace.</p>
      <p>If you omit the namespace part, then the module looks for the repository in your personal namespace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-tag"></div>
      <p class="ansible-option-title"><strong>tag</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tag" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Gather information on that specific tag instead of returning data on all the tags in the repository.</p>
      <p>Mutually exclusive with <em>digest</em>.</p>
    </div></td>
  </tr>
  <tr class="row-even">
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

    - name: Retrieve the tags from the images with the given digest
      herve4m.quay.quay_tag_info:
        repository: production/smallimage
        digest: "sha256:53b2...a7c8"
        only_active_tags: true
        quay_host: https://quay.example.com
        quay_token: vgfH9zH5q6eV16Con7SvDQYSr0KPYQimMHVehZv7
      register: tags




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
      <div class="ansibleOptionAnchor" id="return-tags"></div>
      <p class="ansible-option-title"><strong>tags</strong></p>
      <a class="ansibleOptionLink" href="#return-tags" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of the tags in the repository.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> [{"is_manifest_list": false, "last_modified": "Thu, 30 Sep 2021 06:10:23 -0000", "manifest_digest": "sha256:9ce9...f3c7", "name": "1.33.1", "reversion": false, "size": 784538, "start_ts": 1632982223}, {"is_manifest_list": false, "last_modified": "Thu, 30 Sep 2021 06:10:22 -0000", "manifest_digest": "sha256:9ce9...f3c7", "name": "latest", "reversion": false, "size": 784538, "start_ts": 1632982222}, {"end_ts": 1640336040, "expiration": "Fri, 24 Dec 2021 08:54:00 -0000", "is_manifest_list": false, "last_modified": "Thu, 30 Sep 2021 06:10:21 -0000", "manifest_digest": "sha256:a8f2...5ea7", "name": "1.34.0", "reversion": false, "size": 802700, "start_ts": 1632982221}]</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-tags/end_ts"></div>
      <p class="ansible-option-title"><strong>end_ts</strong></p>
      <a class="ansibleOptionLink" href="#return-tags/end_ts" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Time in seconds since the epoch of the tag expiration.</p>
      <p>The module only returns expired tags when the <em>only_active_tags</em> parameter is <code class='docutils literal notranslate'>no</code>.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> only when an expiration date has been explicitly assigned.</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 1640336040</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-tags/expiration"></div>
      <p class="ansible-option-title"><strong>expiration</strong></p>
      <a class="ansibleOptionLink" href="#return-tags/expiration" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Expiration date and time in a human readable format.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> only when an expiration date has been explicitly assigned.</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Fri, 24 Dec 2021 08:54:00 -0000"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-tags/last_modified"></div>
      <p class="ansible-option-title"><strong>last_modified</strong></p>
      <a class="ansibleOptionLink" href="#return-tags/last_modified" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Date and time of the last tag modification in a human readable format.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Thu, 30 Sep 2021 06:10:22 -0000"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-tags/manifest_digest"></div>
      <p class="ansible-option-title"><strong>manifest_digest</strong></p>
      <a class="ansibleOptionLink" href="#return-tags/manifest_digest" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>SHA256 digest for the tag.</p>
      <p>You can use that digest to pull the image instead of using the tag name. For example, <code class='docutils literal notranslate'>podman pull quay.example.com/production/smallimage@sha256:a8f2...5ea7</code></p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "sha256:a8f231c07da40107543d74ed1e9a1938a004b498377dbefcf29082c7a9e55ea7"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-tags/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#return-tags/name" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Tag identifier.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "0.1.2"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-tags/size"></div>
      <p class="ansible-option-title"><strong>size</strong></p>
      <a class="ansibleOptionLink" href="#return-tags/size" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Size of the associated image in bytes.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 802700</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-tags/start_ts"></div>
      <p class="ansible-option-title"><strong>start_ts</strong></p>
      <a class="ansibleOptionLink" href="#return-tags/start_ts" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Time in seconds since the epoch of the last tag modification.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 1632982222</p>
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

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/herve4m/quay-collection/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/herve4m/quay-collection" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

