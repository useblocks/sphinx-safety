.. _quickstart:

:octicon:`rocket` Quickstart
============================

Installation
------------

This explains how to get a local copy of this documentation, so that ``use cases``
and co. can be extended.

Prerequirement: Python and uv must be installed

1. Checkout the repository: ``git clone https://github.com/useblocks/sphinx-safety``
#. ``cd sphinx-safety``
#. ``uv init``, this will create a virtual Python environment and
   installs all needed dependencies.
#. Build the docs via ``uv run sphinx-build -a -E -b html . _build/html``.
#. Open ``_build/html/index.html`` with your browser of choice.

Usage
-----

The documentation can be used as it is. And for sure also extended.

Extending the documentation is the most important use case, as your
project may use additional features or even tools.

The project configuration contains also the complete qualification model,
so feel free to extend your documentation with own ``checks`` and ``test cases`` to prepare a qualification.
But beware that a ready-to-use qualification kit exists for Sphinx and Sphinx-Needs, provided 
by `useblocks <https://useblocks.com>`__ and `innotec <https://innotecsafety.com>`__.

Tool support
------------

The restrictions documented here got integrated in some tools to
support autoamtic and faster user feedback.

ubCode
~~~~~~

``ubCode`` is an extensions for the editor **VS Code**. It extracts
Sphinx-Needs objects in realtime and performs certains checks, like
used directives. ``ubCode`` helps the developer to follow certain
rules by giving direct feedback already during writing the
documentation.

The restrictions defined in this documentation are integrated into ``ubCode``.
Also checks needed for a final qualification are part of ``ubCode``.

:vendor: `useblocks GmbH <https://useblocks.com>`__
:website: https://ubcode.useblocks.com

Terms
-----

In the context of ISO 26262 and other safety standards, classification
and qualification serve distinct purposes:

- **Classification**: Classification involves categorizing software or
  hardware components based on their criticality and impact on safety.
  For example, in ISO 26262, components are classified into Automotive
  Safety Integrity Levels (ASILs) such as ASIL A, B, C, or D, or deemed
  QM (Quality Management) if they do not impact safety. This process
  helps determine the level of rigor required for development and
  testing.
- **Qualification**: Qualification ensures that a tool, software, or
  component meets the necessary safety requirements for its intended
  use. For example, tool qualification ensures that a development tool
  does not introduce errors into safety-critical systems. This process
  often involves validation, verification, and documentation to
  demonstrate compliance with safety standards.

In summary, classification determines the safety relevance of a
component, while qualification ensures that the component or tool is
suitable for use in a safety-critical environment.
