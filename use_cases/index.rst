.. _`use_cases`:

:octicon:`briefcase` Use cases
==============================

The use cases below describe the safety-relevant usage of the toolchain.
Traceability is the central concern that connects all of them: every
requirement, architecture element, detailed design element, code location,
test case and test result is a traceability object, and the links between
these objects show which requirement is realised by which specification and
code, and which test verifies it. Traceability is therefore classified as a
use case of its own (:need:`UC_TRACEABILITY`), in addition to the use cases
that document the individual artifacts.

Traceability
------------

.. usecase:: Establish and verify traceability between development artifacts
   :id: UC_TRACEABILITY
   :inputs:
   :outputs:
   :tools: TOOL_SPHINX, TOOL_SN, TOOL_SCL, TOOL_STR, TOOL_UBC
   :features: FE_SPHINX_READ, FE_SN_READ, FE_SN_SET_META, FE_SN_LINK, FE_SN_CONTENT_RENDER, FE_SPHINX_NEEDS_CUSTOMIZABLE_LINKS, FE_SPHINX_NEEDS_LINKING_DIRECT, FE_SPHINX_NEEDS_LINKING_BIDIRECTIONAL, FE_SPHINX_NEEDS_LINKING_DEAD_LINK_DETECTION, FE_SN_TYPED_LINK_SCHEMA, FE_SN_SCHEMA_VALIDATION, FE_UBC_SCHEMA_VALIDATE, FE_SCL_LNK, FE_STR_PROPERTY_LINKS, FE_SPHINX_NEEDS_DIRECTIVE_NEEDTABLE, FE_SPHINX_NEEDS_DIRECTIVE_NEEDFLOW
   :ti: 2
   :tcl: [[calculate_tcl()]]

   Establish links between traceability objects across the development
   lifecycle and use these links as evidence of completeness and consistency:

   * requirements are linked to the architecture and detailed design elements
     that realise them,
   * source code is linked to the detailed design and requirements it
     implements,
   * test cases are linked to the requirements and design elements they
     verify,
   * test results are linked to the test cases they were produced by.

   Links are validated during the build (dead link detection, typed link
   schemas, schema validation) and presented as backlinks, traceability
   tables and flow diagrams, so that a reviewer can answer for every
   requirement which specification handles it, which code implements it and
   which test verifies it.

   An incorrect, missing or wrongly shown link can hide a requirement that is
   not implemented or not verified. The traceability documentation is used as
   part of an official release delivery.

Requirements
------------

.. usecase:: Document software requirements
   :id: UC_SW_REQ
   :status: done
   :inputs:
   :outputs:
   :tools: TOOL_SPHINX, TOOL_SN, TOOL_UBC
   :features: FE_SPHINX_READ, FE_SN_READ, FE_SN_CONTENT_RENDER, FE_SN_SET_META, FE_SN_LINK
   :ti: 2
   :tcl: [[calculate_tcl()]]
   :priority: 1
   :responsible:

   Create documentation to document and track software requirements.
   Input are ``rst`` files and output is a static website with ``HTML``, ``CSS``
   and ``JS`` files.

   The documentation is used as part of an official release delivery.

Architectures
-------------

.. usecase:: Document SW architecture
   :id: UC_SW_ARCH
   :outputs:
   :tools: TOOL_SPHINX, TOOL_SN
   :features: FE_SPHINX_READ, FE_SN_READ, FE_SN_SET_META, FE_SN_LINK, FE_SN_CONTENT_RENDER, FE_SPHINX_NEEDS_DIRECTIVE_NEEDFLOW, FE_SPHINX_NEEDS_DIRECTIVE_NEEDTABLE
   :ti: 2
   :tcl: [[calculate_tcl()]]

   Create documentation to document and track software architecture.

   The documentation is used as part of an official release delivery.

SW APIs
-------

.. usecase:: Document SW Detail Design (SW API)
   :id: UC_SW_API
   :outputs:
   :tools: TOOL_SPHINX, TOOL_SN
   :features: FE_SPHINX_READ, FE_SN_READ, FE_SN_SET_META, FE_SN_LINK, FE_SN_CONTENT_RENDER, FE_SCL_DEF, FE_SCL_LNK, FE_SCL_C, FE_SCL_CPP, FE_SCL_PY
   :ti: 2
   :tcl: [[calculate_tcl()]]

   Create documentation to document and track software detailed design.

   The documentation is used as part of an official release delivery.

Tests
-----

.. usecase:: Document SW Unit test cases
   :id: UC_UNIT_TEST
   :outputs:
   :tools: TOOL_SPHINX, TOOL_SN
   :features: FE_SPHINX_READ, FE_SN_READ, FE_SN_SET_META, FE_SN_LINK, FE_SN_CONTENT_RENDER, FE_SPHINX_NEEDS_DIRECTIVE_NEEDTABLE, FE_SCL_LNK
   :ti: 2
   :tcl: [[calculate_tcl()]]

   Create documentation to document and track software  unit test cases.

   The documentation is used as part of an official release delivery.

.. usecase:: Document Test results of SW Unit tests
   :id: UC_UNIT_TEST_RESULTS
   :outputs:
   :tools: TOOL_SPHINX, TOOL_SN
   :features: FE_SPHINX_READ, FE_SN_READ, FE_SN_LINK, FE_SPHINX_NEEDS_DIRECTIVE_NEEDPIE, FE_SPHINX_NEEDS_DIRECTIVE_NEEDBAR, FE_SPHINX_NEEDS_DIRECTIVE_NEEDTABLE
   :ti: 2
   :tcl: [[calculate_tcl()]]

   Document the result of certain test runs and link them to the related
   test cases. Create also test result overview pages with tables and pie
   charts.

   The documentation is used as part of an official release.

Qualifications
--------------

.. usecase:: Document software qualification tests and results
   :id: UC_SW_QA
   :inputs:
   :outputs:
   :tools: TOOL_SPHINX, TOOL_SN
   :features: FE_SPHINX_READ, FE_SN_READ, FE_SN_SET_META, FE_SN_LINK, FE_SN_CONTENT_RENDER, FE_SN_SCHEMA_VALIDATION, FE_UBC_SCHEMA_VALIDATE, FE_UBC_VALIDATE_JSON, FE_SPHINX_NEEDS_DIRECTIVE_NEEDTABLE
   :ti: 2
   :tcl: [[calculate_tcl()]]

   Create documentation to document software qualification.

   The documentation is used as part of an official release delivery.
