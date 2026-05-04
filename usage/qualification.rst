.. _qualification:

:octicon:`shield-check` Qualification Kit
=========================================

To successfully pass an audit and achieve final toolchain
qualification, additional information and tools are required. These
are not included in this classification document.

The required information is provided through a Qualification Kit,
which includes:

* Additional test cases for Sphinx and Sphinx-Needs.
* Documentation of ``checks`` and ``process steps``, including links to
  the ``faults`` described in this document.
* A license for ``ubCode`` and its command-line tool ``ubc``, enabling
  specific checks in VS Code and CI environments.
* A Qualification Report generator to document the final qualification
  results (part of ``ubc``).
* Templates for creating consistent Qualification documentation for
  other tools, both external and internal.

The Qualification documentation is built on the same technical
foundation as this classification documentation, primarily using
Sphinx and Sphinx-Needs. This allows the classification section to be
seamlessly integrated into the Qualification documentation, creating a
comprehensive report.

**To obtain a Sphinx Qualification Kit**, please contact `Innotec GmbH <https://innotecsafety.com/>`__
or `useblocks GmbH <https://useblocks.com>`__.

Qualification Content
---------------------

The diagram below illustrates the distinction between the
Classification and Qualification documentation and toolchain.

The **Classification** setup allows you to document all
project-specific use cases, while the **Qualification** process
extends this information with common checks and restrictions.

This means that the project-specific configuration can be completed in
advance using this Open-Source documentation. The Qualification
process, supported by its tools, follows afterward to automatically
test your project and document the required results.

The Qualification process typically covers over 90% of the documented
classification. Any remaining project-specific extensions can be
implemented independently or with the support of `Innotec GmbH <https://innotecsafety.com/>`__
or `useblocks GmbH <https://useblocks.com>`__.

The ``ubc`` tool enables the required checks to be executed via the
command line, allowing you to run them locally or integrate them into
your CI pipeline for automated code reviews.

The ``ubCode`` tool performs the same checks directly within the VS
Code editor, providing immediate feedback to developers.

This toolchain also allows you to perform similar classification and
qualification processes for other tools. Additionally, it enables the
creation of a unified toolchain qualification project, where the
Sphinx-related part serves as a foundational example.

.. image:: /_static/sphinx-safety_classi_qualification.drawio.png
   :align: center
   :scale: 99%

Showcase
--------

.. grid:: 2

   .. grid-item::

      .. figure:: /_static/qualification_kit_website_1.png
         :width: 99%
         :align: center

         Imported test cases for Sphinx

   .. grid-item::

      .. figure:: /_static/qualification_kit_website_2.png
         :width: 99%
         :align: center

         Defined checks for Sphinx

Qualification Method
--------------------

The qualification process primarily relies on the tools ``ubCode`` and
its command-line counterpart ``ubc`` to recreate specific Sphinx
artifacts and verify them for discrepancies.

These tools are developed by separate teams using entirely different
technical foundations. If both tools produce identical outputs, the
results can be considered **safe**.

Additionally, the Qualification Kit verifies tool-specific test cases
for safety-critical features. If these test cases exist—either as part
of the Open-Source project or the Qualification Kit—and their
execution is successful (*green*), the feature can also be deemed **safe**.

For features that are deemed unsafe, the tool's execution must be
reviewed during or after its run. Special scripts are available for
this purpose, which can be integrated into CI pipelines, pre-commit
hooks, or used with ``ubCode`` to ensure the avoidance of unsafe
features.

.. figure:: /_static/qualification_method.drawio.png
   :align: center

   2 independent tool chains as Qualification method
