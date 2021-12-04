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

.. _ansible_collections.herve4m.quay.quay_tag_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

herve4m.quay.quay_tag_info -- Gather information about tags in a Red Hat Quay repository
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.0.5).

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

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-only_active_tags"></div>
                    <b>only_active_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-only_active_tags" title="Permalink to this option"></a>
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
                                            <div>If <code>yes</code>, then the module only collects information on tags that have not expired. If <code>no</code>, then the module returns information on all the tags.</div>
                                            <div>You can identify expired tags (when <em>only_active_tags</em> is <code>no</code>) in the returned data by inspecting the <code>end_ts</code> or <code>expiration</code> tag attributes. Those attributes provide the expiration date.</div>
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
                                            <div>Name of the repository that contains the tags to list. The format is <code>namespace</code>/<code>shortname</code>. The namespace can be an organization or a personal namespace.</div>
                                            <div>If you omit the namespace part, then the module looks for the repository in your personal namespace.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-tag"></div>
                    <b>tag</b>
                    <a class="ansibleOptionLink" href="#parameter-tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Gather information on that specific tag instead of returning data on all the tags in the repository.</div>
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

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-tags"></div>
                    <b>tags</b>
                    <a class="ansibleOptionLink" href="#return-tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>List of the tags in the repository.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;docker_image_id&#x27;: &#x27;be3e...29d4&#x27;, &#x27;image_id&#x27;: &#x27;be3e...29d4&#x27;, &#x27;is_manifest_list&#x27;: False, &#x27;last_modified&#x27;: &#x27;Thu, 30 Sep 2021 06:10:23 -0000&#x27;, &#x27;manifest_digest&#x27;: &#x27;sha256:9ce9...f3c7&#x27;, &#x27;name&#x27;: &#x27;1.33.1&#x27;, &#x27;reversion&#x27;: False, &#x27;size&#x27;: 784538, &#x27;start_ts&#x27;: 1632982223}, {&#x27;docker_image_id&#x27;: &#x27;be3e...29d4&#x27;, &#x27;image_id&#x27;: &#x27;be3e...29d4&#x27;, &#x27;is_manifest_list&#x27;: False, &#x27;last_modified&#x27;: &#x27;Thu, 30 Sep 2021 06:10:22 -0000&#x27;, &#x27;manifest_digest&#x27;: &#x27;sha256:9ce9...f3c7&#x27;, &#x27;name&#x27;: &#x27;latest&#x27;, &#x27;reversion&#x27;: False, &#x27;size&#x27;: 784538, &#x27;start_ts&#x27;: 1632982222}, {&#x27;docker_image_id&#x27;: &#x27;bda4...29b2&#x27;, &#x27;end_ts&#x27;: 1640336040, &#x27;expiration&#x27;: &#x27;Fri, 24 Dec 2021 08:54:00 -0000&#x27;, &#x27;image_id&#x27;: &#x27;bda4...29b2&#x27;, &#x27;is_manifest_list&#x27;: False, &#x27;last_modified&#x27;: &#x27;Thu, 30 Sep 2021 06:10:21 -0000&#x27;, &#x27;manifest_digest&#x27;: &#x27;sha256:a8f2...5ea7&#x27;, &#x27;name&#x27;: &#x27;1.34.0&#x27;, &#x27;reversion&#x27;: False, &#x27;size&#x27;: 802700, &#x27;start_ts&#x27;: 1632982221}]</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/end_ts"></div>
                    <b>end_ts</b>
                    <a class="ansibleOptionLink" href="#return-tags/end_ts" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>only when an expiration date has been explicitly assigned.</td>
                <td>
                                            <div>Time in seconds since the epoch of the tag expiration.</div>
                                            <div>The module only returns expired tags when the <em>only_active_tags</em> parameter is <code>no</code>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1640336040</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/expiration"></div>
                    <b>expiration</b>
                    <a class="ansibleOptionLink" href="#return-tags/expiration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>only when an expiration date has been explicitly assigned.</td>
                <td>
                                            <div>Expiration date and time in a human readable format.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Fri, 24 Dec 2021 08:54:00 -0000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#return-tags/image_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Identifier of the image associated with the tag.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">d53469b7e6ba9295a4b7a7d9e29537ab879e1582e64d534b6ed2637453dade25</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/last_modified"></div>
                    <b>last_modified</b>
                    <a class="ansibleOptionLink" href="#return-tags/last_modified" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Date and time of the last tag modification in a human readable format.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Thu, 30 Sep 2021 06:10:22 -0000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/manifest_digest"></div>
                    <b>manifest_digest</b>
                    <a class="ansibleOptionLink" href="#return-tags/manifest_digest" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>SHA256 digest for the tag.</div>
                                            <div>You can use that digest to pull the image instead of using the tag name. For example, <code>podman pull quay.example.com/production/smallimage@sha256:a8f2...5ea7</code></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">sha256:a8f231c07da40107543d74ed1e9a1938a004b498377dbefcf29082c7a9e55ea7</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-tags/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Tag identifier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">0.1.2</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#return-tags/size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Size of the associated image in bytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">802700</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags/start_ts"></div>
                    <b>start_ts</b>
                    <a class="ansibleOptionLink" href="#return-tags/start_ts" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Time in seconds since the epoch of the last tag modification.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1632982222</div>
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
