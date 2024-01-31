Image Generator App
===================

This section documents the components of the Image Generator app, including models, views, serializers, and other configurations.

Models
------

The models define the data structure.

.. automodule:: image_generator.models
   :members:
   :undoc-members:
   :show-inheritance:

Views
-----

Views handle requests and responses.

.. automodule:: image_generator.views
   :members:
   :undoc-members:
   :show-inheritance:

Serializers
-----------

Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

.. automodule:: image_generator.serializers
   :members:
   :undoc-members:
   :show-inheritance:

URLs
----

URL configurations define the URL mappings to views.

.. code-block:: python

   # image_generator.urls
   from django.urls import path
   from . import views

   urlpatterns = [
       # Define your URL patterns here
   ]

Admin
-----

The admin module customizes the admin interface.

.. automodule:: image_generator.admin
   :members:
   :undoc-members:
   :show-inheritance:

Tests
-----

This section would include documentation on tests written for the app.

.. automodule:: image_generator.tests
   :members:
   :undoc-members:
   :show-inheritance:
