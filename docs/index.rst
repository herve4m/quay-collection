

.. _plugins_in_herve4m.quay:

Herve4M.Quay
============

Collection version 0.1.0

.. contents::
   :local:
   :depth: 1

Description
-----------

Ansible modules to manage Red Hat Quay installations

**Author:**

* Hervé Quatremain <rv4m@yahoo.co.uk>

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/herve4m/quay-collection/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/herve4m/quay-collection" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>



.. toctree::
    :maxdepth: 1


Plugin Index
------------

These are the plugins in the herve4m.quay collection:


Modules
~~~~~~~

* :ref:`quay_api_token module <ansible_collections.herve4m.quay.quay_api_token_module>` -- Create OAuth access tokens for accessing the Red Hat Quay API
* :ref:`quay_application module <ansible_collections.herve4m.quay.quay_application_module>` -- Manage Red Hat Quay applications
* :ref:`quay_default_perm module <ansible_collections.herve4m.quay.quay_default_perm_module>` -- Manage Red Hat Quay default repository permissions
* :ref:`quay_docker_token module <ansible_collections.herve4m.quay.quay_docker_token_module>` -- Manage tokens for accessing Red Hat Quay repositories
* :ref:`quay_first_user module <ansible_collections.herve4m.quay.quay_first_user_module>` -- Create the first user account
* :ref:`quay_layer_info module <ansible_collections.herve4m.quay.quay_layer_info_module>` -- Gather information about image layers in Red Hat Quay
* :ref:`quay_manifest_label module <ansible_collections.herve4m.quay.quay_manifest_label_module>` -- Manage Red Hat Quay image manifest labels
* :ref:`quay_manifest_label_info module <ansible_collections.herve4m.quay.quay_manifest_label_info_module>` -- Gather information about manifest labels in Red Hat Quay
* :ref:`quay_message module <ansible_collections.herve4m.quay.quay_message_module>` -- Manage Red Hat Quay global messages
* :ref:`quay_notification module <ansible_collections.herve4m.quay.quay_notification_module>` -- Manage Red Hat Quay repository notifications
* :ref:`quay_organization module <ansible_collections.herve4m.quay.quay_organization_module>` -- Manage Red Hat Quay organizations
* :ref:`quay_quota module <ansible_collections.herve4m.quay.quay_quota_module>` -- Manage Red Hat Quay organizations quota
* :ref:`quay_repository module <ansible_collections.herve4m.quay.quay_repository_module>` -- Manage Red Hat Quay repositories
* :ref:`quay_repository_mirror module <ansible_collections.herve4m.quay.quay_repository_mirror_module>` -- Manage Red Hat Quay repository mirror configurations
* :ref:`quay_robot module <ansible_collections.herve4m.quay.quay_robot_module>` -- Manage Red Hat Quay robot accounts
* :ref:`quay_tag module <ansible_collections.herve4m.quay.quay_tag_module>` -- Manage Red Hat Quay image tags
* :ref:`quay_tag_info module <ansible_collections.herve4m.quay.quay_tag_info_module>` -- Gather information about tags in a Red Hat Quay repository
* :ref:`quay_team module <ansible_collections.herve4m.quay.quay_team_module>` -- Manage Red Hat Quay teams
* :ref:`quay_team_ldap module <ansible_collections.herve4m.quay.quay_team_ldap_module>` -- Synchronize Red Hat Quay teams with LDAP groups
* :ref:`quay_user module <ansible_collections.herve4m.quay.quay_user_module>` -- Manage Red Hat Quay users
* :ref:`quay_vulnerability_info module <ansible_collections.herve4m.quay.quay_vulnerability_info_module>` -- Gather information about image vulnerabilities in Red Hat Quay


Role Index
----------

These are the roles in the herve4m.quay collection:

* :ref:`quay_org role <ansible_collections.herve4m.quay.quay_org_role>` -- Create and configure a Red Hat Quay organization


.. seealso::

    List of :ref:`collections <list_of_collections>` with docs hosted here.

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
    quay_quota_module
    quay_repository_module
    quay_repository_mirror_module
    quay_robot_module
    quay_tag_module
    quay_tag_info_module
    quay_team_module
    quay_team_ldap_module
    quay_user_module
    quay_vulnerability_info_module
    quay_org_role
