Features
========

.. dropdown:: 🔍 Features

   .. needtable::
      :filter: "tools/sphinx-codelinks/" in docname and type == "feature"
      :columns: id, title, si as "SI", parent_needs_back as "Errors"

   .. needpie:: Sphinx-CodeLinks features
      :legend:
      :labels: Safety impact, No impact, Undefined impact

      type == "feature" and "tools/sphinx-codelinks/" in docname and si == "yes"
      type == "feature" and "tools/sphinx-codelinks/" in docname and si == "no"
      type == "feature" and "tools/sphinx-codelinks/" in docname and si == ""

.. feature:: Define new traceability objects in source code
    :id: FE_SCL_DEF
    :tools: TOOL_SCL

    Create new Sphinx-Needs directly from a single comment line in your source code.

    .. fault:: Traceability objects are not detected in supported languages
        :id: FAULT_SCL_1

    .. fault:: Sphinx-codelinks halucinates traceability objects
       :id: FAULT_SCL_2

.. feature:: C Language Support
    :id: FE_SCL_C
    :tools: TOOL_SCL

    Support for defining traceability objects in C source code.

    .. fault:: Traceability objects are not detected in C language
       :id: FAULT_SCL_C_1

    .. fault:: Sphinx-codelinks halucinates traceability objects in C
       :id: FAULT_SCL_C_2

.. feature:: C++ Language Support
    :id: FE_SCL_CPP
    :tools: TOOL_SCL

    Support for defining traceability objects in C++ source code.

    .. fault:: Traceability objects are not detected in C++ language
       :id: FAULT_SCL_CPP_1

    .. fault:: Sphinx-codelinks halucinates traceability objects in C++
       :id: FAULT_SCL_CPP_2

.. feature:: Python Language Support
    :id: FE_SCL_PY
    :tools: TOOL_SCL

    Support for defining traceability objects in Python source code.

    .. fault:: Traceability objects are not detected in Python language
       :id: FAULT_SCL_PY_1

    .. fault:: Sphinx-codelinks halucinates traceability objects in Python
       :id: FAULT_SCL_PY_2

.. feature:: Customized comment styles
    :id: FE_SCL_CMT
    :tools: TOOL_SCL

    Support for different customized comment styles in source code.
    The comment structure can be defined in the configuration file.

    .. fault:: Customized comment styles are not detected in supported languages
       :id: FAULT_SCL_CMT

.. feature:: Link code to existing need items
    :id: FE_SCL_LNK
    :tools: TOOL_SCL

    Link code to existing need items without creating new ones, perfect for tracing
    implementations to requirements.

    .. fault:: Linking code to existing need items fails
       :id: FAULT_SCL_LNK_1

    .. fault:: Sphinx-codelinks links code to wrong need items
       :id: FAULT_SCL_LNK_2

.. feature:: Extract blocks of reStructuredText embedded within comments
    :id: FE_SCL_RST_EXTRACTION
    :tools: TOOL_SCL

    Extract blocks of reStructuredText embedded within comments, allowing you to
    include rich documentation with associated metadata right next to your code.

    .. fault:: Extracting reStructuredText from comments fails
       :id: FAULT_SCL_RST_EXTRACTION_1

    .. fault:: Sphinx-codelinks extracts wrong reStructuredText blocks
       :id: FAULT_SCL_RST_EXTRACTION_2

    .. fault:: Extracted reStructuredText blocks are malformed
       :id: FAULT_SCL_RST_EXTRACTION_3

.. feature:: Analyze marked content via CLI interface
    :id: FE_SCL_CLI_ANALYZE
    :tools: TOOL_SCL

    It shall be possible to analyze marked content via the CLI interface.

    .. fault:: CLI integration fails silently
       :id: FAULT_SCL_CLI_ANALYZE_1

    .. fault:: Sphinx-codelinks halucinates marked content
       :id: FAULT_SCL_CLI_ANALYZE_2

    .. fault:: Sphinx-codelinks misses marked content
       :id: FAULT_SCL_CLI_ANALYZE_3

.. feature:: Discover the filepaths a specified root directory via CLI interface
    :id: FE_SCL_CLI_DISCOVER
    :tools: TOOL_SCL

    It shall be possible to specify a root directory for the CLI interface.
    All files in and below this directory shall be discovered.

    .. fault:: Specifying a root directory fails
       :id: FAULT_SCL_CLI_DISCOVER_1

    .. fault:: Sphinx-codelinks discovers files outside the specified root directory
       :id: FAULT_SCL_CLI_DISCOVER_2

       Root directory setting is not respected or ignored

.. feature:: Export marked content to other formats via CLI interface
    :id: FE_SCL_CLI_WRITE
    :tools: TOOL_SCL

    It shall be possible to export marked content to other formats via the CLI interface.

    .. fault:: Exporting marked content fails
       :id: FAULT_SCL_CLI_WRITE_1

    .. fault:: Sphinx-codelinks exports wrong content
       :id: FAULT_SCL_CLI_WRITE_2

    .. fault:: Exported content is malformed
       :id: FAULT_SCL_CLI_WRITE_3
