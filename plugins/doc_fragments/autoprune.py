# -*- coding: utf-8 -*-

# Copyright: (c) 2024 Hervé Quatremain <herve.quatremain@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    # Ansible Galaxy documentation fragment
    DOCUMENTATION = r"""
options:
  auto_prune_method:
    description:
      - Method to use for the auto-pruning tags policy.
      - If C(none), then the module ensures that no policy is in place. The
        tags are not pruned.
      - If C(tags), then the policy keeps only the number of tags that you
        specify in I(auto_prune_value).
      - If C(date), then the policy deletes the tags older than the time period
        that you specify in I(auto_prune_value).
      - I(auto_prune_value) is required when I(auto_prune_method) is C(tags) or
        C(date).
    type: str
    choices: [none, tags, date]
  auto_prune_value:
    description:
      - Number of tags to keep when I(auto_prune_value) is C(tags).
        The value must be 1 or more.
      - Period of time when I(auto_prune_value) is C(date). The value must be 1
        or more, and must be followed by a suffix; s (for second), m (for
        minute), h (for hour), d (for day), or w (for week).
      - I(auto_prune_method) is required when I(auto_prune_value) is set.
    type: str
notes:
  - Your Quay administrator must enable the auto-prune capability of your Quay
    installation (C(FEATURE_AUTO_PRUNE) in C(config.yaml)) to use the
    I(auto_prune_method) and I(auto_prune_value) parameters.
  - Using I(auto_prune_method) and I(auto_prune_value) requires Quay version
    3.11 or later.
"""
