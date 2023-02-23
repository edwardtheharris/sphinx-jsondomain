"""Sphinx configuration."""
# pylint: disable=invalid-name
from pathlib import Path


def get_version():
    """Return current version."""
    with Path('../version').open('r', encoding='utf-8') as v_fh:
        f_version = v_fh.read()
    return f_version


# # pylint: disable=redefined-builtin
# copyright = '2016, Dave Shawley'
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx_jsondomain',
]
html_sidebars = {
    '**': ['about.html', 'navigation.html'], }
html_static_path = ['_static']
html_theme = 'furo'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None), }
master_doc = 'index'
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "inv_link",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
needs_sphinx = '4.0'
project = 'sphinx-jsondomain'
release = get_version()
version = get_version()
