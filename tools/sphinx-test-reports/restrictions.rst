Restrictions
============

.. restriction:: Declare all property link types in ``tr_property_link_types``
   :id: RE_STR_PROP_LINK_TYPES
   :avoids: ER_STR_PROP_LINK_MISSING, ER_STR_PROP_TYPE_UNDECLARED
   :tool: TOOL_STR

   Every JUnit ``<property>`` name that shall create a Sphinx-Needs link must
   be listed in the ``tr_property_link_types`` configuration dict. The dict maps
   property name → link type name.

   In addition, the corresponding link type must be declared in
   ``ubproject.toml`` under ``[needs.links.<name>]``.

   Failing to declare a mapping causes property links to be silently dropped,
   making the test-to-requirement traceability chain invisible.

   Mitigates:

   - **ER_STR_PROP_LINK_MISSING**: Declared properties are always processed
   - **ER_STR_PROP_TYPE_UNDECLARED**: All required mappings are explicit

.. restriction:: Set ``tr_case_id_length`` and ``tr_suite_id_length`` to avoid collisions
   :id: RE_STR_ID_LENGTH
   :avoids: ER_STR_CASE_ID_COLLISION, ER_STR_SUITE_ID_COLLISION
   :tool: TOOL_STR

   The default ID length (5 characters) is insufficient for test suites with
   more than a few hundred test cases. Projects with large test suites must
   set ``tr_case_id_length`` ≥ 8 and ``tr_suite_id_length`` ≥ 6 in
   ``conf.py`` to keep the birthday-paradox collision probability below 0.1%.

   Example (used in this qualification project)::

      tr_case_id_length = 8
      tr_suite_id_length = 6

   Mitigates:

   - **ER_STR_CASE_ID_COLLISION**: Longer IDs drastically reduce collision risk
   - **ER_STR_SUITE_ID_COLLISION**: Same for suite IDs

.. restriction:: Use a dedicated custom type for imported test results
   :id: RE_STR_CUSTOM_TYPE
   :avoids: ER_STR_CUSTOM_TYPE_PREFIX_COLLISION
   :tool: TOOL_STR

   Configure ``tr_case`` to use a dedicated type name (e.g. ``testresult``)
   with a unique ID prefix (e.g. ``TR_``) that does not overlap with any other
   need type used in the project. This prevents ID collisions between imported
   results and hand-written test or requirement needs.

   Example::

      tr_case = ["test-case", "testresult", "Test Result", "TR_", "#4CAF50", "rectangle"]

   Mitigates:

   - **ER_STR_CUSTOM_TYPE_PREFIX_COLLISION**: Unique prefix guarantees no
     overlap with existing need IDs
