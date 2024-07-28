

.. meta::
  :antsibull-docs: 2.12.0


.. _plugins_in_herve4m.quay:

Herve4M.Quay
============

Collection version 1.4.0

.. contents::
   :local:
   :depth: 1

Description
-----------

Ansible modules to manage Quay Container Registry installations

**Author:**

* Hervé Quatremain <rv4m@yahoo.co.uk>

**Supported ansible-core versions:**

* 2.15.0 or newer

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/herve4m/quay-collection/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/herve4m/quay-collection"
    external: true




.. toctree::
    :maxdepth: 1

Plugin Index
------------

These are the plugins in the herve4m.quay collection:


Modules
~~~~~~~

* :ansplugin:`quay_api_token module <herve4m.quay.quay_api_token#module>` -- Create OAuth access tokens for accessing the Quay Container Registry API
* :ansplugin:`quay_application module <herve4m.quay.quay_application#module>` -- Manage Quay Container Registry applications
* :ansplugin:`quay_default_perm module <herve4m.quay.quay_default_perm#module>` -- Manage Quay Container Registry default repository permissions
* :ansplugin:`quay_docker_token module <herve4m.quay.quay_docker_token#module>` -- Manage tokens for accessing Quay Container Registry repositories
* :ansplugin:`quay_first_user module <herve4m.quay.quay_first_user#module>` -- Create the first user account
* :ansplugin:`quay_layer_info module <herve4m.quay.quay_layer_info#module>` -- Gather information about image layers in Quay Container Registry
* :ansplugin:`quay_manifest_label module <herve4m.quay.quay_manifest_label#module>` -- Manage Quay Container Registry image manifest labels
* :ansplugin:`quay_manifest_label_info module <herve4m.quay.quay_manifest_label_info#module>` -- Gather information about manifest labels in Quay Container Registry
* :ansplugin:`quay_message module <herve4m.quay.quay_message#module>` -- Manage Quay Container Registry global messages
* :ansplugin:`quay_notification module <herve4m.quay.quay_notification#module>` -- Manage Quay Container Registry repository notifications
* :ansplugin:`quay_organization module <herve4m.quay.quay_organization#module>` -- Manage Quay Container Registry organizations
* :ansplugin:`quay_proxy_cache module <herve4m.quay.quay_proxy_cache#module>` -- Manage Quay Container Registry proxy cache configurations
* :ansplugin:`quay_quota module <herve4m.quay.quay_quota#module>` -- Manage Quay Container Registry organizations quota
* :ansplugin:`quay_repository module <herve4m.quay.quay_repository#module>` -- Manage Quay Container Registry repositories
* :ansplugin:`quay_repository_mirror module <herve4m.quay.quay_repository_mirror#module>` -- Manage Quay Container Registry repository mirror configurations
* :ansplugin:`quay_robot module <herve4m.quay.quay_robot#module>` -- Manage Quay Container Registry robot accounts
* :ansplugin:`quay_tag module <herve4m.quay.quay_tag#module>` -- Manage Quay Container Registry image tags
* :ansplugin:`quay_tag_info module <herve4m.quay.quay_tag_info#module>` -- Gather information about tags in a Quay Container Registry repository
* :ansplugin:`quay_team module <herve4m.quay.quay_team#module>` -- Manage Quay Container Registry teams
* :ansplugin:`quay_team_ldap module <herve4m.quay.quay_team_ldap#module>` -- Synchronize Quay Container Registry teams with LDAP groups
* :ansplugin:`quay_team_oidc module <herve4m.quay.quay_team_oidc#module>` -- Synchronize Quay Container Registry teams with OIDC groups
* :ansplugin:`quay_user module <herve4m.quay.quay_user#module>` -- Manage Quay Container Registry users
* :ansplugin:`quay_vulnerability_info module <herve4m.quay.quay_vulnerability_info#module>` -- Gather information about image vulnerabilities in Quay Container Registry

.. toctree::
    :maxdepth: 1
    :hidden:

    quay_api_token_module
    quay_application_module
    quay_default_perm_module
    quay_docker_token_module
    quay_first_user_module
    quay_layer_info_module
    quay_manifest_label_module
    quay_manifest_label_info_module
    quay_message_module
    quay_notification_module
    quay_organization_module
    quay_proxy_cache_module
    quay_quota_module
    quay_repository_module
    quay_repository_mirror_module
    quay_robot_module
    quay_tag_module
    quay_tag_info_module
    quay_team_module
    quay_team_ldap_module
    quay_team_oidc_module
    quay_user_module
    quay_vulnerability_info_module


Filter Plugins
~~~~~~~~~~~~~~

* :ansplugin:`quay_docker_config filter <herve4m.quay.quay_docker_config#filter>` -- Build a Docker configuration in JSON format

.. toctree::
    :maxdepth: 1
    :hidden:

    quay_docker_config_filter


Role Index
----------

These are the roles in the herve4m.quay collection:

* :ansplugin:`quay_org role <herve4m.quay.quay_org#role>` -- Create and configure a Quay Container Registry organization


.. toctree::
    :maxdepth: 1
    :hidden:

    quay_org_role

