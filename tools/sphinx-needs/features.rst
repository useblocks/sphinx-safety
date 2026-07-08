Features
========

.. dropdown:: 🔍 Features

   .. needtable::
      :filter: "tools/sphinx-needs/" in docname and type == "feature"
      :columns: id, title, si as "SI", parent_needs_back as "Faults"

   .. needpie:: Sphinx-Needs features
      :legend:
      :labels: Safety impact, No impact, Undefined impact
      
      type == "feature" and "tools/sphinx-needs/" in docname and si == "yes"
      type == "feature" and "tools/sphinx-needs/" in docname and si == "no"
      type == "feature" and "tools/sphinx-needs/" in docname and si == ""

.. feature:: Read Traceability objects in Sphinx-Needs
   :id: FE_SN_READ
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Read Traceability objects from rst/md files into the internal storage.

   .. fault:: Syntax errors in rst/md files cause Traceability objects to be ignored
      :id: ER_SN_SYN_ER

   .. fault:: Missing external needs.json file
      :id: ER_SN_JSON_NOT_FOUND

   .. fault:: Corrupted external needs.json file
      :id: ER_SN_JSON_CORRUPTED

   .. fault:: Authentication issues with needsservice
      :id: ER_SN_SER_AUTH

   .. fault:: Invalid meta-data in rst/md files leads to ignored Traceability objects
      :id: ER_SN_DATA_INVALID

   .. fault:: Programmatic errors in rst/md files result in ignored Traceability objects
      :id: ER_SN_CODE_ERR

   .. fault:: Invalid or incorrect filters used for external needs.json
      :id: ER_SN_JSON_FILTER

   .. fault:: External service unreachable by needsservice
      :id: ER_SN_SER_DOWN

   .. fault:: needsservice unable to process data from external service
      :id: ER_SN_SER_INVALID

.. feature:: Display Traceability objects content in Sphinx-Needs
   :id: FE_SN_CONTENT_RENDER
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Content contains syntax errors
      :id: ER_SN_CONTENT_SYNTAX

.. feature:: Assign meta-data to Traceability objects in Sphinx-Needs
   :id: FE_SN_SET_META
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Dynamic functions return invalid meta-data
      :id: ER_SN_DYN_INVALID

   .. fault:: Dynamic functions return wrong meta-data
      :id: ER_SN_DYN_WRONG

      Internal dynamic functions are checked by test-cases in Sphinx-Needs
      itself.

      But self-written dynamic functions can do whatever they want, as long
      as the returned data ist still valid (but may be wrong).

      So self-written dynamic functions need test cases as well!

   .. fault:: Sphinx-Needs data not valid
      :id: ER_SN_META_INVALID

   .. fault:: Sphinx-Needs data is not process-compliant
      :id: ER_SN_META_NOT_COMPLIANT

.. feature:: Establish links between Traceability objects in Sphinx-Needs
   :id: FE_SN_LINK
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Back-links are not set
      :id: ER_SN_LINKS_NO_BACK

      Links are set only in one direction but not in the other.

      This may lead to missing information, e.g. a Traceability object is
      linked to a specification, but you can't find the linked Traceability
      object during specification implementation.

   .. fault:: Internal target link is not found
      :id: ER_SN_LINKS_NO_TARGET

   .. fault:: External needs not found
      :id: ER_SN_LINKS_NO_EXT

   .. fault:: External needs corrupted
      :id: ER_SN_LINKS_EXT_COR

   .. fault:: Links missing
      :id: ER_SN_LINKS_MISSING

      Set links are not treated correctly and are not part of the final
      documentation.

      Sphinx-Needs shows a warning for all not found used need-IDs for
      links.

.. feature:: Generate object representation in Sphinx-Needs
   :id: FE_SN_DOCTREE
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Meta-data missing
      :id: ER_SN_LAY_META_MIS

      Needed meta-data is not part of the final representation in the
      doctree and so later HTML/PDF build

   .. fault:: Wrong meta-data is used
      :id: ER_SN_LAY_META_WRONG

      Sphinx-Needs is adding wrong Meta-Data to the final doctree-layout

.. feature:: Export needs.json file using Sphinx-Needs
   :id: FE_SN_JSON
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Objects missing in needs.json
      :id: ER_SN_JSON_MIS

   .. fault:: Traceability objects meta-data corrupted
      :id: ER_SN_JSON_COR

   .. fault:: Traceability objects links corrupted
      :id: ER_SN_JSON_LINKS_COR

   .. fault:: Traceability objects content corrupted
      :id: ER_SN_JSON_CONTENT_COR
      

