.. _`approach_iso26262`:

:octicon:`verified` Tool Qualification ISO 26262
================================================

Introduction
------------

This document outlines the approach used to qualify software tools for
use in safety-relevant development activities, in compliance with **ISO
26262:2018**. The qualification ensures that the tools meet the
necessary safety requirements and can be reliably integrated into the
ISO 26262-compliant development lifecycle.

Qualification Approach Overview
-------------------------------

The qualification process is based on **ISO 26262 Part 8, Clause 11**,
and consists of the following key steps:

- **Tool Classification**: Corresponds to the evaluation phase of ISO
  26262 and is included in the open-source repository.
- **Tool Qualification**: Links identified errors to mitigation
  strategies, tests etc., provides the tests results, final validation
  evidences and the safety manual as part of the qualification package.

Planning Tool Usage (Clause 11.4.4)
-----------------------------------

Identification of the different tools in scope are given in :ref:`tools`
and their use in the safety lifecycle (e.g., requirements definition,
traceability, documentation generation) is defined via :ref:`use_cases`
.In addition also the information about allowed configuration and the
environment are available in the qualification pack.

The maximum ASIL of the elements where the toolchain is used, is
assumed to be ``ASIL D``.

Tool Evaluation by Analysis (Clause 11.4.5)
-------------------------------------------

Use Case Analysis
^^^^^^^^^^^^^^^^^

Each use case is analyzed to identify the specific tool features
required. This enables full traceability starting from use cases,
downd to the individual features and their verification tests.

HAZOP Analysis
^^^^^^^^^^^^^^

A **HAZOP (Hazard and Operability)** analysis is conducted to identify
potential failure modes. This technique facilitates structured
brainstorming by applying a set of predefined “Guide Words” to analyze
deviations in the feature behavior. During this analysis also the Tool
Impact (``TI``) for the use case and therefore for the feature is
determined. There is the possibility also, that a use case is
classified as ``TI2``, meaning it can have an impact on safety, but
specific features used in that use case might still be classified as ``TI1``,
if their contribution to that use case has no safety impact. Each
guide word is methodically applied to all features and tools to
analyze possible deviations. The results is a collection of errors
linked to each feature.

Error Mitigation Strategies
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Identified errors are addressed using one or more of the following
mitigation techniques:

1. **Usage Restrictions** define ways to avoid specific errors, such
as by not using certain functions or configurations. During tool
execution, compliance with restrictions should be checked
automatically or through a manual process. These will also be as much
as possible automated through **checks** in ``ubc``

2. **Test cases** to validate the correct behaviour of the tool,
possible built-in error detection mechanisms or validating that a
specific error is shown to not be possible

3. **Redundancy in tools** via the use of other tools (e.g. ``ubc``)
to allow for detection of tool errors

4. **Process steps** that are required to be implemented by the tool
user in order to detect the tool error. This is kept to a minimum and
in line with the already expected process steps in an ISO 26262
compliant lifecycle (e.g. verification of requirements by
review/inspection etc.)

Tool Confidence Level (TCL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

As the different mitigations also differ in their ability or
confidence in detection toool errors, the Tool Error Detection (``TD``),
is now annoted back to the error. At the same time also the resulting
Tool Confidence Level (``TCL``) is determined according to Table 3 of **ISO
26262-8:2018** and marks the completion of the evaluation phase.

Tool Qualification (Clause 11.4.6)
----------------------------------

Based on the resulting Tool Confidence Level (``TCL``) an appropriate
comibnation of the qualification methods from Tables 4 and 5 of **ISO
26262-8:2018** has to be made. As per above, the assumed ``ASIL`` is ``ASIL D``
when selecting the methods.

+----+--------------------------------------------------+-------------------+
|    | Methods                                          | ASIL              |
+----+                                                  +----+----+----+----+
|    |                                                  | A  | B  | C  | D  |
+====+==================================================+====+====+====+====+
| 1a | Increased confidence from use                    | ++ | ++ | \+ | \+ |
+----+--------------------------------------------------+----+----+----+----+
| 1b | Evaluation of the tool development process       | ++ | ++ | \+ | \+ |
+----+--------------------------------------------------+----+----+----+----+
| 1c | Validation of the software tool                  | \+ | \+ | ++ | ++ |
+----+--------------------------------------------------+----+----+----+----+
| 1d | Development in accordance with a safety standard | \+ | \+ | ++ | ++ |
+----+--------------------------------------------------+----+----+----+----+

Increased confidence from use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Increased confidence from use as a qualification method is not
applied, as the qualification shall be adaptable to new versions
without relying on specific prior experience. Therefore this method is
not used in this project.

Development in accordance with a safety standard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Also the approach to develop the tool according to for example ISO
26262-6 or IEC 61508-3 is not feasibile, as the tools are already
pre-existing as open source tools. Therefore this approach can not be
applied in the project.

Evaluation of the tool development process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The evaluation of the tool development process method is applied, as **ISO
26262-8: 2018**, Clause 11.4.8.2 spcifically also states in the note,
that open source community standards of contribution etc. are also
valid evidences to show application of this method. Therefore in the
qualification pack also analysis and justifications showing fulfilment
of **ISO 26262-8:2018**, Clause 11.4.8 are provided. This method is
recommended for ``TCL3`` and ``ASIL D`` but not highly recommended,
therefore this method is used in conjuntion with the validation.

Validation of the software tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method then choosen for ``ASIL D`` in combination with the
evaluation of the tool development process above is the validation of
the software tools against their requirements. This is also the reason
to break down the use case further to features, as the features
themselves will be used as the requirements/specification for the
validation through test cases. Starting point for the test cases are
of course the already existing test cases in the open source project.
These will be linked to the features and if insufficient coverage of
the feature is detected, additional test cases will be written. The
test will be executed for the defined configurations and different
environments to show the correct execution of the tools in the defined
environments.

To further check coverage of the features through testing, also the
Code Coverage (Statment Coverage) achieved during the above testing
will be captured and analyzed. Any missing percentage to 90% coverage
will either be closed by additional test cases or the remaining gaps
be analyzed and justified as part of the qualification package.

Work Products
^^^^^^^^^^^^^

The **Software Tool Criteria Evaluation Report** is the documentation
in this repository, minus the error detection or mitigation (and
therefore without ``TD`` and resulting ``TCL``) as these are part of
the qualification pack.

Consequently the **Software Tool Qualification Report** is the
qualification pack including the verification results and the safety
manual detailing the usage restrictions or process steps required.
