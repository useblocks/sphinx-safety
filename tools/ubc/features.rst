Features
========

.. dropdown:: 🔍 Features

   .. needtable::
      :filter: "tools/ubc/" in docname and type == "feature"
      :columns: id, title, si as "SI", parent_needs_back as "Errors"

   .. needpie:: ubc features
      :legend:
      :labels: Safety impact, No impact, Undefined impact
      
      type == "feature" and "tools/ubc/" in docname and si == "yes"
      type == "feature" and "tools/ubc/" in docname and si == "no"
      type == "feature" and "tools/ubc/" in docname and si == ""

.. feature:: Check rst files for linting problems
   :id: FE_UBC_LINTING
   :tools: TOOL_UBC
   :inputs: ART_SPHINX_RST
   :si: no

   .. fault:: Not covered format
      :id: ER_UBC_LINTING_NOT_COVERED

.. feature:: Format rst files
   :id: FE_UBC_FORMAT
   :tools: TOOL_UBC
   :si: yes

   .. fault:: Format introduces errors
      :id: ER_UBC_FORMAT_ERRORS

.. feature:: Clean internal caches
   :id: FE_UBC_CACHE
   :tools: TOOL_UBC
   :si: no

.. feature:: Build needs.json
   :id: FE_UBC_BUILD_JSON
   :tools: TOOL_UBC
   :inputs: ART_SPHINX_RST
   :outputs: ART_UBC_NEEDS_JSON
   :si: yes

   .. fault:: Incomplete data
      :id: ER_UBC_JSON_INCOMPLETE

      This can have several reasons:

      * Not supported or unknown Sphinx-Needs directives. Like

        * list2needs

      * Not supported features of Sphinx-Needs. Like

        * dynamic functions

      * Unknown script executions
      * Unknown/not accessible sources, like

        * external services
        * import of needs.json files
        * unknown rst files

.. feature:: Validate needs.json
   :id: FE_UBC_VALIDATE_JSON
   :tools: TOOL_UBC
   :inputs: ART_UBC_NEEDS_JSON
   :si: no

   .. fault:: Unknown file format
      :id: ER_UBC_VAL_FORMAT

   .. fault:: Incomplete Validation
      :id: ER_UBC_VAL_INCOMPLETE

      Not all types and options, which are represetned in a given needs.json
      file, are known/defined by the ``ubproject.toml`` configuration.
