
Sphinx-Needs
============

.. tool:: Sphinx-Needs
   :id: TOOL_SN
   :version: 8.0.0
   :status: in_progress

   Sphinx makes it easy to create intelligent and beautiful
   documentation.

   :Documentation: https://www.sphinx-needs.com
   :Code: https://github.com/useblocks/sphinx-needs

Analysis
--------


.. needflow::
   :filter: "tools/sphinx-needs/" in docname

.. needtable::
   :filter: "tools/sphinx-needs/" in docname
   :columns: id, title, type

.. needpie:: Sphinx-Needs objects
   :legend:
   :labels: Features, Faults, Restrictions, Checks, Steps
   :explode: 0,0,0,0.1,0.1

   type == "feature" and "tools/sphinx-needs/" in docname
   type == "fault" and "tools/sphinx-needs/" in docname
   type == "restriction" and "tools/sphinx-needs/" in docname
   type == "check" and "tools/sphinx-needs/" in docname
   type == "step" and "tools/sphinx-needs/" in docname

.. dropdown:: ✅ Compliance statistics

   Features without faults: :need_count:`"tools/sphinx-needs/" in docname and type == "feature" and len(parent_needs_back) == 0`
   / :need_count:`"tools/sphinx-needs/" in docname and type == "feature"`

   Faults without a mitigation: :need_count:`"tools/sphinx-needs/" in docname and type == "fault" and (len(avoids_back) == 0 and len(checks_back) == 0)`
   / :need_count:`"tools/sphinx-needs/" in docname and type == "fault"`

   Restrictions without fault: :need_count:`"tools/sphinx-needs/" in docname and type == "restriction" and len(avoids) == 0`
   / :need_count:`"tools/sphinx-needs/" in docname and type == "restriction"`

   Checks without fault: :need_count:`"tools/sphinx-needs/" in docname and type == "check" and len(checks) == 0`
   / :need_count:`"tools/sphinx-needs/" in docname and type == "check"`