Dynamic Content
+++++++++++++++

.. feature:: Apply dynamic functions for meta-data computation
   :id: FE_SN_DYN_FUNC
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Function gets not executed
      :id: ER_SN_DYN_NO_EXEC

      The function gets not executed and in the generated documentation the
      dynamic-function string can be found.

   .. fault:: Function returns invalid value
      :id: ER_SN_DYN_INVALID2

      Function returns a technically not allowed value.

   .. fault:: Function returns wrong calculated values
      :id: ER_SN_DYN_WRONG_CALC

      The dynamic functions calculates wrong values

   .. fault:: Function returns no value
      :id: ER_SN_DYN_NO_VALUE

      The dynamic function does not return a value, so the meta-data is not
      set.

.. feature:: Extend page content with templates in Sphinx-Needs
   :id: FE_SN_TEMPLATE_PAGE
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Template file not found
      :id: ER_SN_TEMPLATE_FILE_NOT_FOUND

      The template file is not found in the Sphinx-Needs templates directory.

   .. fault:: Template file is not a valid Jinja2 template
      :id: ER_SN_TEMPLATE_FILE_INVALID

      The template file is not a valid Jinja2 template, so it cannot be
      processed by Sphinx-Needs.

   .. fault:: Template file contains syntax errors
      :id: ER_SN_TEMPLATE_FILE_SYNTAX

      The template file contains syntax errors and cannot be processed by
      Sphinx-Needs.

.. feature:: Enhance Need content using templates in Sphinx-Needs
   :id: FE_SN_TEMPLATE_NEED
   :tools: TOOL_SN
   :si: yes
   :td: 3

   .. fault:: Template file not found
      :id: ER_SN_TEMPLATE_NEED_FILE_NOT_FOUND

      The template file is not found in the Sphinx-Needs templates directory.

   .. fault:: Template file is not a valid Jinja2 template
      :id: ER_SN_TEMPLATE_NEED_FILE_INVALID

      The template file is not a valid Jinja2 template, so it cannot be
      processed by Sphinx-Needs.

   .. fault:: Template file contains syntax errors
      :id: ER_SN_TEMPLATE_NEED_FILE_SYNTAX

      The template file contains syntax errors and cannot be processed by
      Sphinx-Needs.

Core Need Object
++++++++++++++++

.. feature:: Definable need types
   :id: FE_SPHINX_NEEDS_DEFINABLE_TYPES
   :tools: TOOL_SN
   :si: yes
   :td: 1

   Allows the definition of custom need types beyond the built-in ones.
   Each type gets its own directive, title, and color for easy
   identification in diagrams.

   .. code-block:: python

      # In conf.py
      needs_types = [
          dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2"),
          dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2"),
          dict(directive="test", title,"Test Case", prefix="T_", color="#DCFED2"),
      ]

.. feature:: Customizable need fields
   :id: FE_SPHINX_NEEDS_CUSTOMIZABLE_OPTIONS
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Define extra fields that any need object can have, such as ``author``
   or ``component``. Custom fields can be displayed in tables, used for
   filtering, and (since Sphinx-Needs 7) validated by an attached JSON
   Schema.

   The legacy list-style ``needs_extra_options`` configuration is
   deprecated; declarative ``needs_fields`` (``[needs.fields.<name>]``
   in ``ubproject.toml``) is the supported form.

   .. code-block:: toml

      # In ubproject.toml
      [needs.fields.author]
      description = "Author of the need"
      schema.type = "string"

      [needs.fields.component]
      description = "Logical sub-system the need belongs to"
      schema.type = "string"
      schema.enum = ["UI", "Backend", "Database"]

   .. code-block:: rst

      .. req:: A specific requirement
         :id: R_001
         :author: John Doe
         :component: UI

   .. fault:: Invalid field used in a need
      :id: ER_SN_INVALID_OPTION

      A field that is not defined in ``needs_fields`` is used in a
      directive. Sphinx-Needs raises a warning during the build.

   .. fault:: Field value does not match declared schema
      :id: ER_SN_INVALID_OPTION_VALUE

      A field value does not match the declared ``schema.type``,
      ``schema.enum``, ``schema.minimum`` / ``maximum`` or ``schema.pattern``.
      Sphinx-Needs emits a ``sn_schema_violation`` during the build.

   .. fault:: Field value is not allowed
      :id: ER_SN_OPTION_NOT_ALLOWED

      A field value is not part of the allowed ``schema.enum`` list.
      Without schema validation the wrong value silently reaches the
      exported ``needs.json`` and downstream analysis.

.. feature:: Customizable link types
   :id: FE_SPHINX_NEEDS_CUSTOMIZABLE_LINKS
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Define different types of links between needs to represent various
   relationships. This is the foundation of a precise traceability
   model.

   The legacy ``needs_extra_links`` list form is deprecated since
   Sphinx-Needs 7; link types are declared as ``needs_links`` dicts
   (``[needs.links.<name>]`` in ``ubproject.toml``) and can carry an
   optional ``schema`` block for cardinality / typing constraints.

   .. code-block:: toml

      # In ubproject.toml
      [needs.links.verifies]
      incoming = "verified by"
      outgoing = "verifies"
      schema.minItems = 1          # every need using :verifies: must link at least one target

      [needs.links.implements]
      incoming = "implemented by"
      outgoing = "implements"

   .. fault:: Invalid link type used in a need
      :id: ER_SN_INVALID_LINK_TYPE

      A link option is used in a directive that is not declared in
      ``needs_links``. Sphinx-Needs raises a warning during the build.

   .. fault:: Link target value violates link schema
      :id: ER_SN_INVALID_LINK_TYPE_VALUE

      The set of targets assigned to a link field violates the declared
      ``schema`` (e.g. ``maxItems``, ``minItems``, ``uniqueItems``),
      leading to an ``sn_schema_violation`` warning.

.. feature:: Automatic ID generation
   :id: FE_SPHINX_NEEDS_AUTO_ID
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Sphinx-Needs can automatically generate a unique ID for any need that
   does not have one. The format of the ID can be configured using a
   prefix and a specific length.

   .. code-block:: rst

      .. req:: This requirement will get an ID automatically.
         :tags: auto_id

   .. fault:: ID generation failed
      :id: ER_SN_ID_GENERATION_FAILED

      If the automatic ID generation fails, Sphinx-Needs will raise an error
      during the build process.

   .. fault:: ID already exists
      :id: ER_SN_ID_ALREADY_EXISTS

      If the generated ID already exists in the project, Sphinx-Needs will
      raise an error during the build process.

   .. fault:: ID format is invalid
      :id: ER_SN_ID_FORMAT_INVALID

      If the generated ID does not match the expected format, Sphinx-Needs will
      raise an error during the build process.

   .. fault:: ID length is invalid
      :id: ER_SN_ID_LENGTH_INVALID

      If the generated ID does not match the expected length, Sphinx-Needs will
      raise an error during the build process.

.. feature:: Manual ID assignment
   :id: FE_SPHINX_NEEDS_MANUAL_ID
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Allows for setting a specific, human-readable ID for a need. This is
   useful for referencing important requirements easily.

   .. code-block:: rst

      .. req:: A requirement with a specific ID
         :id: R_IMPORTANT_FEATURE

   .. fault:: Manual ID already exists
      :id: ER_SN_MANUAL_ID_EXISTS

      If a manually set ID already exists in the project, Sphinx-Needs will
      raise an error during the build process.

   .. fault:: Manual ID format is invalid
      :id: ER_SN_MANUAL_ID_FORMAT_INVALID

      If a manually set ID does not match the expected format, Sphinx-Needs will
      raise an error during the build process.

   .. fault:: Manual ID length is invalid
      :id: ER_SN_MANUAL_ID_LENGTH_INVALID

      If a manually set ID does not match the expected length, Sphinx-Needs will
      raise an error during the build process.

.. feature:: Need status enforcement
   :id: FE_SPHINX_NEEDS_STATUS_ENFORCEMENT
   :tools: TOOL_SN
   :si: yes
   :td: 3

   You can define a list of allowed statuses for needs. If a need uses a
   status that is not on the list, Sphinx will raise a warning during the
   build.

   .. code-block:: python

      # In conf.py
      needs_statuses = [
          ('open', 'Is still open'),
          ('in_progress', 'Work in progress'),
          ('closed', 'Is closed'),
          ('rejected', 'Will not be implemented'),
      ]

   .. fault:: Invalid status used in a need
      :id: ER_SN_INVALID_STATUS

      If a need uses a status that is not defined in the configuration,
      Sphinx-Needs will raise an error during the build process.

.. feature:: Tagging support
   :id: FE_SPHINX_NEEDS_TAGGING
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Assign one or more tags to a need for categorization and filtering.
   Tags help in organizing needs and creating specific views or reports.

   .. code-block:: rst

      .. spec:: A specification for the login system
         :id: S_LOGIN
         :tags: ui, security

.. feature:: In-content need parts for granular references
   :id: FE_SPHINX_NEEDS_NEED_PARTS
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Create references to specific sentences or parts inside a need's
   content. This allows for very precise linking and traceability.

   .. code-block:: rst

      .. req:: User Authentication
         :id: R_AUTH

         The user must be able to log in via a username and password.
         The password must be stored securely. :np:`secure_storage`

      .. test:: Test secure password storage
         :id: T_SECURE_STORAGE
         :links: R_AUTH.secure_storage

.. feature:: Unique ID enforcement and checks
   :id: FE_SPHINX_NEEDS_UNIQUE_ID_ENFORCEMENT
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Sphinx-Needs automatically checks if all manually set IDs are unique
   across the project. The build will fail if a duplicate ID is found,
   ensuring data consistency.

   .. fault:: Duplicate ID is not detected
      :id: ER_SN_DUPLICATE_ID

      If a duplicate ID is not detected, it may lead to incorrect traceability
      and data integrity issues. 

Directives for Creating & Displaying Needs
++++++++++++++++++++++++++++++++++++++++++

.. feature:: Display needs in a filterable table (needtable)
   :id: FE_SPHINX_NEEDS_DIRECTIVE_NEEDTABLE
   :tools: TOOL_SN
   :si: no

   Renders a table of needs based on specified filters. The table columns
   can be customized to show different need options like status or
   outgoing links.

   .. code-block:: rst

      .. needtable::
         :tags: ui
         :status: open
         :columns: id, title, status, links

.. feature:: Render a PlantUML flow diagram of needs (needflow)
   :id: FE_SPHINX_NEEDS_DIRECTIVE_NEEDFLOW
   :tools: TOOL_SN
   :si: no

   Generates a flowchart that visualizes the relationships between
   filtered needs. This is excellent for showing process flows or
   dependencies.

   .. code-block:: rst

      .. needflow::
         :tags: login_flow
         :show_legend:

.. feature:: Create a pie chart based on need statistics (needpie)
   :id: FE_SPHINX_NEEDS_DIRECTIVE_NEEDPIE
   :tools: TOOL_SN
   :si: no

   Generates a pie chart from need data, for instance, to show the
   distribution of statuses. This provides a quick visual summary of the
   project's state.

   .. code-block:: rst

      .. needpie:: Requirements Status
         :content: status
         :legend:

.. feature:: Create a bar chart based on need statistics (needbar)
   :id: FE_SPHINX_NEEDS_DIRECTIVE_NEEDBAR
   :tools: TOOL_SN
   :si: no

   Generates a bar chart to visualize need data. This is useful for
   comparing counts across different categories, such as components.

   .. code-block:: rst

      .. needbar:: Needs per Component
         :x_option: component
         :x_labels: UI, Backend, Database

.. feature:: Import needs from an external JSON file (needimport)
   :id: FE_SPHINX_NEEDS_DIRECTIVE_NEEDIMPORT
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Import need objects from an external ``needs.json`` file. This allows
   for sharing and reusing requirements across different Sphinx projects.

   .. code-block:: rst

      .. needimport:: ../../shared/output/needs.json

   .. fault:: Importing needs is not completed
      :id: ER_SN_IMPORT_NOT_COMPLETED
      

      If the import process is not completed, it may lead to missing or
      incomplete data in the project.

   .. fault:: Importing needs is not valid
      :id: ER_SN_IMPORT_NOT_VALID
      

      If the imported data is not valid, it may lead to errors in the
      documentation or incorrect traceability.

   .. fault:: Importing needs is not accessible
      :id: ER_SN_IMPORT_NOT_ACCESSIBLE
      

      If the imported file is not accessible, it may lead to errors in the
      documentation or missing data.

.. feature:: Modify existing needs in bulk (needextend)
   :id: FE_SPHINX_NEEDS_DIRECTIVE_NEEDEXTEND
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Modifies multiple needs at once based on a filter. You can add tags,
   change the status, or set any other option for all filtered needs.

   .. code-block:: rst

      .. needextend:: status == 'in_progress'
         :add_tags: sprint_5

   .. fault:: Bulk modification of needs is not completed
      :id: ER_SN_EXTEND_NOT_COMPLETED
      

      If the bulk modification process is not completed, it may lead to
      missing or incomplete data in the project.

   .. fault:: Bulk modification failes silently
      :id: ER_SN_EXTEND_FAIL_SILENTLY
      

      If the bulk modification fails silently, it may lead to missing or
      incomplete data in the project without any error message.

   .. fault:: Bulk modification of needs is not valid
      :id: ER_SN_EXTEND_NOT_VALID
      

      If the bulk modification is not valid, it may lead to errors in the
      documentation or incorrect traceability.

Linking and Traceability
++++++++++++++++++++++++

.. feature:: Direct linking between needs using IDs
   :id: FE_SPHINX_NEEDS_LINKING_DIRECT
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Create links between needs by referencing their unique IDs in link
   options. This forms the basis of all traceability in Sphinx-Needs.

   .. code-block:: rst

      .. spec:: Defines how the login button works.
         :id: S_LOGIN_BUTTON

      .. req:: The login button must be blue.
         :id: R_LOGIN_COLOR
         :links: S_LOGIN_BUTTON

   .. fault:: Link target not found
      :id: ER_SN_LINK_TARGET_NOT_FOUND
      

      If a link target is not found, it may lead to missing traceability
      and incorrect documentation.

   .. fault:: Link target is not valid
      :id: ER_SN_LINK_TARGET_NOT_VALID
      

      If a link target is not valid, it may lead to errors in the
      documentation or incorrect traceability.

.. feature:: Bidirectional link tracking
   :id: FE_SPHINX_NEEDS_LINKING_BIDIRECTIONAL
   :tools: TOOL_SN
   :si: yes
   :td: 1

   When you link from need A to need B, Sphinx-Needs automatically knows
   about the incoming link on need B. This allows for full, bidirectional
   traceability without extra work.

.. feature:: Dead link detection and warnings
   :id: FE_SPHINX_NEEDS_LINKING_DEAD_LINK_DETECTION
   :tools: TOOL_SN
   :si: yes
   :td: 3

   The Sphinx build will issue a warning if a need links to an ID that
   does not exist. This helps to maintain the integrity of the
   traceability data.

   .. fault:: Dead link not detected
      :id: ER_SN_DEAD_LINK_NOT_DETECTED


      If a dead link is not detected, it may lead to missing traceability
      and incorrect documentation.

   .. fault:: Dead link false positive
      :id: ER_SN_DEAD_LINK_FALSE_POSITIVE


      If a dead link is falsely reported, it may lead to unnecessary warnings
      and confusion in the documentation.

.. feature:: Conditional link evaluation (NeedLink, parse_conditions)
   :id: FE_SN_LINK_CONDITIONS
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Introduced with Sphinx-Needs 8.0, a link target can carry an
   inline filter expression
   (``:links: FEAT_X[status=="done"]``) that is evaluated during the
   build. Conditional links are represented internally by the
   structured ``NeedLink`` object, enabling downstream analysis of
   *which* links are active under *which* conditions.

   A link type opts in via ``parse_conditions = true`` in its
   ``[needs.links.<name>]`` entry.

   .. code-block:: toml

      [needs.links.verifies]
      incoming = "verified by"
      outgoing = "verifies"
      parse_conditions = true

   .. code-block:: rst

      .. test:: Integration test for login feature
         :id: T_LOGIN
         :verifies: FE_LOGIN[status=="released"]

   .. fault:: Condition expression parse error
      :id: ER_SN_LINK_COND_PARSE

      The expression inside the link condition is syntactically
      invalid or references an undefined field. Sphinx-Needs reports
      a warning, but if the warning is ignored the link is dropped
      from the traceability, silently reducing coverage.

   .. fault:: Condition evaluates to the wrong result
      :id: ER_SN_LINK_COND_EVAL_WRONG

      The predicate references a mutable field (``status``, ``tags``)
      whose value changes between the authoring and audit state of
      the documentation. The evaluated link set therefore differs
      from the one intended by the author.

   .. fault:: Condition hides a safety-relevant link
      :id: ER_SN_LINK_COND_HIDES_SAFE

      A conditional filter excludes a link that should be active for
      safety reasons (e.g. a test verifying a fault is conditioned on
      ``status == "released"`` but the fault is already safety-
      relevant in earlier states). Coverage reports under-represent
      the traceability.

   .. fault:: Condition opt-in missing
      :id: ER_SN_LINK_COND_NOT_PARSED

      The link type is used with an inline condition, but
      ``parse_conditions = true`` is not set on the
      ``[needs.links.<name>]`` entry. The bracket expression is
      treated as part of the target ID, leading to a dead link or an
      unintended target.

Automated Features
++++++++++++++++++

