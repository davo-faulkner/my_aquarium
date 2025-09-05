# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Davo, you'll need these imports for automatic documentation:
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Davo's Demo Project"
copyright = '2025, David Faulkner'
author = 'David Faulkner'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Davo, this extensions automates documentation for the project:
extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
# Davo, add `.env/*` to the line below to exclude your venv.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.env/*']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# Davo, you may need to comment the following line depending on your theme.
html_static_path = ['_static']

# Davo, add these lines to link to other Sphinx projects:
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
}
