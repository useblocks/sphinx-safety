.. _contribute:

:octicon:`people` Contribute
============================

Basic Principles
----------------

1. Validate only relevant use cases.
2. If a tool error is negligible compared to human error, validation is
   not required.
3. Use comparisons between diverse tools as part of the argumentation.
4. Reuse community tests wherever reasonable.
5. There is no such thing as "proven in use" for newer tool versions.

Classification & Qualification Model
------------------------------------

The following flowchart provides an overview of all available
Sphinx-Needs types and their relationships.

.. image:: /_static/sphinx-safety_classi_qualification.drawio.png
   :align: center
   :scale: 99%

This classification documentation focuses on the blue elements:

* Use cases
* Features
* Errors
* Restrictions
* Tools

The remaining elements are part of the :ref:`qualification`.

An example of this data model with real elements is shown below:

.. image:: /_static/contribute_model_example.png
   :align: center

Each Sphinx-Needs object has several attributes, as illustrated in the
following class diagram.

Calculated attributes are marked with a red square, while manual ones
are marked with a green circle.

.. uml::

   class "Use Case" as uc {
      __Defaults__
      +title: string
      +id: string
      +content: string
      +status: string
      __Specific__
      +TI: integer
      -TCL: integer
      ..Links..
      +tools <<tool>>
      +features <<feature>>
      +inputs <<artifact>>
      +outputs <<artifact>>
   }

   class "Tool" as to {
      __Defaults__
      +title: string
      +id: string
      +content: string
      +status: string
      __Specific__
      +version: string
   }

   class "Feature" as fe {
      __Defaults__
      +title: string
      +id: string
      +content: string
      +status: string
      __Specific__
      -TD: integer
      ..Links..
      +tools <<tool>>
      -child needs <<error>>
      +inputs <<artifact>>
      +outputs <<artifact>>
   }

   class "Fault" as er {
      __Defaults__
      +title: string
      +id: string
      +content: string
      +status: string
      __Specific__
      +TD: integer
   }

   class "Restriction" as re {
      __Defaults__
      +title: string
      +id: string
      +content: string
      +status: string
      __Specific__
      ..Links..
      +avoids <<error>>
   }

   uc -> fe
   fe --> er
   re --> er
   uc --> to
   fe --> to

Extend Documentation
--------------------

For this documentation, the workflow described in :ref:`usage` is the
preferred approach.

After making changes and testing them locally with a Sphinx build,
create a Pull Request (PR) in the repository.

The PR will be automatically checked, and the documentation will be
built in a test run. Afterward, a manual review will be conducted.

Once the review is approved and all CI tests pass, the PR will be
merged, and the updated documentation will be deployed.

TI, TD, and TCL Values
----------------------

The **Tool Impact (TI)** value is assigned at the ``use case`` level
and indicates whether the ``use case`` has a safety-relevant impact:

- **TI = 2**: Indicates a safety-relevant impact.
- **TI = 1**: Indicates no safety relevance.

.. hint::

   The **TI** level is very project-specific. For instance in one project
   requirements are used to describe an Airbag system for a car, in
   another project there are used for minor parts of the multimedia
   system.

   This documentation always have the "worst case" in mind, which means
   that the target documentation is the single source of truth for a high
   safety critical project.

The **Tool Error Detection (TD)** value must be defined for each ``error``
and represents the ability to detect the error:

- **TD = 1**: The error is detected, and execution stops without
  producing a final result.
- **TD = 3**: The error is not detected.
- **TD = 2**: This value is not used in this document.

The final **Tool Confidence Level (TCL)** is calculated as follows:

- If **TI = 1**, then **TCL = 1**, and no further actions are required
  for tool qualification.
- If **TI = 2**, the highest **TD** value among all linked,
  safety-relevant features and their errors determines the **TCL**.
- A **tbd** (to  be done) can be set, if the final TCL can onyl be set
  after missing features and co. are added.

A ``use case`` with a **TCL** of **2** or **3** requires special
handling during the tool qualification process.

.. list-table::
   :stub-columns: 1
   :header-rows: 1

   * - Type
     - Allowed Values
     - Scope
     - Manually Set?
   * - TI
     - 1, 2
     - Use Case
     - Yes
   * - TD
     - 1, 3
     - Error, Feature
     - Yes
   * - TCL
     - 1, 2, 3, tbd
     - Use Case
     - No

Safety Impact Value
-------------------

The **Tool Impact (TI)** value indicates whether a tool, as a whole,
has a safety-relevant impact. However, it does not differentiate
between individual features. Instead, the safety impact is determined
by how the tool is used within a specific project.

To address this limitation, we introduced the **Safety Impact (SI)**
value. This value specifies whether a feature has a safety impact for
most standard use cases or if it can always be used safely without
further qualification.

For example, the Sphinx feature :need:`FE_SPHINX_INLINE_STRONG` allows
text to be displayed in bold. Whether text is bold or not does not
have a safety impact, so this feature can always be used safely **without
requiring further qualification**.

In contrast, features like :need:`FE_SPHINX_OUTPUT_HTML` can have a
significant impact if their output does not include all necessary
data.

Ultimately, the ``use case`` determines whether it has a safety
impact. This decision can vary by project, as only the project team
knows how critical the output artifacts are to the overall safety
concept.

**Example**

.. code-block:: rst

   .. feature:: Read Traceability objects in Sphinx-Needs
      :id: FE_SN_READ
      :tools: TOOL_SN
      :si: yes

