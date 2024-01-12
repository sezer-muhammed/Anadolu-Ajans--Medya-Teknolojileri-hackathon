API Reference: InputRecords Endpoint
====================================

Endpoint Overview
-----------------

- **URL**: `/api/inputrecords`
- **Method**: `GET`, `POST`
- **Authentication**: Required (Session Authentication)
- **Permission**: Only Authenticated Users

Authentication and Permissions
------------------------------

- The endpoint requires users to be authenticated using Session Authentication.
- Only authenticated users with valid permissions can access this endpoint.

JSON Request Structure for POST
-------------------------------

.. code-block:: json

    {
      "instructions": "Generate a detailed and realistic JSON response for an input record. Each field should contain relevant and contextually appropriate data. Reflect a scenario where the input is an article or a document being analyzed for content, source, sentiment, and other metadata.",
      "template": {
        "input_id": "<Unique Identifier for the Input Record>",
        "input_type": "<Type of Input (e.g., article, tweet, report, image, voice, )>",
        "timestamp": "<Timestamp of the Input Creation in ISO 8601 format>",
        "source_info": {
          "source": "<Name of the Source (e.g., publication, website, author)>",
          "city": "<City where the source is located>",
          "country": "<Country where the source is located>",
          "location": {
            "latitude": "<Latitude of the Source>",
            "longitude": "<Longitude of the Source>"
          }
        },
        "content_analysis": {
          "detailed_description": "<A detailed description of the content>",
          "summary": "<A concise summary of the content>",
          "keywords": [
            {"value": "<Primary Keyword 1>"},
            {"value": "<Primary Keyword 2>"},
            {"value": "<Keep adding primary keywords here...>"}
          ]
        },
        "ai_analysis": {
          "emotion_analysis": {
            "associated_emotions": [
              {"emotion": "<Primary Emotion Detected>"},
              {"emotion": "<Secondary Emotion Detected>"},
              {"emotion": "<Keep adding emotions here...>"}
            ]
          },
          "object_detection": [
            {"name": "<Name of the Detected Object>", "status": "<Detection Status>", "action": "<Recommended Action>"},
            {"name": "<Another Detected Object>", "status": "<Detection Status>", "action": "<Recommended Action>"},
            {"name": "Keep adding detected objects here...", "status": "<Detection Status>", "action": "<Recommended Action>"}
          ],
          "text_extraction": [
            {"text": "<Extracted Text Segment 1>"},
            {"text": "<Extracted Text Segment 2>"},
            {"text": "Keep adding extracted text segments here..."}
          ]
        },
        "additional_metadata": {
          "source_attributes": [
            {"attribute": "<Attribute of the Source 1>"},
            {"attribute": "<Attribute of the Source 2>"},
            {"attribute": "Keep adding attributes here..."}
          ],
          "content_themes": [
            {"theme": "<Main Theme of the Content 1>"},
            {"theme": "<Main Theme of the Content 2>"},
            {"theme": "Keep adding themes here..."}
          ],
          "audience": [
            {"audience_type": "<Intended Audience Type 1>"},
            {"audience_type": "<Intended Audience Type 2>"},
            {"audience_type": "Keep adding audience types here..."}
          ],
          "geographic_relevance": [
            {"geography": "<Geographic Area Relevant to the Content 1>"},
            {"geography": "<Geographic Area Relevant to the Content 2>"},
            {"geography": "Keep adding geographic areas here..."}
          ],
          "temporal_relevance": [
            {"temporal": "<Relevant Time Period or Date 1>"},
            {"temporal": "<Relevant Time Period or Date 2>"},
            {"temporal": "Keep adding relevant time periods or dates here..."}
          ],
          "technical_level": [
            {"level": "<Technical Complexity Level of the Content 1>"},
            {"level": "<Technical Complexity Level of the Content 2>"},
            {"level": "Keep adding technical complexity levels here..."}
          ],
          "sentiment_trends": [
            {"trend": "<Predominant Sentiment Trend in the Content 1>"},
            {"trend": "<Predominant Sentiment Trend in the Content 2>"},
            {"trend": "Keep adding sentiment trends here..."}
          ],
          "influencer_tags": [
            {"tag": "<Tag Related to Key Influencers or Stakeholders 1>"},
            {"tag": "<Tag Related to Key Influencers or Stakeholders 2>"},
            {"tag": "Keep adding tags here..."}
          ]
        }
      }
    }

Example Usage for POST
----------------------

.. code-block:: python

    # Example usage in a Django view
    serializer = InputRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=400)

Example Usage for GET
---------------------

To retrieve existing `InputRecord` data using the API:

1. Make a GET request to the endpoint: `/api/inputrecords`.
2. Include appropriate authentication headers based on the Session Authentication method.

Example using `curl`:

.. code-block:: bash

    curl http://<your_domain>/api/inputrecords

This command sends a GET request to the `/api/inputrecords` endpoint. Replace `YOUR_API_TOKEN` with your actual API token and `<your_domain>` with your API's domain. The response will be a list of `InputRecord` objects in JSON format, assuming the request is authenticated and authorized.


Retrieving a Specific InputRecord (GET)
---------------------------------------

- To retrieve a specific `InputRecord` by its index or ID, make a GET request to `/api/inputrecords/<id>`.
- The URL parameter `<id>` should be replaced with the actual ID of the `InputRecord`.
- This request returns a single `InputRecord` object, provided the user has the necessary permissions and is authenticated.

Example Usage for Retrieving a Specific Record
----------------------------------------------

Using `curl`:

.. code-block:: bash

    curl http://<your_domain>/api/inputrecords/<id>

Replace `<your_domain>` with your API's domain, and `<id>` with the ID of the specific `InputRecord` you want to retrieve. The response will be the `InputRecord` object in JSON format if the ID is valid and the request is authorized.
