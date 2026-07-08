Features
========

.. dropdown:: 🔍 Features

   .. needtable::
      :filter: "tools/ubc/" in docname and type == "feature"
      :columns: id, title, si as "SI", parent_needs_back as "Faults"

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

.. feature:: Validate ontology schema (``ubc schema validate``)
   :id: FE_UBC_SCHEMA_VALIDATE
   :tools: TOOL_UBC
   :inputs: ART_SPHINX_RST, ART_UBC_NEEDS_JSON
   :si: yes

   Runs the same JSON-Schema-based rules that power
   :need:`FE_SN_SCHEMA_VALIDATION` from the command line, independent
   of a Sphinx build. This is the primary CI gate for a safety
   qualification: the same rules that pass during ``sphinx-build``
   are re-evaluated against the published ``needs.json`` to detect
   drift.

   .. code-block:: bash

      ubc schema validate

   .. fault:: Schema rules not loaded
      :id: ER_UBC_SCHEMA_NO_RULES

      ``ubc`` cannot find the schema definitions referenced by
      ``needs_schema_definitions`` / ``schema_definitions_from_json``
      and therefore validates against an empty rule set. Exit code is
      ``0`` and the pipeline passes, but no safety rule is actually
      enforced.

   .. fault:: Schema rule set diverges from Sphinx-Needs
      :id: ER_UBC_SCHEMA_DIVERGE

      The version of the schema evaluation engine embedded in ``ubc``
      differs from the one used by the installed Sphinx-Needs, so a
      rule accepted in one tool is rejected in the other. The audit
      artefact becomes ambiguous.

   .. fault:: Safety violation reported only as warning
      :id: ER_UBC_SCHEMA_EXIT_ZERO

      ``ubc schema validate`` reports violations but returns exit
      code ``0`` (e.g. severity configured as ``warning`` only). CI
      does not fail and the safety breach reaches release.

.. feature:: Impact analysis on git changes (``ubc diff git``)
   :id: FE_UBC_DIFF_GIT
   :tools: TOOL_UBC
   :si: yes

   Computes the traceability impact of a git commit / diff using the
   classified link model. Given a configurable link depth and
   direction, ``ubc diff git`` reports which needs are transitively
   affected — essential for change-impact analysis required by ISO
   26262 tool classification activities.

   .. code-block:: bash

      ubc diff git --depth 3 --direction both

   .. fault:: Impact depth truncates the graph
      :id: ER_UBC_DIFF_DEPTH_CUT

      The configured ``--depth`` is smaller than the deepest
      safety-relevant link chain, so the impact report misses
      affected needs. Downstream reviewers underestimate the change.

   .. fault:: Wrong direction omits incoming impact
      :id: ER_UBC_DIFF_DIR_WRONG

      ``--direction`` is set to ``outgoing`` only, so needs that
      depend *on* a modified need (incoming links) are not reported.

   .. fault:: Uncommitted local edits not covered
      :id: ER_UBC_DIFF_DIRTY

      The diff is computed against HEAD and ignores uncommitted
      changes in the working tree, which causes the report to
      under-represent the actual delta being reviewed.

.. feature:: Generate AI-agent skill for the project (``ubc agent-skill``)
   :id: FE_UBC_AGENT_SKILL
   :tools: TOOL_UBC
   :outputs: ART_UBC_NEEDS_JSON
   :si: no

   Emits a machine-readable description of the project ontology
   (types, fields, links, schemas) that LLM-based tooling can load
   to author and review needs deterministically. Because the skill
   is generated from the same ``ubproject.toml`` that drives the
   build, agent behaviour stays in sync with the qualified
   configuration.

   .. code-block:: bash

      ubc agent-skill

   .. fault:: Skill out of sync with qualified configuration
      :id: ER_UBC_AGENT_SKILL_STALE

      The generated skill is committed once and not refreshed when
      ``ubproject.toml`` changes. Agents create needs that conflict
      with the current schema and the build fails later than
      necessary.

.. feature:: Cross-check needs.json against an independent index (``ubc diff json``)
   :id: FE_UBC_JSON_CROSSCHECK
   :tools: TOOL_UBC
   :inputs: ART_SPHINX_RST, ART_UBC_NEEDS_JSON
   :si: yes

   Builds a second, independent ``needs.json`` from the same RST sources
   (see :need:`FE_UBC_BUILD_JSON`) and compares it field by field against
   the ``needs.json`` produced by the Sphinx-Needs build (ids, meta-data,
   links, permalinks).

   This diverse redundancy is the primary *tool error detection* means
   for the open-source Sphinx-Needs: a defect that silently alters the
   published index is caught because two independent implementations
   would have to fail in exactly the same way.

   .. code-block:: bash

      ubc diff json --against _build/html/needs.json

   .. fault:: Divergence not detected (false negative)
      :id: ER_UBC_CROSSCHECK_FALSE_NEG

      The cross-check reports no difference although the two indices
      differ (e.g. a field is excluded from the comparison), so a
      corrupted index passes unnoticed.
