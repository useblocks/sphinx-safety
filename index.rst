:sd_hide_title:
:hide-toc:

Introduction
============

.. grid::
   :class-row: sd-w-100

   .. grid-item::
      :columns: 12 8 8 8
      :child-align: justify
      :class: sd-fs-3

      .. div:: sd-font-weight-bold

         Classification for Sphinx + X

      .. div:: sd-fs-5 sd-font-italic

         Qualify your Sphinx-based documentation toolchain for safety audits
         required by ISO 26262, IEC 61508, EN 50716, and more.

      .. grid:: 1 1 2 2
         :gutter: 2 2 3 3
         :margin: 2
         :padding: 0

         .. grid-item::
            :columns: auto

            .. button-ref:: usage/quickstart
               :ref-type: doc
               :outline:
               :color: primary
               :class: sd-rounded-pill sd-px-4 sd-fs-5

               Get Started

         .. grid-item::
            :columns: auto

            .. button-link:: https://useblocks.com/
               :outline:
               :color: primary
               :class: sd-rounded-pill sd-px-4 sd-fs-5

               Qualification Support

This documentation provides the necessary information to achieve
"qualification readiness" for any Sphinx-based project. It includes ``use cases``,
``features``, ``faults``, and ``restrictions`` represented as `Sphinx-Needs <https://sphinx-needs.com>`__
objects.

The classification serves as the foundation for any qualification
process. Additional qualification support is available through a
commercial :ref:`qualification` provided by `useblocks <https://useblocks.com>`__
and `Innotec <https://innotecsafety.com/>`__.

.. hint::

   **Project Status**

   This documentation is in its early stages. Tools and data are
   currently being collected and classified. Contributions are welcome!
   Visit our GitHub repository at https://github.com/useblocks/sphinx-safety/
   to join as a user or contributor.

   The current status and problemeatic entries can seen in :ref:`analysis`
   and :ref:`completeness`.

Supported Standards
-------------------

This documentation provides essential information for the
classification of Sphinx and Sphinx-Needs according to the following
standards:

* **Automotive**: `ISO 26262 <https://en.wikipedia.org/wiki/ISO_26262>`__
* **Automation, Industrial**: `IEC 61508 <https://en.wikipedia.org/wiki/IEC_61508>`__
* **Railway**: `EN 50716 <https://www.dinmedia.de/de/norm/din-en-50716/378381071>`__
* **Medical**: `IEC 62304 <https://en.wikipedia.org/wiki/IEC_62304>`__
* **Agriculture**: `ISO 25119 <https://en.wikipedia.org/wiki/ISO_25119>`__
* Additional standards can be added upon request or via a pull request.

Tool Scope
----------

The classification and qualification documentation cover the following
tools:

.. needtable::
   :filter: type == "tool"
   :style: table
   :columns: title, id, version, status
   :colwidths: 30,30,20,20

Please note that this classification does not cover **all features**
of a tool. It focuses exclusively on safety-relevant use cases. As a
result, a Tool Confidence Level (TCL) is assigned to individual use
cases rather than the tool as a whole.

Use Case Scope
--------------

.. needtable::
   :filter: type == "usecase"
   :style: table
   :columns: id, title, ti as "TI", tcl as "TCL"
   :colwidths: 20,40,20,20

Support
-------

.. grid:: 2

   .. grid-item-card:: useblocks
      :link: https://useblocks.com
      :class-card: ubcard

      Tool Support
      ^^^
      useblocks GmbH is a German solution provider specializing in documentation tools for
      software development teams, with a strong focus on the "docs-as-code" methodology.
      Their expertise lies in integrating documentation seamlessly into development workflows,
      enabling teams to treat documentation as an integral part of their codebase.
      This approach ensures consistency, version control, and collaboration across teams.

      +++
      .. image:: https://useblocks.com/_static/useblocks_white.svg
        :align: center
        :height: 50px

   .. grid-item-card:: innotec
      :link: https://innotecsafety.com/
      :class-card: ubcard

      Consultancy Support
      ^^^
      innotec GmbH, a member of the TÜV Austria Group, is a German consultancy specializing in functional safety across various sectors, including automotive, machinery, and embedded systems. Their expertise encompasses comprehensive support for tool qualification and validation, ensuring compliance with standards such as ISO 26262, IEC 61508, and EN 50128.

      +++
      .. image:: https://innotecsafety.com/wp-content/uploads/2024/10/innotec-logo-tuv-austria-group-e1728416243598-1.png
         :align: center
         :height: 50px

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Basics

   usage/quickstart
   usage/index
   usage/contribute
   usage/approach_iso26262
   usage/qualification
   usage/license

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Classification Data

   use_cases/index
   tools/index
   analysis/index
