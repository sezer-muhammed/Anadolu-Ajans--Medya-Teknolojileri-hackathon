Text and Image Upload API Documentation
=======================================

Introduction
------------
The Text and Image Upload API provides functionalities for uploading and managing text and image data. This documentation describes the available endpoints for interacting with text and image data stored in the system.

Models
------
+-----------------------+----------------------------+
| TextUpload Model      | ImageUpload Model          |
+=======================+============================+
| **Fields**:           | **Fields**:                |
+-----------------------+----------------------------+
| `text`: Stores text   | `image`: Stores the path   |
| data.                 | to the uploaded image.     |
+-----------------------+----------------------------+

Serializers
-----------
+-----------------------+----------------------------+
| TextUploadSerializer  | ImageUploadSerializer      |
+=======================+============================+
| **Fields**:           | **Fields**:                |
+-----------------------+----------------------------+
| `text`: The text data | `image`: The image file to |
| to be uploaded.       | be uploaded.               |
+-----------------------+----------------------------+

API Endpoints
-------------
The API is accessible under the `/api/` URL.

+-------------------------+-------------------------------+
| Text Upload Endpoints   | Image Upload Endpoints        |
+=========================+===============================+
| **URL**: `/api/texts/`  | **URL**: `/api/images/`       |
+-------------------------+-------------------------------+
| **Supported Methods**:  | **Supported Methods**:        |
+-------------------------+-------------------------------+
| `GET`: List all text    | `GET`: List all image uploads.|
| uploads.                |                               |
+-------------------------+-------------------------------+
| `POST`: Create a new    | `POST`: Create a new image    |
| text upload.            | upload.                       |
+-------------------------+-------------------------------+
| **Specific Text Upload**| **Specific Image Upload**:    |
+-------------------------+-------------------------------+
| **URL**: `/api/texts/{id}/` | **URL**: `/api/images/{id}/` |
+-------------------------+-------------------------------+
| `GET`: Retrieve a       | `GET`: Retrieve a specific    |
| specific text upload.   | image upload.                 |
+-------------------------+-------------------------------+
| `PUT/PATCH`: Update a   | `PUT/PATCH`: Update a         |
| specific text upload.   | specific image upload.        |
+-------------------------+-------------------------------+
| `DELETE`: Delete a      | `DELETE`: Delete a specific   |
| specific text upload.   | image upload.                 |
+-------------------------+-------------------------------+
