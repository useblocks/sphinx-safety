# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

import jinja2

# We need to make Python aware of our project source code, which is stored outside `/docs`,
# under `src/`
code_path = os.path.join(os.path.dirname(__file__), "../", "src/")
sys.path.append(code_path)
print(f"CODE_PATH: {code_path}")


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sphinx Classification"
copyright = "2025, team useblocks"
author = "team useblocks and friends"
version = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# List of Sphinx extension to use.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_needs",
    "sphinx_design",
    "sphinxcontrib.plantuml",
    "sphinx_simplepdf",
]


intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "needs": ("https://sphinx-needs.readthedocs.io/en/latest/", None),
}

###############################################################################
# SPHINX-NEEDS Config START
###############################################################################

# Read the configuration from an external TOML file.
# This makes it possible to use ubCode and its tools directly with
# the project. Declarative configuration formats are also preferred as they
# cannot contain logic and can be consumed by almost all languages.
needs_from_toml = "ubproject.toml"

needs_string_links = {
    # Adds link to the Sphinx-Needs configuration page
    'config_link': {
        'regex': r'^(?P<value>.*)$',
        'link_url': '{{value}}',
        'link_name': 'GitHub',
        'options': ['url']
    },
}


###############################################################################
# SPHINX-NEEDS Config END
###############################################################################


templates_path = ["_templates"]

# List of files/folder to ignore.
# Sphinx builds all ``.rst`` files under ``/docs``, no matte if they are part
# of a toctree or not. So as we have some rst-templates, we need to tell Sphinx to ignore
# these files.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".venv",
    ".ub_cache",
    "_build",
    "**/main.rst"
]

# We bring our own plantuml jar file.
# These options tell Sphinxcontrib-PlantUML we it can find this file.
local_plantuml_path = os.path.join(
    os.path.dirname(__file__), "utils", "plantuml-1.2022.14.jar"
)
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
# plantuml_output_format = 'png'
plantuml_output_format = "svg_img"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_theme_options = {
    "sidebar_hide_name": True,
    "top_of_page_buttons": ["view", "edit"],
    "source_repository": "https://github.com/useblocks/sphinx-safety",
    "source_branch": "main",
    "source_directory": "/",
    "light_logo": "logo_sphinx_classification_light.png",
    "dark_logo": "logo_sphinx_classification_dark.png",
}
html_css_files = ["custom.css"]


# -- Custom dynamic functions ------------------------------------------------
from sphinx_needs.api import add_dynamic_function  # noqa: E402
from sphinx_safety.needs_functions import calculate_tcl  # noqa: E402


def setup(app):
    add_dynamic_function(app, calculate_tcl)
