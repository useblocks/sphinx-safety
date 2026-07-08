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
