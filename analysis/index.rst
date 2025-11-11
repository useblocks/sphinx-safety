.. _analysis:

:octicon:`graph` Analysis
=========================

.. toctree::
   :hidden:

   qualification


All elements
------------

Table
+++++
.. needtable::
   :columns: id, title, type

Flowchart
+++++++++
.. needflow::

Piechart
++++++++

By Tool
~~~~~~~
.. needpie::
   :labels: Sphinx, Sphinx-Needs, Sphinx-Test-Reports, ubCode, ubc, ubTrace

   "tools/sphinx/" in docname
   "tools/sphinx-needs/" in docname
   "tools/sphinx-test-reports" in docname
   "tools/ubcode" in docname
   "tools/ubc/" in docname
   "tools/ubtrace" in docname

By Type
~~~~~~~
.. needpie::
   :labels: Use Case, Feature, Fault, Restriction, Artifact

   type == "usecase"
   type == "feature"
   type == "fault"
   type == "restriction"
   type == "artifact"

