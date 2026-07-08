
Sphinx-Test-Reports
===================

.. tool:: Sphinx-Test-Reports
   :id: TOOL_STR
   :version: 1.4.0
   :status: in_progress

   Sphinx extension to import test results from JUnit XML files as linkable
   :need:`TOOL_SN` objects into the documentation. Supports automatic
   generation of test-suite and test-case needs with configurable IDs, custom
   types, and property-based linking to existing Sphinx-Needs objects.

   :Documentation: https://sphinx-test-reports.readthedocs.io
   :Code: https://github.com/useblocks/sphinx-test-reports

Analysis
--------

.. needflow::
   :filter: "tools/sphinx-test-reports/" in docname

.. needtable::
   :filter: "tools/sphinx-test-reports/" in docname
   :columns: id, title, type

.. needpie:: Sphinx-Test-Reports objects
   :legend:
   :labels: Features, Faults, Restrictions, Checks, Tests, Test Results

   type == "feature" and "tools/sphinx-test-reports/" in docname
   type == "fault" and "tools/sphinx-test-reports/" in docname
   type == "restriction" and "tools/sphinx-test-reports/" in docname
   type == "check" and "tools/sphinx-test-reports/" in docname
   type == "test" and "tools/sphinx-test-reports/" in docname
   type == "testresult" and "tools/sphinx-test-reports/" in docname
