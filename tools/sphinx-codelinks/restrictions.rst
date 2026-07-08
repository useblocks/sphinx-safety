Restrictions
============

.. restriction:: Configuration files under version control
   :id: RE_SCL_CONFIG_IN_SCOPE
   :avoids: FAULT_SCL_CMT, FAULT_SCL_CLI_DISCOVER_1
   :tool: TOOL_SCL

   All Sphinx-CodeLinks configuration files (e.g., ``.codelinks.toml``, Sphinx ``conf.py``
   sections) must be placed under version control in the documented project scope.
   
   This ensures:
   
   - Custom comment styles are explicitly documented and tracked
   - Root directory configurations are versioned and auditable
   - Configuration changes are reviewed and traceable
   
   This mitigates:
   
   - **FAULT_SCL_CMT**: Configuration defines which comment styles are supported; 
     versioned config prevents undocumented style changes
   - **FAULT_SCL_CLI_DISCOVER_1**: Root directory paths are documented in versioned 
     config, making failures traceable

.. restriction:: Sphinx warnings break the build
   :id: RE_SCL_WARNINGS_BREAK_BUILD
   :avoids: FAULT_SCL_1, FAULT_SCL_CLI_ANALYZE_3
   :tool: TOOL_SCL

   The Sphinx build process must be configured with ``-W`` (warnings as errors) or
   ``-n`` (nitpick mode) to ensure any warnings from Sphinx-CodeLinks cause build 
   failure.
   
   This enforces:
   
   - Missing or undetected traceability objects trigger warnings → build fails
   - Incomplete content analysis is immediately visible
   - Zero tolerance for extraction issues
   
   This mitigates:
   
   - **FAULT_SCL_1**: Undetected traceability objects cause Sphinx-CodeLinks to emit
     warnings about missing references
   - **FAULT_SCL_CLI_ANALYZE_3**: Missed content results in incomplete need extraction,
     triggering warnings when referenced in documentation
