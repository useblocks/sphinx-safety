Features
========

.. dropdown:: 🔍 Features

   .. needtable::
      :filter: "tools/sphinx/" in docname and type == "feature"
      :columns: id, title, si as "SI", parent_needs_back as "Errors"

   .. needpie:: Sphinx features
      :legend:
      :labels: Safety impact, No impact, Undefined impact
      
      type == "feature" and "tools/sphinx/" in docname and si == "yes"
      type == "feature" and "tools/sphinx/" in docname and si == "no"
      type == "feature" and "tools/sphinx/" in docname and si == ""


.. feature:: Read-in documents with Sphinx
   :id: FE_SPHINX_READ
   :tools: TOOL_SPHINX
   :si: yes

   Readin all needed rst/md files for the Sphinx project.

   .. fault:: Needed folders/files are ignored
      :id: ER_FILES_IGNORED

      Error is logged by Sphinx and with build-option ``-W`` this warning
      gets thrown as error and stops the build.

   .. fault:: Needed files/folders have not supported encoding
      :id: ER_SPH_WRONG_ENCODING

   .. fault:: Access to files/folders not given
      :id: ER_SPH_WRONG_ACCESS

Inline Text Formatting
++++++++++++++++++++++

.. feature:: Italicized (Emphasis) Text
   :id: FE_SPHINX_INLINE_EMPHASIS
   :tools: TOOL_SPHINX
   :si: no

   Use emphasis to italicize text in your documentation.

   .. code-block:: rst

      This is *italicized* text.

.. feature:: Bold (Strong) Text
   :id: FE_SPHINX_INLINE_STRONG
   :tools: TOOL_SPHINX
   :si: no

   Use strong emphasis to make text bold.

   .. code-block:: rst

      This is **bold** text.

.. feature:: Inline Literal (Code) Text
   :id: FE_SPHINX_INLINE_LITERAL
   :tools: TOOL_SPHINX
   :si: no

   Use inline literals to display code or commands inline.

   .. code-block:: rst

      This is ``inline code``.

.. feature:: Named Hyperlink Reference
   :id: FE_SPHINX_INLINE_NAMED_HYPERLINK
   :tools: TOOL_SPHINX
   :si: yes

   Create a named hyperlink reference to link to external or internal
   resources.

   .. code-block:: rst

      `Sphinx Documentation <https://www.sphinx-doc.org/en/master/>`__

.. feature:: Inline Internal Target
   :id: FE_SPHINX_INLINE_INTERNAL_TARGET
   :tools: TOOL_SPHINX
   :si: no

   Use internal targets to create cross-references within your
   documentation.

   .. code-block:: rst

      See :ref:`example-section` for more details.

.. feature:: Escaped Markup Characters
   :id: FE_SPHINX_INLINE_ESCAPE
   :tools: TOOL_SPHINX
   :si: no

   Escape special characters to display them as plain text.

   .. code-block:: rst

      Use \\* to display an asterisk (*).

.. feature:: Subscript Role
   :id: FE_SPHINX_ROLE_SUBSCRIPT
   :tools: TOOL_SPHINX
   :si: no

   Use the subscript role to display text as a subscript.

   .. code-block:: rst

      H\ :sub:`2`\ O

.. feature:: Superscript Role
   :id: FE_SPHINX_ROLE_SUPERSCRIPT
   :tools: TOOL_SPHINX
   :si: no

   Use the superscript role to display text as a superscript.

   .. code-block:: rst

      E = mc\ :sup:`2`

.. feature:: Strong Role
   :id: FE_SPHINX_ROLE_STRONG
   :tools: TOOL_SPHINX
   :si: no

   Use the strong role to emphasize text strongly.

   .. code-block:: rst

      :strong:`Important!`

.. feature:: Emphasis Role
   :id: FE_SPHINX_ROLE_EMPHASIS
   :tools: TOOL_SPHINX
   :si: no

   Use the emphasis role to italicize text.

   .. code-block:: rst

      :emphasis:`This is emphasized text.`

.. feature:: Literal Role
   :id: FE_SPHINX_ROLE_LITERAL
   :tools: TOOL_SPHINX
   :si: no

   Use the literal role to display inline code or commands.

   .. code-block:: rst

      :literal:`print("Hello, World!")`

