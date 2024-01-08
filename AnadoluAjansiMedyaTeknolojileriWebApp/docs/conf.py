# -- Project information -----------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'AnadoluAjansiMedyaTeknolojileriWebApp.settings'
import django
django.setup()

project = 'Anadolu Ajansı Medya Teknolojileri Web App'
copyright = '2024, Muhammed Sezer'
author = 'Muhammed Sezer, Şevval Belkıs Dikkaya, Ahmet Sezer, Metehan İçöz'
release = 'Version 1.0'

# -- General configuration ---------------------------------------------------

html_theme = 'sphinx_rtd_theme'

extensions = [
    'sphinx.ext.autodoc',  # Include documentation from docstrings
    'sphinx.ext.viewcode',  # Add links to source code
    'sphinxcontrib_django',  # Specific for Django
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
]

# Theme options and customization
html_theme_options = {
    'navigation_depth': 4,
    'display_version': True,
    'collapse_navigation': True,  # Collapse navigation for a cleaner look
    'sticky_navigation': True,  # Ensures the navigation pane stays while scrolling
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Intersphinx mapping for Django 5.0
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/5.0/', None),
}

# Enable todos
todo_include_todos = True

# Sphinxcontrib Django
# It's good to specify the settings here for your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Ensure that the theme is set to Read The Docs theme
import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- Options for sphinxcontrib_django ---------------------------------------

# Document all available fields in models (default: True)
sphinxcontrib_django_settings = {
    'doc_fields': True,
}

# If you have a custom user model and want to document it properly
django_settings_module = os.environ['DJANGO_SETTINGS_MODULE']
