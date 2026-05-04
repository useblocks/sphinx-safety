Restrictions
============

.. restriction:: Do not use dynamic functions
   :id: CHECK_SN_NO_DYN
   :avoids: ER_SN_DYN_INVALID, ER_SN_DYN_WRONG

   Dynamic functions can execute not qualified code, which has full
   access to all Sphinx-Needs data. So its execution can corrupt the
   data.

.. restriction:: Warning to Error
   :id: RE_SN_WARNINGS
   :avoids: ER_FILES_IGNORED, ER_SN_DATA_INVALID

   Always use the sphinx-build option ``-W`` to transform all warnings
   into errors, because only errors stop the build and set an exit code >
   0.

.. restriction:: Clean full build
   :id: RE_SN_CLEAN

   Always use a **clean** and **full** sphinx-build. An incremental build
   is not allowed, as not all files get updated by Sphinx.

   So before the ``sphinx-build`` command gets executed, the related ``build``
   folder shall be deleted. Then ``sphinx-build`` shall be built with the
   options ``-a`` and ``-E`` to force Sphinx to read and write really all
   files.

.. restriction:: Use declarative schema validation instead of needs_constraints
   :id: RE_SN_USE_SCHEMA
   :avoids: ER_SN_CONSTRAINT_NOT_CHECKED, ER_SN_CONSTRAINT_FAIL_SILENTLY, ER_SN_CONSTRAINT_WRONG_DATA, ER_SN_CONSTRAINT_INCOMPLETE_DATA, ER_SN_CONSTRAINT_INVALID_DATA

   The legacy ``needs_constraints`` mechanism evaluates arbitrary
   Python expressions against need data. Safety-relevant projects
   shall use :need:`FE_SN_SCHEMA_VALIDATION` (JSON-Schema based) via
   ``needs_schema_definitions`` or ``schema_definitions_from_json``
   instead. The schema form is declarative, auditable, reproducible
   (no embedded Python), and its diagnostics are structured
   (``sn_schema_*``), which lets CI and ubCode process them.

.. restriction:: Use severity "violation" for safety-relevant schema rules
   :id: RE_SN_SCHEMA_VIOLATION
   :avoids: ER_SN_SCHEMA_WRONG_SEVERITY, ER_SN_SCHEMA_NOT_REPORTED

   Any schema rule that encodes a safety invariant (e.g. "every safe
   feature raises at least one fault", "every fault is mitigated")
   shall declare ``severity = "violation"``. Combined with
   :need:`RE_SN_WARNINGS`, a violation breaks the build and therefore
   cannot reach a release pipeline unnoticed.

.. restriction:: Type every extra field via needs.fields schema
   :id: RE_SN_TYPE_FIELDS
   :avoids: ER_SN_TYPED_FIELD_TYPE_MISS, ER_SN_TYPED_FIELD_ENUM_MISS, ER_SN_TYPED_FIELD_RANGE_MISS, ER_SN_INVALID_OPTION_VALUE

   Every field declared under ``[needs.fields.<name>]`` shall carry
   at least an explicit ``schema.type``. Safety-relevant enumerations
   (``asil``, ``tcl``, ``ti``, ``td``, ``si``) shall additionally
   declare ``schema.enum``. This removes the fall-back to an untyped
   nullable-string schema and makes invalid values surface during
   the build.

.. restriction:: Declare cardinality on safety-relevant link types
   :id: RE_SN_LINK_CARDINALITY
   :avoids: ER_SN_TYPED_LINK_CARD_MISS

   Link types that express safety-relevant completeness
   (``raises``, ``avoids``, ``checks``, ``errors``, ``responsible``)
   shall declare ``schema.minItems = 1`` under their
   ``[needs.links.<name>]`` entry so that a missing link produces a
   schema violation rather than a silent gap.

.. restriction:: Export link conditions in needs.json
   :id: RE_SN_JSON_LINK_COND
   :avoids: ER_SN_JSON_LINK_COND_MISSING

   ``needs_json_include_link_conditions`` shall be left at the
   default ``True`` for the qualification artefact, so that the
   exported ``needs.json`` is a complete record of the traceability
   including conditions evaluated at build time.