.. feature:: Code Role
   :id: FE_SPHINX_ROLE_CODE
   :tools: TOOL_SPHINX
   :si: no

   Use the code role to highlight inline code snippets.

   .. code-block:: rst

      :code:`def example(): pass`

.. feature:: Inline Math Role
   :id: FE_SPHINX_ROLE_MATH
   :tools: TOOL_SPHINX
   :si: no

   Use the math role to display inline mathematical expressions.

   .. code-block:: rst

      :math:`E = mc^2`

Structural Elements
+++++++++++++++++++

.. feature:: Section Titles with Underlines
   :id: FE_SPHINX_STRUCTURE_SECTION_TITLES
   :tools: TOOL_SPHINX
   :si: no

   Use underlines to define section titles in your documentation.

   .. code-block:: rst

      Section Title
      =============

.. feature:: Document Title and Subtitle
   :id: FE_SPHINX_STRUCTURE_DOC_TITLE
   :tools: TOOL_SPHINX
   :si: no

   Define a document title and optional subtitle using underlines.

   .. code-block:: rst

      Document Title
      ==============

      Subtitle
      --------

.. feature:: Transitions (Horizontal Lines)
   :id: FE_SPHINX_STRUCTURE_TRANSITIONS
   :tools: TOOL_SPHINX
   :si: no

   Use transitions to separate sections visually with horizontal lines.

   .. code-block:: rst

      --------

.. feature:: Table of Contents Tree Directive (toctree)
   :id: FE_SPHINX_DIRECTIVE_TOCTREE
   :tools: TOOL_SPHINX
   :si: yes

   Use the toctree directive to create a table of contents for your
   documentation.

   .. code-block:: rst

      .. toctree::
         :maxdepth: 2

         introduction
         usage
         contribute

.. feature:: Rubric Directive
   :id: FE_SPHINX_DIRECTIVE_RUBRIC
   :tools: TOOL_SPHINX
   :si: no

   Use the rubric directive to add a styled heading to your
   documentation.

   .. code-block:: rst

      .. rubric:: Important Notes

Lists and Quotes
++++++++++++++++

.. feature:: Bulleted Lists
   :id: FE_SPHINX_LISTS_BULLETED
   :tools: TOOL_SPHINX
   :si: no

   Use bulleted lists to organize items without a specific order.

   .. code-block:: rst

      - Item 1
      - Item 2
      - Item 3

.. feature:: Numbered (Enumerated) Lists
   :id: FE_SPHINX_LISTS_ENUMERATED
   :tools: TOOL_SPHINX
   :si: no

   Use numbered lists to organize items in a specific order.

   .. code-block:: rst

      1. First item
      2. Second item
      3. Third item

.. feature:: Auto-Numbered Lists
   :id: FE_SPHINX_LISTS_AUTO_NUMBERED
   :tools: TOOL_SPHINX
   :si: no

   Use auto-numbered lists to let Sphinx automatically number the items.

   .. code-block:: rst

      #. First item
      #. Second item
      #. Third item

.. feature:: Nested Lists
   :id: FE_SPHINX_LISTS_NESTED
   :tools: TOOL_SPHINX
   :si: no

   Use nested lists to create hierarchical structures.

   .. code-block:: rst

      - Parent item
        - Child item
          - Sub-child item

.. feature:: Definition Lists
   :id: FE_SPHINX_LISTS_DEFINITION
   :tools: TOOL_SPHINX
   :si: no

   Use definition lists to define terms and their descriptions.

   .. code-block:: rst

      Term 1
         Definition of term 1.

      Term 2
         Definition of term 2.

.. feature:: Option Lists
   :id: FE_SPHINX_LISTS_OPTION
   :tools: TOOL_SPHINX
   :si: no

   Use option lists to document command-line options or similar items.

   .. code-block:: rst

      -a  Enable all features.
      -h  Display help information.

.. feature:: Block Quotes
   :id: FE_SPHINX_CONTENT_BLOCKQUOTES
   :tools: TOOL_SPHINX
   :si: no

   Use block quotes to highlight quoted text or important notes.

   .. code-block:: rst

      > This is a block quote.

.. feature:: Line Blocks
   :id: FE_SPHINX_CONTENT_LINE_BLOCKS
   :tools: TOOL_SPHINX
   :si: no

   Use line blocks to preserve line breaks in text.

   .. code-block:: rst

      | Line 1
      | Line 2
      | Line 3

