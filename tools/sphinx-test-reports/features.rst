Features
========

.. dropdown:: 🔍 Features

   .. needtable::
      :filter: "tools/sphinx-test-reports/" in docname and type == "feature"
      :columns: id, title, si as "SI", parent_needs_back as "Faults"

   .. needpie:: Sphinx-Test-Reports features
      :legend:
      :labels: Safety impact, No impact, Undefined impact

      type == "feature" and "tools/sphinx-test-reports/" in docname and si == "yes"
      type == "feature" and "tools/sphinx-test-reports/" in docname and si == "no"
      type == "feature" and "tools/sphinx-test-reports/" in docname and si == ""

.. feature:: Import JUnit XML test results
   :id: FE_STR_JUNIT_IMPORT
   :tools: TOOL_STR
   :si: yes

   Parse a JUnit-compatible XML file and make all contained test suites and
   test cases available as Sphinx-Needs objects via the ``test-file`` directive.

   .. fault:: JUnit XML file cannot be parsed
      :id: ER_STR_XML_PARSE

      The XML file is malformed, incomplete, or contains encoding errors that
      prevent successful parsing.

   .. fault:: JUnit XML file contains unexpected schema
      :id: ER_STR_XML_SCHEMA

      The XML structure deviates from the expected JUnit schema (e.g. missing
      ``testsuites`` root, unexpected attributes), causing data to be silently
      dropped or misread.

   .. fault:: Test result status is incorrectly classified
      :id: ER_STR_STATUS_WRONG

      A test that failed, was skipped, or errored is imported with a wrong
      ``result`` value (e.g. ``passed`` instead of ``failed``).

   .. fault:: Test result status is not detected
      :id: ER_STR_STATUS_MISSING

      The ``result`` field on an imported test-case need is empty or absent
      even though the XML contained explicit pass/fail/skip/error information.

.. feature:: Auto-generate test suite needs
   :id: FE_STR_AUTO_SUITES
   :tools: TOOL_STR
   :si: yes

   When ``auto_suites`` is set, each ``<testsuite>`` element in the XML
   generates a ``testsuite`` need automatically.

   .. fault:: Test suite need is not created
      :id: ER_STR_SUITE_MISSING

      A ``<testsuite>`` element in the XML does not result in a ``testsuite``
      need in the documentation.

   .. fault:: Test suite ID collision
      :id: ER_STR_SUITE_ID_COLLISION

      Two test suites receive the same auto-generated ID, causing one to
      silently overwrite the other or a build error.

.. feature:: Auto-generate test case needs
   :id: FE_STR_AUTO_CASES
   :tools: TOOL_STR
   :si: yes

   When ``auto_cases`` is set, each ``<testcase>`` element in the XML
   generates a ``testcase`` need automatically with a stable hash-based ID.

   .. fault:: Test case need is not created
      :id: ER_STR_CASE_MISSING

      A ``<testcase>`` element in the XML does not result in a need in the
      documentation.

   .. fault:: Test case ID collision
      :id: ER_STR_CASE_ID_COLLISION

      Two test cases receive the same auto-generated ID because
      ``tr_case_id_length`` is too small for the number of test cases.

   .. fault:: Test case need contains wrong data
      :id: ER_STR_CASE_WRONG_DATA

      Fields such as ``classname``, ``file``, ``time``, or ``message`` on the
      imported test-case need differ from the values in the JUnit XML.

.. feature:: Map JUnit properties to Sphinx-Needs links
   :id: FE_STR_PROPERTY_LINKS
   :tools: TOOL_STR
   :si: yes

   JUnit XML ``<property>`` elements with a name declared in
   ``tr_property_link_types`` are turned into outgoing Sphinx-Needs links on
   the imported test-case need.

   .. fault:: Property link is not created
      :id: ER_STR_PROP_LINK_MISSING

      A ``<property>`` element whose name matches a ``tr_property_link_types``
      entry does not result in a link on the imported need.

   .. fault:: Property link points to wrong target
      :id: ER_STR_PROP_LINK_WRONG

      The link created from a property points to a different need than the one
      named in the property value.

   .. fault:: Undeclared property link type causes silent failure
      :id: ER_STR_PROP_TYPE_UNDECLARED

      A property whose name is not in ``tr_property_link_types`` is silently
      ignored instead of raising a diagnostic, making misconfiguration
      invisible.

.. feature:: Configurable need types for imported results
   :id: FE_STR_CUSTOM_TYPES
   :tools: TOOL_STR
   :si: yes

   The need type used for imported test cases and test suites can be overridden
   via ``tr_case`` / ``tr_suite`` configuration, e.g. to use a dedicated
   ``testresult`` type with a distinct ID prefix and styling.

   .. fault:: Custom type is not applied to imported needs
      :id: ER_STR_CUSTOM_TYPE_IGNORED

      Imported test-case or test-suite needs use the default type even though
      ``tr_case`` or ``tr_suite`` was configured.

   .. fault:: Custom type ID prefix collision with existing needs
      :id: ER_STR_CUSTOM_TYPE_PREFIX_COLLISION

      The configured ID prefix for a custom type collides with IDs of
      pre-existing needs, causing duplicate-ID errors or silent overwrites.

.. feature:: Import test environment information
   :id: FE_STR_ENV_IMPORT
   :tools: TOOL_STR
   :si: no

   The ``test-env`` directive imports environment metadata produced by
   tox-envreport (Python version, packages, platform) as a Sphinx-Needs
   object for documentation purposes.

   .. fault:: Environment need is not created
      :id: ER_STR_ENV_MISSING

      The ``test-env`` directive does not produce a need despite a valid
      environment report file being present.

.. feature:: Filter and display test results
   :id: FE_STR_DISPLAY
   :tools: TOOL_STR
   :si: no

   The ``test-results`` and ``test-report`` directives create filtered tables
   and summaries of imported test results within the documentation.

   .. fault:: Test results table is empty despite imported data
      :id: ER_STR_DISPLAY_EMPTY

      The ``test-results`` directive renders an empty table even though
      matching testresult needs exist.
