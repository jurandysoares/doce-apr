# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Doce-APR'
copyright = '2026, Jurandy Soares'
author = 'Jurandy Soares'
release = '2026.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'furo'
html_theme = 'sphinx_book_theme'
#html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = html_short_title = project
html_theme_options = {
    # Options for sphinx-book-theme
    "repository_url": "https://github.com/jurandysoares/doce-apr/",
    "repository_branch": "main",
    "path_to_docs": "docs/",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,

    # Options for furo
    #    "source_repository": "https://github.com/jurandysoares/doce-apr/",
    #    "source_branch": "main",
    #    "source_directory": "docs/",

    # Options for pydata-sphinx-theme

}