Directives for Content
++++++++++++++++++++++

.. feature:: Image Directive
   :id: FE_SPHINX_DIRECTIVE_IMAGE
   :tools: TOOL_SPHINX
   :si: yes

   Use the image directive to include images in your documentation.

   .. code-block:: rst

      .. image:: example.png
         :alt: Example image
         :width: 300px

.. feature:: Figure Directive
   :id: FE_SPHINX_DIRECTIVE_FIGURE
   :tools: TOOL_SPHINX
   :si: yes

   Use the figure directive to include images with captions.

   .. code-block:: rst

      .. figure:: example.png
         :alt: Example image

         This is a caption for the figure.

.. feature:: Table Directive with Title
   :id: FE_SPHINX_DIRECTIVE_TABLE
   :tools: TOOL_SPHINX
   :si: yes

   Use the table directive to create tables with titles.

   .. code-block:: rst

      .. table:: Example Table

         ========  ========
         Header 1  Header 2
         ========  ========
         Row 1     Data 1
         Row 2     Data 2
         ========  ========

.. feature:: Simple Tables
   :id: FE_SPHINX_TABLES_SIMPLE
   :tools: TOOL_SPHINX
   :si: yes

   Use simple tables for basic tabular data.

   .. code-block:: rst

      ========  ========
      Header 1  Header 2
      ========  ========
      Row 1     Data 1
      Row 2     Data 2
      ========  ========

.. feature:: Grid Tables
   :id: FE_SPHINX_TABLES_GRID
   :tools: TOOL_SPHINX
   :si: yes

   Use grid tables for more complex table layouts.

   .. code-block:: rst

      +----------+----------+
      | Header 1 | Header 2 |
      +==========+==========+
      | Row 1    | Data 1   |
      +----------+----------+
      | Row 2    | Data 2   |
      +----------+----------+

.. feature:: CSV Table Directive
   :id: FE_SPHINX_DIRECTIVE_CSV_TABLE
   :tools: TOOL_SPHINX
   :si: yes

   Use the CSV table directive to create tables from CSV files.

   .. code-block:: rst

      .. csv-table:: Example CSV Table
         :file: example.csv
         :header-rows: 1

.. feature:: List Table Directive
   :id: FE_SPHINX_DIRECTIVE_LIST_TABLE
   :tools: TOOL_SPHINX
   :si: yes

   Use the list table directive to create tables from lists.

   .. code-block:: rst

      .. list-table:: Example List Table
         :header-rows: 1

         * - Header 1
           - Header 2
         * - Row 1
           - Data 1
         * - Row 2
           - Data 2

.. feature:: Code Block Directive
   :id: FE_SPHINX_DIRECTIVE_CODE_BLOCK
   :tools: TOOL_SPHINX
   :si: no

   Use the code block directive to include syntax-highlighted code
   snippets.

   .. code-block:: python

      def example():
          print("Hello, World!")

.. feature:: Literal Include Directive
   :id: FE_SPHINX_DIRECTIVE_LITERALINCLUDE
   :tools: TOOL_SPHINX
   :si: yes

   Use the literal include directive to include external code files.

   .. code-block:: rst

      .. literalinclude:: example.py
         :language: python

.. feature:: Math Directive
   :id: FE_SPHINX_DIRECTIVE_MATH
   :tools: TOOL_SPHINX
   :si: no

   Use the math directive to include mathematical equations.

   .. code-block:: rst

      .. math::

         E = mc^2

.. feature:: Contents Directive (Local ToC)
   :id: FE_SPHINX_DIRECTIVE_CONTENTS
   :tools: TOOL_SPHINX
   :si: no

   Use the contents directive to create a local table of contents.

   .. code-block:: rst

      .. contents::
         :local:

.. feature:: Include Directive
   :id: FE_SPHINX_DIRECTIVE_INCLUDE
   :tools: TOOL_SPHINX
   :si: yes

   Use the include directive to include content from other files.

   .. code-block:: rst

      .. include:: other_file.rst

.. feature:: Raw Content Directive
   :id: FE_SPHINX_DIRECTIVE_RAW
   :tools: TOOL_SPHINX
   :si: no

Directives for Admonitions
++++++++++++++++++++++++++

