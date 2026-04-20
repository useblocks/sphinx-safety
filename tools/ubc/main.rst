ubc
===

.. tool:: ubc
   :id: TOOL_UBC
   :status: in_progress

   Command-line tool for checking and formating certain rules in sphinx
   and rst-based files.

   Little brother of :need:`TOOL_UBCODE`.

   **Commercial tool**

   :Documentation: https://ubcode.useblocks.com/ubc/introduction.html


Analysis
--------

.. needflow::
   :filter: "tools/ubc/" in docname

.. needtable::
   :filter: "tools/ubc/" in docname
   :columns: id, title, type

.. needpie:: Sphinx-Needs objects
   :legend: 
   :labels: Features, Faults, Restrictions, Checks, Steps
   :explode: 0,0,0,0.1,0.1

   type == "feature" and "tools/ubc/" in docname
   type == "fault" and "tools/ubc/" in docname
   type == "restriction" and "tools/ubc/" in docname
   type == "check" and "tools/ubc/" in docname
   type == "step" and "tools/ubc/" in docname

.. dropdown:: ✅ Compliance statistics

   Features without faults:
   :need_count:`"tools/ubc/" in docname and type == "feature" and len(parent_needs_back) == 0` /
   :need_count:`"tools/ubc/" in docname and type == "feature"`

   Faults without a mitigation:
   :need_count:`"tools/ubc/" in docname and type == "fault" and (len(avoids_back) == 0 and len(checks_back) == 0)` /
   :need_count:`"tools/ubc/" in docname and type == "fault"`

   Restrictions without fault:
   :need_count:`"tools/ubc/" in docname and type == "restriction" and len(avoids) == 0` /
   :need_count:`"tools/ubc/" in docname and type == "restriction"`

   Checks without fault:
   :need_count:`"tools/ubc/" in docname and type == "check" and len(checks) == 0` /
   :need_count:`"tools/ubc/" in docname and type == "check"`

