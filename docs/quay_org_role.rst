.. Document meta

:orphan:

.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-entry
.. role:: ansible-option-default
.. role:: ansible-option-default-bold

.. Anchors

.. _ansible_collections.herve4m.quay.quay_org_role:

.. Anchors: aliases


.. Title

herve4m.quay.quay_org role -- Create and configure a Quay Container Registry organization
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This role is part of the `herve4m.quay collection <https://galaxy.ansible.com/herve4m/quay>`_ (version 0.1.1).

    To install it use: :code:`ansible-galaxy collection install herve4m.quay`.

    To use it in a playbook, specify: :code:`herve4m.quay.quay_org`.

.. contents::
   :local:
   :depth: 2


.. Entry point title

Entry point ``main`` -- Create and configure a Quay Container Registry organization
-----------------------------------------------------------------------------------

.. version_added


.. Deprecated


Synopsis
^^^^^^^^

.. Description

- Create an organization and configure it with robot accounts, teams, default permissions, OAuth applications, and repositories.

.. Requirements


.. Options

Parameters
^^^^^^^^^^

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
      <div class="ansibleOptionAnchor" id="parameter-main--quay_host"></div>
      <p class="ansible-option-title"><strong>quay_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_host" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>URL for accessing the API. <a href='https://quay.example.com:8443'>https://quay.example.com:8443</a> for example.</p>
      <p>If you do not set the parameter, then the role uses the <code class='docutils literal notranslate'>QUAY_HOST</code> environment variable.</p>
      <p>If you do no set the environment variable either, then the role uses the <a href='http://127.0.0.1'>http://127.0.0.1</a> URL.</p>
      <p class="ansible-option-line"><span class="ansible-option-default-bold">Default:</span> <span class="ansible-option-default">"http://127.0.0.1"</span></p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_applications"></div>
      <p class="ansible-option-title"><strong>quay_org_applications</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_applications" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Create applications in the organization.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_applications/application_uri"></div>
      <p class="ansible-option-title"><strong>application_uri</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_applications/application_uri" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>URL to the application home page.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_applications/avatar_email"></div>
      <p class="ansible-option-title"><strong>avatar_email</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_applications/avatar_email" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Email address that represents the avatar for the application.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_applications/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_applications/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Description for the application.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_applications/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_applications/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the application to create in the organization. Application names must be at least two characters long.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_applications/redirect_uri"></div>
      <p class="ansible-option-title"><strong>redirect_uri</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_applications/redirect_uri" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Prefix of the application&#x27;s OAuth redirection/callback URLs.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_default_perms"></div>
      <p class="ansible-option-title"><strong>quay_org_default_perms</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_default_perms" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Create default repository permissions for the organization.</p>
      <p>The permissions you define with this parameter apply when a user creates a new repository in the organization.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_default_perms/creator"></div>
      <p class="ansible-option-title"><strong>creator</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_default_perms/creator" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Quay applies the default permission only when repositories are created by the user that you define in <em>creator</em>.</p>
      <p>By default, if you do not provide that <em>creator</em> parameter, then Quay applies the default permission to all new repositories, whoever creates them.</p>
      <p>You cannot use robot accounts or teams for the <em>creator</em> parameter. You can only use regular user accounts.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_default_perms/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_default_perms/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the user or team that gets permission to new created repositories in the organization.</p>
      <p>For robot accounts use the <code class='docutils literal notranslate'>organization</code>+<code class='docutils literal notranslate'>shortrobotname</code> format.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_default_perms/role"></div>
      <p class="ansible-option-title"><strong>role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_default_perms/role" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Permission that Quay automatically grants to the user or team on new created repositories in the organization.</p>
      <p>If you do not provide that parameter, then the role uses <code class='docutils literal notranslate'>read</code> by default.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">read</span></p></li>
        <li><p><span class="ansible-option-choices-entry">write</span></p></li>
        <li><p><span class="ansible-option-choices-entry">admin</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_default_perms/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_default_perms/type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Type of the account defined in <em>name</em>. Choose <code class='docutils literal notranslate'>user</code> for both user and robot accounts.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">user</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">team</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_email"></div>
      <p class="ansible-option-title"><strong>quay_org_email</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_email" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Email address to associate with the new organization.</p>
      <p>If your Quay administrator has enabled the mailing capability of your Quay installation (<code class='docutils literal notranslate'>FEATURE_MAILING</code> to <code class='docutils literal notranslate'>true</code> in <code class='docutils literal notranslate'>config.yaml</code>), then this <em>email</em> parameter is mandatory.</p>
      <p>You cannot use the same address as your account email.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_name"></div>
      <p class="ansible-option-title"><strong>quay_org_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the organization to create.</p>
      <p>The name must be in lowercase and must not contain white spaces. For compatibility with earlier versions of Docker, the name must be at least four characters long.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_quota"></div>
      <p class="ansible-option-title"><strong>quay_org_quota</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_quota" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Quota that Quay uses to compute the warning and reject limits for the organization.</p>
      <p>You specify a quota in bytes, but you can also use the K[i]B, M[i]B, G[i]B, or T[i]B suffixes.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_reject_pct"></div>
      <p class="ansible-option-title"><strong>quay_org_reject_pct</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_reject_pct" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Reject (hard) limit as a percentage of the quota.</p>
      <p>Quay terminates any image push in the organization when the limit is reached.</p>
      <p>Set <em>quay_org_reject_pct</em> to <code class='docutils literal notranslate'>0</code> to remove the reject limit.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories"></div>
      <p class="ansible-option-title"><strong>quay_org_repositories</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Create repositories in the organization.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Text in Markdown format that describes the repository.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the repository to create in the organization. The name must be in lowercase and must not contain white spaces.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/perms"></div>
      <p class="ansible-option-title"><strong>perms</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/perms" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>User, robot, and team permissions to associate with the repository.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/perms/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/perms/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the account. The format for robot accounts is <code class='docutils literal notranslate'>organization</code>+<code class='docutils literal notranslate'>shortrobotname</code>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/perms/role"></div>
      <p class="ansible-option-title"><strong>role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/perms/role" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Type of permission to grant.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">read</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">write</span></p></li>
        <li><p><span class="ansible-option-choices-entry">admin</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/perms/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/perms/type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Specifies the type of the account. Choose <code class='docutils literal notranslate'>user</code> for both user and robot accounts.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">user</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">team</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/repo_state"></div>
      <p class="ansible-option-title"><strong>repo_state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/repo_state" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>NORMAL</code>, then the repository is in the default state (read/write).</p>
      <p>If <code class='docutils literal notranslate'>READ_ONLY</code>, then the repository is read-only.</p>
      <p>If <code class='docutils literal notranslate'>MIRROR</code>, then the repository is a mirror and you can configure it by using the M(quay_repository_mirror) module.</p>
      <p>You must enable the mirroring capability of your Quay installation to use this <em>repo_state</em> parameter.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">NORMAL</span></p></li>
        <li><p><span class="ansible-option-choices-entry">READ_ONLY</span></p></li>
        <li><p><span class="ansible-option-choices-entry">MIRROR</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_repositories/visibility"></div>
      <p class="ansible-option-title"><strong>visibility</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_repositories/visibility" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If <code class='docutils literal notranslate'>public</code>, then anyone can pull images from the repository.</p>
      <p>If <code class='docutils literal notranslate'>private</code>, then nobody can access the repository and you need to explicitly grant access to users, robots, and teams.</p>
      <p>If you do not set the parameter when you create a repository, then it defaults to <code class='docutils literal notranslate'>private</code>.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">public</span></p></li>
        <li><p><span class="ansible-option-choices-entry">private</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_robots"></div>
      <p class="ansible-option-title"><strong>quay_org_robots</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_robots" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of robot accounts to create for the organization.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_robots/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_robots/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Description of the robot account. You cannot update the description of existing robot accounts.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_robots/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_robots/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the robot account to create. Because the role creates the robot account in the organization it manages, you do not need to use the format <code class='docutils literal notranslate'>organization</code>+<code class='docutils literal notranslate'>shortname</code>, although the role accepts that format. You can simply specify the robot account name without the <code class='docutils literal notranslate'>organization</code>+ prefix.</p>
      <p>The name must be in lowercase, must not contain white spaces, must not start by a digit, and must be at least two characters long.</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_teams"></div>
      <p class="ansible-option-title"><strong>quay_org_teams</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_teams" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of teams to create in the organization.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_teams/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_teams/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Text in Markdown format that describes the team.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_teams/members"></div>
      <p class="ansible-option-title"><strong>members</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_teams/members" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>List of the user or robot accounts in the team. Use the syntax <code class='docutils literal notranslate'>organization</code>+<code class='docutils literal notranslate'>robotshortname</code> for robot accounts.</p>
      <p>If the team is synchronized with an LDAP group (see the M(quay_team_ldap) module), then you can only add or remove robot accounts.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_teams/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_teams/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the team to create.</p>
      <p>The name must be in lowercase, must not contain white spaces, must not start by a digit, and must be at least two characters long.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_teams/role"></div>
      <p class="ansible-option-title"><strong>role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_teams/role" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Role of the team within the organization. If not set, then the new team has the <code class='docutils literal notranslate'>member</code> role.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">member</span></p></li>
        <li><p><span class="ansible-option-choices-entry">creator</span></p></li>
        <li><p><span class="ansible-option-choices-entry">admin</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_users"></div>
      <p class="ansible-option-title"><strong>quay_org_users</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_users" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of user account to create.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_users/email"></div>
      <p class="ansible-option-title"><strong>email</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_users/email" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>User&#x27;s email address.</p>
      <p>If your Quay administrator has enabled the mailing capability of your Quay installation (<code class='docutils literal notranslate'>FEATURE_MAILING</code> to <code class='docutils literal notranslate'>true</code> in <code class='docutils literal notranslate'>config.yaml</code>), then this <em>email</em> parameter is mandatory.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_users/password"></div>
      <p class="ansible-option-title"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_users/password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>User&#x27;s password as a clear string.</p>
      <p>The password must be at least eight characters long and must not contain white spaces.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_users/username"></div>
      <p class="ansible-option-title"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_users/username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>

    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the user account to create.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_org_warning_pct"></div>
      <p class="ansible-option-title"><strong>quay_org_warning_pct</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_org_warning_pct" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Warning (soft) limit as a percentage of the quota.</p>
      <p>Quay notifies the users when the limit is reached.</p>
      <p>Set <em>quay_org_warning_pct</em> to <code class='docutils literal notranslate'>0</code> to remove the warning limit.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_password"></div>
      <p class="ansible-option-title"><strong>quay_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>The password to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the role tries the <code class='docutils literal notranslate'>QUAY_PASSWORD</code> environment variable.</p>
      <p>If you set <em>quay_password</em>, then you also need to set <em>quay_username</em>.</p>
      <p>Mutually exclusive with <em>quay_token</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_token"></div>
      <p class="ansible-option-title"><strong>quay_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>OAuth access token for authenticating against the API.</p>
      <p>If you do not set the parameter, then the role tries the <code class='docutils literal notranslate'>QUAY_TOKEN</code> environment variable.</p>
      <p>Mutually exclusive with <em>quay_username</em> and <em>quay_password</em>.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_username"></div>
      <p class="ansible-option-title"><strong>quay_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>The username to use for authenticating against the API.</p>
      <p>If you do not set the parameter, then the role tries the <code class='docutils literal notranslate'>QUAY_USERNAME</code> environment variable.</p>
      <p>If you set <em>quay_username</em>, then you also need to set <em>quay_password</em>.</p>
      <p>Mutually exclusive with <em>quay_token</em>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-main--quay_validate_certs"></div>
      <p class="ansible-option-title"><strong>quay_validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-main--quay_validate_certs" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>

    </div></td>
    <td><div class="ansible-option-cell">
      <p>Whether to allow insecure connections to the API.</p>
      <p>If <code class='docutils literal notranslate'>no</code>, then the role does not validate SSL certificates.</p>
      <p>If you do not set the parameter, then the role tries the <code class='docutils literal notranslate'>QUAY_VERIFY_SSL</code> environment variable (<code class='docutils literal notranslate'>yes</code>, <code class='docutils literal notranslate'>1</code>, and <code class='docutils literal notranslate'>True</code> mean yes, and <code class='docutils literal notranslate'>no</code>, <code class='docutils literal notranslate'>0</code>, <code class='docutils literal notranslate'>False</code>, and no value mean no).</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-default-bold">yes</span> <span class="ansible-option-default">← (default)</span></p></li>
      </ul>
    </div></td>
  </tr>
  </tbody>
  </table>



.. Notes


.. Seealso


Authors
^^^^^^^

- Hervé Quatremain 



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/herve4m/quay-collection/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/herve4m/quay-collection" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