.. feature:: Note Admonition
   :id: FE_SPHINX_ADMONITION_NOTE
   :tools: TOOL_SPHINX
   :si: no

   Use the note admonition to highlight additional information.

   .. code-block:: rst

      .. note::

         This is a note.

.. feature:: Warning Admonition
   :id: FE_SPHINX_ADMONITION_WARNING
   :tools: TOOL_SPHINX
   :si: no

   Use the warning admonition to emphasize potential issues or risks.

   .. code-block:: rst

      .. warning::

         This is a warning.

.. feature:: Hint Admonition
   :id: FE_SPHINX_ADMONITION_HINT
   :tools: TOOL_SPHINX
   :si: no

   Use the hint admonition to provide helpful tips or suggestions.

   .. code-block:: rst

      .. hint::

         This is a hint.

.. feature:: Tip Admonition
   :id: FE_SPHINX_ADMONITION_TIP
   :tools: TOOL_SPHINX
   :si: no

   Use the tip admonition to share useful advice.

   .. code-block:: rst

      .. tip::

         This is a tip.

.. feature:: Important Admonition
   :id: FE_SPHINX_ADMONITION_IMPORTANT
   :tools: TOOL_SPHINX
   :si: no

   Use the important admonition to highlight critical information.

   .. code-block:: rst

      .. important::

         This is important.

.. feature:: Attention Admonition
   :id: FE_SPHINX_ADMONITION_ATTENTION
   :tools: TOOL_SPHINX
   :si: no

   Use the attention admonition to draw focus to specific content.

   .. code-block:: rst

      .. attention::

         Pay attention to this.

.. feature:: Caution Admonition
   :id: FE_SPHINX_ADMONITION_CAUTION
   :tools: TOOL_SPHINX
   :si: no

   Use the caution admonition to warn about potential problems.

   .. code-block:: rst

      .. caution::

         Proceed with caution.

.. feature:: Error Admonition
   :id: FE_SPHINX_ADMONITION_ERROR
   :tools: TOOL_SPHINX
   :si: no

   Use the error admonition to indicate errors or critical issues.

   .. code-block:: rst

      .. fault::

         This is an error.

.. feature:: Danger Admonition
   :id: FE_SPHINX_ADMONITION_DANGER
   :tools: TOOL_SPHINX
   :si: no

   Use the danger admonition to highlight severe risks.

   .. code-block:: rst

      .. danger::

         This is dangerous.

.. feature:: Generic Admonition
   :id: FE_SPHINX_ADMONITION_GENERIC
   :tools: TOOL_SPHINX
   :si: no

   Use the generic admonition to create custom-styled notes.

   .. code-block:: rst

      .. admonition:: Custom Title

         This is a custom admonition.

Hyperlinks and Cross-Referencing
++++++++++++++++++++++++++++++++

.. feature:: External Hyperlinks
   :id: FE_SPHINX_LINK_EXTERNAL
   :tools: TOOL_SPHINX
   :si: no

   Use external hyperlinks to link to external resources.

   .. code-block:: rst

      `Sphinx Documentation <https://www.sphinx-doc.org/en/master/>`__

.. feature:: Implicit Hyperlinks from URLs
   :id: FE_SPHINX_LINK_IMPLICIT
   :tools: TOOL_SPHINX
   :si: no

   Use implicit hyperlinks to automatically create links from URLs.

   .. code-block:: rst

      https://www.sphinx-doc.org/en/master/

.. feature:: Internal Cross-References to Labels
   :id: FE_SPHINX_LINK_INTERNAL_LABELS
   :tools: TOOL_SPHINX
   :si: no

   Use internal cross-references to link to labeled sections.

   .. code-block:: rst

      See :ref:`example-section` for more details.

.. feature:: Explicit Target Creation
   :id: FE_SPHINX_LINK_EXPLICIT_TARGET
   :tools: TOOL_SPHINX
   :si: no

   Use explicit targets to create reusable links.

   .. code-block:: rst

      .. _example-target:

      This is the target.

      See :ref:`example-target`.

.. feature:: Reference Role
   :id: FE_SPHINX_ROLE_REF
   :tools: TOOL_SPHINX
   :si: no

   Use the reference role to create cross-references.

   .. code-block:: rst

      :ref:`example-section`

