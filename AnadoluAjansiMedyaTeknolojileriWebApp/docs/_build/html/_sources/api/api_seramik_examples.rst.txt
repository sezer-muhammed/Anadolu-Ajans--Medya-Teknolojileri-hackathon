InputRecord API Examples
========================

This section provides examples of how to interact with the InputRecord API using Python and command-line tools. Authentication is required for all API endpoints.

Python Requests Examples
------------------------

.. code-block:: python

    import requests
    import json

    # Base URL for the API
    base_url = 'http://example.com/api/inputrecords/'
    login_url = 'http://example.com/api-auth/login/'
    headers = {'Content-Type': 'application/json'}

    # Session Authentication
    session = requests.Session()
    session.post(login_url, data={'username': 'your_username', 'password': 'your_password'})

    # Example JSON data for POST request
    data = {
        "input_id": "12345",
        "input_type": "article",
        "timestamp": "2024-01-12T12:00:00",
        "source_info": {
            "source": "Example News",
            "city": "New York",
            "country": "USA",
            "location": {
                "latitude": "40.7128",
                "longitude": "-74.0060"
            }
        },
        "content_analysis": {
            "detailed_description": "This article discusses the impact of AI in modern healthcare...",
            "summary": "AI's role in healthcare transformation",
            "keywords": [
                {"value": "AI"},
                {"value": "Healthcare"},
                {"value": "Technology"}
            ]
        },
        "ai_analysis": {
            "emotion_analysis": {
                "associated_emotions": [
                    {"emotion": "Curiosity"},
                    {"emotion": "Optimism"}
                ]
            },
            "object_detection": [
                {"name": "Robot", "status": "Detected", "action": "Analyze further"},
                {"name": "Hospital Equipment", "status": "Detected", "action": "Review"}
            ],
            "text_extraction": [
                {"text": "Artificial Intelligence in Hospitals"},
                {"text": "Revolutionizing Patient Care"}
            ]
        },
        "additional_metadata": {
            "source_attributes": [
                {"attribute": "Credible"},
                {"attribute": "Renowned"}
            ],
            "content_themes": [
                {"theme": "Innovation"},
                {"theme": "Healthcare Technology"}
            ],
            "audience": [
                {"audience_type": "Medical Professionals"},
                {"audience_type": "Tech Enthusiasts"}
            ],
            "geographic_relevance": [
                {"geography": "Global"},
                {"geography": "North America"}
            ],
            "temporal_relevance": [
                {"temporal": "2024"},
                {"temporal": "Q1"}
            ],
            "technical_level": [
                {"level": "Advanced"},
                {"level": "Intermediate"}
            ],
            "sentiment_trends": [
                {"trend": "Positive"},
                {"trend": "Engaging"}
            ],
            "influencer_tags": [
                {"tag": "AI Expert"},
                {"tag": "Healthcare Innovator"}
            ]
        }
    }

    # POST request to create a new Input Record
    response = session.post(base_url, headers=headers, data=json.dumps(data))
    print(response.json())

Command Line Curl Examples
--------------------------

.. code-block:: bash

    # Session Authentication using Curl
    curl -c cookies.txt -d "username=your_username&password=your_password" http://example.com/api-auth/login/

    # Example JSON data for POST request
    data='{
        "input_id": "12345",
        "input_type": "article",
        "timestamp": "2024-01-12T12:00:00",
        # Include the rest of the JSON data structure here...
    }'

    # POST request to create a new Input Record
    curl -b cookies.txt -X POST http://example.com/api/inputrecords/ -H "Content-Type: application/json" -d "$data"
