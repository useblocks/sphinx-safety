.. _completeness:

Qualification Completeness
==========================

Features
--------
Overall Features: :need_count:`type=="feature"`

.. list-table::
   :align: center
   :header-rows: 1
   :width: 100%
   :widths: 60,20, 20

   - * Metric
     * Measurement
     * Target
   - * Safety Features without Errors
     * :need_count:`type == "feature" and si == "yes" and len(parent_needs_back) == 0` 
     * 0
   - * Features without Safety Impact value
     * :need_count:`type == "feature" and si == "" and len(parent_needs_back) == 0`
     * 0
   - * Features without use case
     * :need_count:`type == "feature" and len(features_back) == 0`
     * \-

.. dropdown:: Features without Errors

   .. needtable::
      :columns: id, title, tools
      :filter: type == "feature" and si == "yes" and len(parent_needs_back) == 0

.. dropdown:: Features without Safety Impact value

   .. needtable::
      :columns: id, title, tools
      :filter: type == "feature" and si == "" and len(parent_needs_back) == 0

.. dropdown:: Features without use case

   .. needtable::
      :columns: id, title, si, tools
      :filter: type == "feature" and len(features_back) == 0

Errors
------
Overall Errors: :need_count:`type=="fault"`

.. list-table::
   :align: center
   :header-rows: 1
   :width: 100%
   :widths: 60,20, 20

   - * Metric
     * Measurement
     * Target
   - * Errors without Mitigation
     * :need_count:`type == "fault" and len(avoids_back) == 0`
     * 0

.. dropdown:: Errors without Mitigation

   .. needtable::
      :columns: id, title, parent_needs
      :filter: type == "fault" and len(avoids_back) == 0

Restrictions
------------
Overall Restrictions: :need_count:`type=="restriction"`

.. list-table::
   :align: center
   :header-rows: 1
   :width: 100%
   :widths: 60,20, 20

   - * Metric
     * Measurement
     * Target
   - * Restrictions without Error
     * :need_count:`type == "restriction" and len(avoids) == 0`
     * 0

.. dropdown:: Restrictions without Error

   .. needtable::
      :columns: id, title, docname
      :filter: type == "restriction" and len(avoids) == 0