Restrictions
============

.. restriction:: Do not use dynamic functions
   :id: CHECK_UBC_NO_DYN
   :avoids: ER_UBC_JSON_INCOMPLETE

.. restriction:: Do not use list2needs
   :id: CHECK_UBC_NO_LIST2NEEDS
   :avoids: ER_UBC_JSON_INCOMPLETE

.. restriction:: Do not use/reference rst files outside the ubproject workspace/scope
   :id: CHECK_UBC_RST_WORKSPACE
   :avoids: ER_UBC_JSON_INCOMPLETE

.. restriction:: Run needs.json cross-check in CI and fail on any diff
   :id: RE_UBC_CROSSCHECK_CI
   :avoids: ER_UBC_CROSSCHECK_FALSE_NEG

   ``ubc diff json`` shall run in CI over the full field set (no
   exclusions) and return a non-zero exit code on any divergence, so an
   undetected difference between the two indices cannot reach a release.

.. restriction:: Run ``ubc format`` in check mode only in CI
   :id: RE_UBC_FORMAT_CHECK_ONLY
   :avoids: ER_UBC_FORMAT_ERRORS

   In CI, ``ubc format`` shall be invoked with the ``--check`` flag
   (or equivalent read-only mode). Silent auto-correction of RST files
   is not permitted in a CI pipeline; any formatting deviation causes a
   non-zero exit code so it can be reviewed before merging.

.. restriction:: Pin ``ubc`` and ``sphinx-needs`` to compatible releases
   :id: RE_UBC_VERSION_PIN
   :avoids: ER_UBC_SCHEMA_DIVERGE

   ``ubc`` and ``sphinx-needs`` shall be version-pinned together in the
   same dependency lock file. A version bump of either tool requires a
   joint re-qualification step to ensure the JSON-Schema evaluation
   engines remain compatible.

.. restriction:: Schema violations must cause a non-zero exit code
   :id: RE_UBC_SCHEMA_SEVERITY_ERROR
   :avoids: ER_UBC_SCHEMA_EXIT_ZERO

   The ``severity`` for all schema rules in ``ubproject.toml`` shall be
   set to ``error`` (not ``warning``). CI must assert that
   ``ubc schema validate`` returns exit code ``0`` only when no
   violations are present. A pipeline step that ignores the exit code
   is not permitted.

.. restriction:: Run ``ubc diff git`` with sufficient impact depth
   :id: RE_UBC_DIFF_MIN_DEPTH
   :avoids: ER_UBC_DIFF_DEPTH_CUT

   ``ubc diff git`` shall be configured with ``--impact-depth`` set to at
   least the longest safety-relevant link chain in the project (minimum
   5). The configured depth shall be reviewed whenever new link types
   or multi-level traceability chains are introduced.

.. restriction:: Run ``ubc diff git`` with ``--impact-direction both``
   :id: RE_UBC_DIFF_DIRECTION_BOTH
   :avoids: ER_UBC_DIFF_DIR_WRONG

   ``ubc diff git`` shall always be called with ``--impact-direction both``
   so that both outgoing (downstream) and incoming (upstream / dependent)
   needs are included in the impact report. Omitting incoming links
   silently under-reports the change scope.