.. feature:: Legacy constraint checking (needs_constraints)
   :id: FE_SPHINX_NEEDS_DYNAMIC_CONSTRAINTS
   :tools: TOOL_SN
   :si: yes
   :td: 1

   .. warning::

      ``needs_constraints`` is the **legacy** mechanism to validate need
      data through Python check-code strings. Since Sphinx-Needs 7 it
      is superseded by :need:`FE_SN_SCHEMA_VALIDATION` (JSON-Schema
      based) which is declarative, cacheable, and auditable.
      New classifications **should not** rely on ``needs_constraints``.

   Define rules about your need data that are checked during the
   build. For example, you can enforce that every requirement must be
   linked to a test case.

   .. code-block:: python

      # Legacy form in conf.py (avoid for new projects)
      needs_constraints = {
          "req_verified": {
              "check_code": "len(links_back['verifies']) > 0",
              "severity": "fault",
              "filter": "'req' in tags"
          }
      }

   .. fault:: Constraint not checked during build
      :id: ER_SN_CONSTRAINT_NOT_CHECKED

      If a constraint is not checked during the build, it may lead to
      missing or incorrect traceability data.

   .. fault:: Constraint check fails silently
      :id: ER_SN_CONSTRAINT_FAIL_SILENTLY

      If a constraint check fails silently, it may lead to missing or
      incorrect traceability data without any error message.

   .. fault:: Constraint check runs with wrong data
      :id: ER_SN_CONSTRAINT_WRONG_DATA

      If a constraint check runs with wrong data, it may lead to incorrect
      traceability data and errors in the documentation.

   .. fault:: Constraint check runs with incomplete data
      :id: ER_SN_CONSTRAINT_INCOMPLETE_DATA


      If a constraint check runs with incomplete data, it may lead to
      missing or incorrect traceability data and errors in the documentation.

   .. fault:: Constraint check runs with invalid data
      :id: ER_SN_CONSTRAINT_INVALID_DATA

      If a constraint check runs with invalid data, it may lead to errors in
      the documentation or incorrect traceability.