.. feature:: Document Role
   :id: FE_SPHINX_ROLE_DOC
   :tools: TOOL_SPHINX
   :si: no

   Use the document role to link to other documents.

   .. code-block:: rst

      :doc:`usage`

.. feature:: Numbered Reference Role
   :id: FE_SPHINX_ROLE_NUMREF
   :tools: TOOL_SPHINX
   :si: no

   Use the numbered reference role to create numbered cross-references.

   .. code-block:: rst

      :numref:`example-figure`

.. feature:: Footnotes
   :id: FE_SPHINX_LINK_FOOTNOTES
   :tools: TOOL_SPHINX
   :si: no

   Use footnotes to provide additional information or references.

   .. code-block:: rst

      This is a sentence with a footnote. [#]_

      .. [#] This is the footnote text.

.. feature:: Citations
   :id: FE_SPHINX_LINK_CITATIONS
   :tools: TOOL_SPHINX
   :si: no

   Use citations to reference external sources.

   .. code-block:: rst

      This is a citation. [CITATION]_

      .. [CITATION] Author, Title, Year.

Output and Build System
+++++++++++++++++++++++

.. feature:: HTML Output
   :id: FE_SPHINX_OUTPUT_HTML
   :tools: TOOL_SPHINX
   :si: yes

   Generate HTML output for your documentation.

   .. code-block:: bash

      sphinx-build -b html source/ build/html/

.. feature:: Single-File HTML Output
   :id: FE_SPHINX_OUTPUT_SINGLE_HTML
   :tools: TOOL_SPHINX
   :si: yes

   Generate a single HTML file for your documentation.

   .. code-block:: bash

      sphinx-build -b singlehtml source/ build/singlehtml/

.. feature:: Directory HTML Output
   :id: FE_SPHINX_OUTPUT_DIR_HTML
   :tools: TOOL_SPHINX
   :si: yes   

   Generate HTML output with a directory structure.

   .. code-block:: bash

      sphinx-build -b dirhtml source/ build/dirhtml/

.. feature:: LaTeX Output
   :id: FE_SPHINX_OUTPUT_LATEX
   :tools: TOOL_SPHINX
   :si: yes

   Generate LaTeX output for your documentation.

   .. code-block:: bash

      sphinx-build -b latex source/ build/latex/

.. feature:: ePub 3 Output
   :id: FE_SPHINX_OUTPUT_EPUB
   :tools: TOOL_SPHINX
   :si: yes

   Generate ePub output for your documentation.

   .. code-block:: bash

      sphinx-build -b epub source/ build/epub/

.. feature:: Man Page Output
   :id: FE_SPHINX_OUTPUT_MANPAGE
   :tools: TOOL_SPHINX

   Generate man page output for your documentation.

   .. code-block:: bash

      sphinx-build -b man source/ build/man/

.. feature:: Plain Text Output
   :id: FE_SPHINX_OUTPUT_TEXT
   :tools: TOOL_SPHINX

   Generate plain text output for your documentation.

   .. code-block:: bash

      sphinx-build -b text source/ build/text/

.. feature:: JSON Output
   :id: FE_SPHINX_OUTPUT_JSON
   :tools: TOOL_SPHINX

   Generate JSON output for your documentation.

   .. code-block:: bash

      sphinx-build -b json source/ build/json/

.. feature:: Gettext Message Catalog Output
   :id: FE_SPHINX_OUTPUT_GETTEXT
   :tools: TOOL_SPHINX

   Generate gettext message catalogs for translations.

   .. code-block:: bash

      sphinx-build -b gettext source/ build/gettext/

.. feature:: Built-in HTML Search
   :id: FE_SPHINX_BUILD_HTML_SEARCH
   :tools: TOOL_SPHINX

   Enable built-in search functionality for HTML output.

   .. code-block:: rst

      .. search::

.. feature:: HTML Theming Support
   :id: FE_SPHINX_BUILD_THEMING
   :tools: TOOL_SPHINX

   Customize the appearance of HTML output using themes.

   .. code-block:: rst

      html_theme = 'alabaster'

.. feature:: Static File Support
   :id: FE_SPHINX_BUILD_STATIC_FILES
   :tools: TOOL_SPHINX

   Include static files like images, CSS, or JavaScript in your build.

   .. code-block:: rst

      html_static_path = ['_static']
