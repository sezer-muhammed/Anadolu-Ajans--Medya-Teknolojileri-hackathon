API App Documentation
=====================

This documentation covers the components of the API app within the Anadolu Ajansi Medya Teknolojileri Web Application. The app includes models, views, serializers, and interfaces for OpenAI integration, among others.

Models
------

The models define the data structure for the API app.

.. automodule:: api.models
   :members:
   :undoc-members:
   :show-inheritance:

Views
-----

Views handle the request-response cycle for the API.

.. automodule:: api.views
   :members:
   :undoc-members:
   :show-inheritance:

Serializers
-----------

Serializers are responsible for converting models into JSON format for API responses.

.. automodule:: api.serializers
   :members:
   :undoc-members:
   :show-inheritance:

URLs
----

URL configurations map endpoints to views.

.. code-block:: python

   # api.urls
   from django.urls import path
   from . import views

   urlpatterns = [
       # Define your URL patterns here
   ]

Admin
-----

Customizations to the Django admin interface for the API app.

.. automodule:: api.admin
   :members:
   :undoc-members:
   :show-inheritance:

OpenAI Interface
----------------

Defines interactions with OpenAI's APIs.

.. automodule:: api.openai_interface
   :members:
   :undoc-members:
   :show-inheritance:

Callbacks
---------

Custom callback functions used within the app.

.. automodule:: api.callbacks
   :members:
   :undoc-members:
   :show-inheritance:

Validators
----------

Validators ensure the integrity of data being processed by the app.

.. automodule:: api.validators
   :members:
   :undoc-members:
   :show-inheritance:

Tests
-----

Documentation of tests for the API app.

.. automodule:: api.tests
   :members:
   :undoc-members:
   :show-inheritance:
