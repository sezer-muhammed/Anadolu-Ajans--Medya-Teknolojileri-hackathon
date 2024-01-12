Text and Image Upload API Examples
==================================

.. note:: This API requires session-based authentication. Users must be authenticated to access the endpoints.

Python Requests Examples
------------------------

Import the `requests` library to use these examples.

.. code-block:: python

    import requests

    # Base URL for the API
    base_url = 'http://example.com/api/'
    login_url = 'http://example.com/api-auth/login/'

    # Log in to the API to establish a session
    credentials = {'username': 'your_username', 'password': 'your_password'}
    session = requests.Session()
    session.post(login_url, data=credentials)

    # GET request for Text Uploads
    response = session.get(f'{base_url}texts/')
    print(response.json())

    # POST request to create a new Text Upload
    new_text = {'text': 'Sample text data'}
    response = session.post(f'{base_url}texts/', data=new_text)
    print(response.json())

    # PATCH request to update an existing Text Upload
    updated_text = {'text': 'Updated text data'}
    response = session.patch(f'{base_url}texts/1/', data=updated_text)
    print(response.json())

    # GET request for Image Uploads
    response = session.get(f'{base_url}images/')
    print(response.json())

    # POST request to create a new Image Upload
    # Note: Replace 'path/to/image.jpg' with the actual file path
    with open('path/to/image.jpg', 'rb') as img:
        response = session.post(f'{base_url}images/', files={'image': img})
    print(response.json())

Command Line Curl Examples
--------------------------

These command-line examples use `curl` for making HTTP requests.

.. code-block:: bash

    # Log in to establish a session
    # The session cookie will be used in subsequent requests
    curl -c cookies.txt -d "username=your_username&password=your_password" http://example.com/api-auth/login/

    # GET request for Text Uploads
    curl -b cookies.txt http://example.com/api/texts/

    # POST request to create a new Text Upload
    curl -b cookies.txt -d "text=Sample text data" http://example.com/api/texts/

    # PATCH request to update an existing Text Upload
    curl -b cookies.txt -X PATCH -d "text=Updated text data" http://example.com/api/texts/1/

    # GET request for Image Uploads
    curl -b cookies.txt http://example.com/api/images/

    # POST request to create a new Image Upload
    # Note: Replace 'path/to/image.jpg' with the actual file path
    curl -b cookies.txt -F "image=@path/to/image.jpg" http://example.com/api/images/