.. feature:: Declarative schema validation of needs
   :id: FE_SN_SCHEMA_VALIDATION
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Introduced with Sphinx-Needs 7 and hardened in 8.0, schema
   validation expresses data rules declaratively using a JSON-Schema
   derived format. Rules are defined once, evaluated per build, and
   produce structured diagnostics that downstream tools (ubCode,
   ``ubc schema validate``, CI) can consume.

   A schema object consists of three parts:

   * ``select`` — which needs the rule applies to
     (types, fields, combinations).
   * ``validate.local`` — property constraints on a single need
     (type, enum, pattern, min / max, required).
   * ``validate.network`` — cross-need constraints along link types
     (``contains``, ``minContains``, ``maxContains``), enabling
     traceability completeness checks (e.g. "every safe feature must
     have at least one test").
   * ``severity`` — ``violation`` (build fails), ``warning`` or
     ``info``.

   Safety-critical projects (ISO 26262, IEC 61508, EN 50716) use the
   ``violation`` severity to make an incomplete classification
   reject the build.

   .. code-block:: toml

      # In ubproject.toml
      schema_definitions_from_json = "schemas.json"
      schema_debug_active = true

   .. code-block:: json

      {
        "$defs": {
          "type-feature": { "properties": { "type": { "const": "feature" } } },
          "safe-feature": {
            "allOf": [
              { "$ref": "#/$defs/type-feature" },
              { "properties": { "si": { "const": "yes" } },
                "required": ["si"] }
            ]
          }
        },
        "schemas": [
          {
            "id": "safe-feature-has-fault",
            "severity": "violation",
            "message": "A safety-impacting feature must raise at least one fault",
            "select": { "$ref": "#/$defs/safe-feature" },
            "validate": {
              "network": {
                "raises": { "contains": { "local": {} }, "minContains": 1 }
              }
            }
          }
        ]
      }

   .. fault:: Schema validation silently disabled
      :id: ER_SN_SCHEMA_DISABLED

      ``needs_schema_validation_enabled`` is set to ``False`` (or
      implicitly disabled by a configuration error) without the
      project being aware. Safety-relevant rules are not enforced
      during the build.

   .. fault:: Schema definition itself is invalid
      :id: ER_SN_SCHEMA_INVALID

      The supplied ``needs_schema_definitions`` (or external
      ``schema_definitions_from_json``) does not conform to the
      JSON-Schema dialect accepted by Sphinx-Needs. Rules are not
      evaluated and the project silently loses validation coverage.

   .. fault:: Schema ``select`` does not match the intended needs
      :id: ER_SN_SCHEMA_SELECT_WRONG

      The ``select`` filter of a rule is too narrow or too broad,
      so the rule either misses safety-relevant needs (false negative)
      or fires on unrelated needs (false positive).

   .. fault:: Schema violation not surfaced in build
      :id: ER_SN_SCHEMA_NOT_REPORTED

      A failing schema rule does not produce a user-visible warning
      or error (e.g. because the category is listed in
      ``suppress_warnings`` or ``-W`` is not used). The build appears
      green although safety rules are violated.

   .. fault:: Schema violation wrongly suppressed via severity
      :id: ER_SN_SCHEMA_WRONG_SEVERITY

      A rule is declared with ``severity = "info"`` or ``"warning"``
      although it encodes a safety-relevant invariant. The violation
      does not fail the build.

   .. fault:: Network validation misses indirect links
      :id: ER_SN_SCHEMA_NETWORK_MISS

      A ``validate.network`` rule expects linkage via a specific
      ``needs.links.<name>``, but the project uses a different link
      option for the same semantic relation, so the check silently
      passes with zero matches.

.. feature:: Typed need fields with JSON-Schema validation
   :id: FE_SN_TYPED_FIELDS
   :tools: TOOL_SN
   :si: yes
   :td: 1

   Each custom field declared via ``[needs.fields.<name>]`` can carry
   a ``schema`` block (``type``, ``enum``, ``minimum`` / ``maximum``,
   ``pattern``, ``format``) and a ``nullable`` flag. Value mismatches
   are reported as ``sn_schema_violation`` warnings and written to
   ``schema_violations.json`` in the build output.

   This is the type-safe successor to the untyped string list form of
   ``needs_extra_options``.

   .. code-block:: toml

      [needs.fields.asil]
      description = "Automotive Safety Integrity Level (ISO 26262)"
      schema.type = "string"
      schema.enum = ["QM", "A", "B", "C", "D"]

      [needs.fields.efforts]
      description = "FTE days"
      schema.type = "integer"
      schema.minimum = 0
      schema.maximum = 100

   .. fault:: Schema type mismatch not detected
      :id: ER_SN_TYPED_FIELD_TYPE_MISS

      An integer-typed field receives a non-numeric value but the
      violation is not reported (e.g. schema validation disabled or
      category suppressed).

   .. fault:: Enum constraint not enforced
      :id: ER_SN_TYPED_FIELD_ENUM_MISS

      A value outside the declared ``schema.enum`` list is accepted
      silently, so an invalid ASIL / TCL value reaches the exported
      ``needs.json``.

   .. fault:: Range constraint not enforced
      :id: ER_SN_TYPED_FIELD_RANGE_MISS

      A value violates ``schema.minimum`` / ``schema.maximum`` but is
      accepted. Safety metrics derived from this field are wrong.

.. feature:: Typed link schemas (cardinality and targeting)
   :id: FE_SN_TYPED_LINK_SCHEMA
   :tools: TOOL_SN
   :si: yes
   :td: 3

   ``[needs.links.<name>]`` supports a ``schema`` block that
   constrains the array of link targets (``minItems``, ``maxItems``,
   ``uniqueItems``). Combined with
   :need:`FE_SN_SCHEMA_VALIDATION` ``validate.network`` rules this
   expresses completeness constraints (e.g. "every fault must be
   mitigated by at least one restriction or check").

   .. code-block:: toml

      [needs.links.avoids]
      incoming = "avoided by"
      outgoing = "avoids"
      schema.minItems = 1

   .. fault:: Link cardinality not enforced
      :id: ER_SN_TYPED_LINK_CARD_MISS

      A need uses a typed link without meeting the ``minItems`` /
      ``maxItems`` constraint, but the violation is not reported.
      Traceability completeness is silently broken.

   .. fault:: Typed link accepts wrong target type
      :id: ER_SN_TYPED_LINK_TARGET_WRONG

      A ``validate.network`` rule on a link does not fully constrain
      the target type, so a link intended to point at e.g. a
      ``fault`` can target an unrelated type.

Configuration & Customization
+++++++++++++++++++++++++++++

.. feature:: Configuration via conf.py or an external TOML file
   :id: FE_SPHINX_NEEDS_CONFIG_FILES
   :tools: TOOL_SN
   :si: no

   All Sphinx-Needs options can be configured in the main ``conf.py`` file.
   For large configurations, you can also use an external ``needs.toml``
   file to keep things organized.

.. feature:: Customizable layouts for need presentation
   :id: FE_SPHINX_NEEDS_CONFIG_LAYOUTS
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Change the visual presentation of needs by defining custom layouts.
   You can reorder options, use grids, and change how information is
   displayed.

   .. code-block:: python

      # In conf.py
      needs_layouts = {
          'my_layout': {
              'grid': 'simple_side_right',
              'layout': {
                  'side': ['id', 'status', 'tags', 'links']
              }
          }
      }

   .. fault:: Layout leads to incorrect rendering
      :id: ER_SN_LAYOUT_INCORRECT_RENDERING

      If a layout leads to incorrect rendering, it may cause confusion in the
      documentation and make it hard to read.

   .. fault:: Layout leads to missing information
      :id: ER_SN_LAYOUT_MISSING_INFO

      If a layout leads to missing information, it may cause confusion in the
      documentation and make it hard to read.

   .. fault:: Layout leads to incorrect information
      :id: ER_SN_LAYOUT_INCORRECT_INFO

      If a layout leads to incorrect information, it may cause confusion in the
      documentation and make it hard to read.

Exporting & Reporting
+++++++++++++++++++++

.. feature:: JSON builder to export all need data
   :id: FE_SPHINX_NEEDS_EXPORT_JSON
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Export all need objects and their relationships into a structured ``needs.json``
   file. This file can be used for external analysis, reporting, or
   imported into other Sphinx projects.

   .. code-block:: bash

      sphinx-build -b needs . _build

   .. fault:: Exporting needs.json fails silently
      :id: ER_SN_EXPORT_JSON_FAIL_SILENTLY

      If the export fails silently, it may lead to missing or incomplete data
      in the project without any error message.

   .. fault:: Exported needs.json file is not valid
      :id: ER_SN_EXPORT_JSON_NOT_VALID

      If the exported needs.json file is not valid, it may lead to errors in
      the documentation or incorrect traceability. 

   .. fault:: Exported needs.json file is corrupted
      :id: ER_SN_EXPORT_JSON_CORRUPTED

      If the exported needs.json file is corrupted, it may lead to errors in
      the documentation or incorrect traceability.

.. feature:: Link conditions exported to needs.json
   :id: FE_SN_JSON_LINK_CONDITIONS
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Added in Sphinx-Needs 8.0, ``needs_json_include_link_conditions``
   (default ``True``) controls whether link-condition expressions are
   included in the exported outgoing link fields of ``needs.json``.
   When enabled, downstream analysis tools (``ubc build
   validate-json``, audit scripts) can reason about the exact set of
   targets under each condition.

   .. code-block:: toml

      [needs]
      build_json = true
      json_include_link_conditions = true

   .. fault:: Link conditions missing in needs.json
      :id: ER_SN_JSON_LINK_COND_MISSING

      ``needs_json_include_link_conditions`` is disabled, so
      downstream tools see only the target IDs. Conditional filtering
      is lost from the audit artefact and cannot be reproduced from
      ``needs.json`` alone.

   .. fault:: Exported link conditions differ from runtime evaluation
      :id: ER_SN_JSON_LINK_COND_DRIFT

      The exported condition string is out of sync with the
      condition evaluated during the build (e.g. because
      post-processing rewrote fields). The JSON artefact misrepresents
      the state of traceability.

.. feature:: Permalink generation to specific need objects
   :id: FE_SPHINX_NEEDS_EXPORT_PERMALINKS
   :tools: TOOL_SN
   :si: yes
   :td: 3

   Generate a ``needs.json`` file where each need includes a permalink to
   its location in the HTML documentation. This is useful for linking
   from external tools directly to the requirement definition.

   .. fault:: Permalink generation fails silently
      :id: ER_SN_PERMALINK_FAIL_SILENTLY
      

      If the permalink generation fails silently, it may lead to missing or
      incomplete data in the project without any error message.

   .. fault:: Permalink is not valid
      :id: ER_SN_PERMALINK_NOT_VALID

      If the permalink is not valid, it may lead to errors in the
      documentation or incorrect traceability.

   .. fault:: Permalink links to non-existing need
      :id: ER_SN_PERMALINK_NON_EXISTING

      If the permalink links to a non-existing need, it may lead to errors in
      the documentation or incorrect traceability.

   .. fault:: Permalink links to wrong need
      :id: ER_SN_PERMALINK_WRONG_NEED

      If the permalink links to the wrong need, it may lead to errors in the
      documentation or incorrect traceability.
