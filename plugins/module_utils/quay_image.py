# Copyright: (c) 2022, Herve Quatremain <rv4m@yahoo.co.uk>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type


class QuayImage(object):
    """Provide access to the components of a container image."""

    def __init__(self, module, image):
        """Initialize the object.

        The method accepts the following formats for the image name:

        * ``namespace/repository@digest``. For example:
          ``bitnami/nginx@sha256:19e8...136e``
        * ``namespace/repository:tag``. For example:
          ``bitnami/nginx:1.21.5``
        * ``namespace/repository``. The ``latest`` tag is assumed. For example:
          ``bitnami/nginx``
        * ``repository@digest``. The user's personal namespace is assumed.
        * ``repository:tag``. The user's personal namespace is assumed.
        * ``repository``. The user's personal namespace and the ``latest`` tag
          are assumed.


        :param module: An initialized :py:class:``api_module.APIModule`` object
                       that can be used to access the API.
        :type module: :py:class:``api_module.APIModule``
        :param image: The image name to process
        :type image: str
        """
        try:
            repo, digest = image.split("@", 1)
            self._digest = digest
            self._tag = None
        except ValueError:
            try:
                repo, tag = image.rsplit(":", 1)
                self._digest = None
                self._tag = tag
            except ValueError:
                repo = image
                self._digest = None
                self._tag = "latest"

        # Get the namespace and the repository
        try:
            namespace, repo_shortname = repo.split("/", 1)
            self._namespace = namespace
            self._repository = repo_shortname
        except ValueError:
            # No namespace part in the repository name. Therefore, the
            # repository is in the user's personal namespace.
            # In case of anonymous access to the API, self.namespace is set to
            # None. That is an error that should be reported to the user
            # because when the API is anonymously accessed, the given image
            # name must include the namespace.
            self._namespace = module.who_am_i()
            self._repository = repo

    @property
    def namespace(self):
        """Return the namespace part of the image name.

        :return: The namespace part. If no namespace was provided in the image
                 name, then the namespace is the connected user's personal
                 namespace. In case of anonymous access, None is returned (it is
                 an error from the user to give an image name without a
                 namespace part when connected as anonymous)
        :rtype: str or None
        """
        return self._namespace

    @property
    def repository(self):
        """Return the repository part of the image name."""
        return self._repository

    @property
    def tag(self):
        """Return the tag part of the image name.

        :return: The tag part. If the given image specified a digest rather
                 than a tag, then None is returned. If neither a digest or a tag
                 were specified, then ``latest`` is returned.
        :rtype: str or None
        """
        return self._tag

    @property
    def digest(self):
        """Return the digest part of the image name.

        :return: The digest part. If the given image specified a tag rather
                 than a digest, then None is returned.
        :rtype: str or None
        """
        return self._digest
