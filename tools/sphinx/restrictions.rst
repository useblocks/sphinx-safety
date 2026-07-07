Restrictions
============

.. restriction:: Warning to Error
   :id: RE_SPHINX_WARNINGS
   :avoids: ER_FILES_IGNORED, ER_SPH_WRONG_ENCODING, ER_SPH_WRONG_ACCESS

   Always use the sphinx-build option ``-W`` to transform all warnings
   into errors, because only errors stop the build and set an exit code >
   0.

.. restriction:: Clean full build
   :id: RE_SPHINX_CLEAN
   :avoids: ER_SPH_STALE_BUILD

   Always use a **clean** and **full** sphinx-build. An incremental build
   is not allowed, as not all files get updated by Sphinx.

   So before the ``sphinx-build`` command gets executed, the related ``build``
   folder shall be deleted. Then ``sphinx-build`` shall be built with the
   options ``-a`` and ``-E`` to force Sphinx to read and write really all
   files.
