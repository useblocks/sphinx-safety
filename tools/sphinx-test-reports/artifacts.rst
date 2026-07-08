Artifacts
=========

.. artifact:: JUnit XML test result file
   :id: ART_STR_JUNIT_XML

   A JUnit-compatible XML file produced by a test runner (e.g. pytest with
   ``--junitxml``). Contains ``<testsuite>`` and ``<testcase>`` elements with
   result status, timing, and optional ``<property>`` elements.

   Consumed by the ``test-file`` directive.
