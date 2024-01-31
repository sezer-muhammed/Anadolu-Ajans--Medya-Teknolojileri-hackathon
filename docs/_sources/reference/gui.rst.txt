GUI App Documentation
=====================

This section provides documentation for the GUI (Graphical User Interface) app, detailing its forms, views, and integrations, particularly focusing on its role in providing a user interface for the Anadolu Ajansi Medya Teknolojileri Web Application.

Forms
-----

The `forms.py` file contains form classes that are used for data input and submissions through the web interface.

.. automodule:: GUI.forms
   :members:
   :undoc-members:
   :show-inheritance:

Views
-----

Views handle the request-response cycle for the GUI, rendering templates and forms as needed.

.. automodule:: GUI.views
   :members:
   :undoc-members:
   :show-inheritance:

URLs
----

The URL configurations map endpoints to their corresponding views within the GUI app.

.. code-block:: python

   # GUI.urls
   from django.urls import path
   from . import views

   urlpatterns = [
       # Define your URL patterns here
   ]

OpenAI Interface
----------------

This module facilitates interaction with OpenAI's API, integrating AI functionalities into the GUI components.

.. automodule:: GUI.openai_interface
   :members:
   :undoc-members:
   :show-inheritance:

Templates
---------

The `templates` directory contains HTML files that define the layout and structure of the web interface. While Sphinx does not automatically document these, it's important to note that templates are closely linked with views, rendering dynamic content served to the user.

Admin
-----

While minimal, the admin module can be customized for the GUI app as needed.

.. automodule:: GUI.admin
   :members:
   :undoc-members:
   :show-inheritance:

Models
------

Although the GUI app might have minimal model definitions, it's crucial to document any data structures it defines or interacts with.

.. automodule:: GUI.models
   :members:
   :undoc-members:
   :show-inheritance:

Tests
-----

Documentation of tests written for the GUI app's functionality.

.. automodule:: GUI.tests
   :members:
   :undoc-members:
   :show-inheritance:
