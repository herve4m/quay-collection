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

.. _ansible_collections.herve4m.quay.quay_layer_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_layer_info -- Gather information about image layers in Red Hat Quay
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.6).

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

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-image"></div>
                    <b>image</b>
                    <a class="ansibleOptionLink" href="#parameter-image" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the image. The format is <code>namespace</code>/<code>repository</code>:<code>tag</code>. The namespace can be an organization or a personal namespace.</div>
                                            <div>If you omit the namespace part, then the module looks for the repository in your personal namespace.</div>
                                            <div>If you omit the tag, then it defaults to <code>latest</code>.</div>
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

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-layers"></div>
                    <b>layers</b>
                    <a class="ansibleOptionLink" href="#return-layers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Sorted list of the image layers. The top layer is listed first.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;ancestors&#x27;: &#x27;/f757...6b36/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/&#x27;, &#x27;command&#x27;: [&#x27;/bin/sh&#x27;, &#x27;-c&#x27;, &#x27;#(nop) &#x27;, &#x27;ENTRYPOINT [&quot;/usr/sbin/dnsmasq&quot;]&#x27;], &#x27;comment&#x27;: None, &#x27;created&#x27;: &#x27;Thu, 16 Nov 2017 22:24:13 -0000&#x27;, &#x27;id&#x27;: &#x27;3f7885b48af404b0b9fffb2120e5907929504b33a104894762e4e192f5db9e63&#x27;, &#x27;size&#x27;: 32, &#x27;sort_index&#x27;: 6, &#x27;uploading&#x27;: False}, {&#x27;ancestors&#x27;: &#x27;/e6f4...4f62/e619...cc21/f243...b231/15e0...2e36/a52c...327c/&#x27;, &#x27;command&#x27;: [&#x27;/bin/sh -c #(nop)  EXPOSE 53/tcp 67/tcp 69/tcp&#x27;], &#x27;comment&#x27;: None, &#x27;created&#x27;: &#x27;Thu, 16 Nov 2017 22:24:12 -0000&#x27;, &#x27;id&#x27;: &#x27;f7573df3a79319ce013ada220edea02c4def0bb2938d059313ca3b50c22c6b36&#x27;, &#x27;size&#x27;: 32, &#x27;sort_index&#x27;: 5, &#x27;uploading&#x27;: False}, {&#x27;ancestors&#x27;: &#x27;/e619...cc21/f243...b231/15e0...2e36/a52c...327c/&#x27;, &#x27;command&#x27;: [&#x27;/bin/sh -c #(nop) COPY dir:5c38...5694 in /var/lib/tftpboot &#x27;], &#x27;comment&#x27;: None, &#x27;created&#x27;: &#x27;Thu, 16 Nov 2017 22:24:11 -0000&#x27;, &#x27;id&#x27;: &#x27;e6f4fbbb429f4a42e138489b72fc451df7567750bfb28dfa81a4f93fb31b4f62&#x27;, &#x27;size&#x27;: 848185, &#x27;sort_index&#x27;: 4, &#x27;uploading&#x27;: False}, {&#x27;ancestors&#x27;: &#x27;/f243...b231/15e0...2e36/a52c...327c/&#x27;, &#x27;command&#x27;: [&#x27;/bin/sh -c apk -U add dnsmasq curl&#x27;], &#x27;comment&#x27;: None, &#x27;created&#x27;: &#x27;Thu, 16 Nov 2017 22:24:10 -0000&#x27;, &#x27;id&#x27;: &#x27;e6197fd52d52021b186662d4477d11db4520cbca280883245ef31cc4e2b3cc21&#x27;, &#x27;size&#x27;: 2010338, &#x27;sort_index&#x27;: 3, &#x27;uploading&#x27;: False}, {&#x27;ancestors&#x27;: &#x27;/15e0...2e36/a52c...327c/&#x27;, &#x27;command&#x27;: [&#x27;/bin/sh -c #(nop)  MAINTAINER Dalton Hubble &lt;dalton.hubble@coreos.com&gt;&#x27;], &#x27;comment&#x27;: None, &#x27;created&#x27;: &#x27;Thu, 16 Nov 2017 22:24:04 -0000&#x27;, &#x27;id&#x27;: &#x27;f2435a32f659b4a4568fbad867e9b88fa421586ab171ee2cd8096217e7ecb231&#x27;, &#x27;size&#x27;: 32, &#x27;sort_index&#x27;: 2, &#x27;uploading&#x27;: False}, {&#x27;ancestors&#x27;: &#x27;/a52c...327c/&#x27;, &#x27;command&#x27;: [&#x27;/bin/sh -c #(nop)  CMD [&quot;/bin/sh&quot;]&#x27;], &#x27;comment&#x27;: None, &#x27;created&#x27;: &#x27;Wed, 13 Sep 2017 14:32:26 -0000&#x27;, &#x27;id&#x27;: &#x27;15e0dc04655d169bbdc7e942756a594e808c6c50214aca9b97deb36715ec2e36&#x27;, &#x27;size&#x27;: 32, &#x27;sort_index&#x27;: 1, &#x27;uploading&#x27;: False}, {&#x27;ancestors&#x27;: &#x27;//&#x27;, &#x27;command&#x27;: [&#x27;/bin/sh -c #(nop) ADD file:4583...9e45 in / &#x27;], &#x27;comment&#x27;: None, &#x27;created&#x27;: &#x27;Wed, 13 Sep 2017 14:32:26 -0000&#x27;, &#x27;id&#x27;: &#x27;a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c&#x27;, &#x27;size&#x27;: 1990402, &#x27;sort_index&#x27;: 0, &#x27;uploading&#x27;: False}]</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-layers/ancestors"></div>
                    <b>ancestors</b>
                    <a class="ansibleOptionLink" href="#return-layers/ancestors" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Forward slash separated list of the parent layer identifiers.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">/f243...b231/15e0...2e36/a52c...327c/</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-layers/command"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#return-layers/command" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The command that was used to build the layer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;/bin/sh&#x27;, &#x27;-c&#x27;, &#x27;#(nop) &#x27;, &#x27;ENTRYPOINT [&quot;/usr/sbin/dnsmasq&quot;]&#x27;]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-layers/created"></div>
                    <b>created</b>
                    <a class="ansibleOptionLink" href="#return-layers/created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Layer creation date and time.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Thu, 30 Sep 2021 07:18:56 -0000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-layers/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-layers/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Internal identifier of the layer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">a52c7d714e5fc2f9c1e6bb2f8393636861045890c2731c53436924c9e2ad327c</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-layers/sort_index"></div>
                    <b>sort_index</b>
                    <a class="ansibleOptionLink" href="#return-layers/sort_index" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Index of the layer in the image.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">4</div>
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
