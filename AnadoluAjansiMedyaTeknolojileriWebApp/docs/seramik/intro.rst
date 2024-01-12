Seramik Object Features
=======================

The Seramik object encapsulates a rich set of features for content analysis. Below are the key components organized in tabular format.

Identification
--------------

+--------------+----------------------------------------------------------+
| Field        | Description                                              |
+==============+==========================================================+
| input_id     | Unique Identifier for the Input Record                    |
+--------------+----------------------------------------------------------+
| input_type   | Type of Input (e.g., article, tweet, report, image, etc.) |
+--------------+----------------------------------------------------------+
| timestamp    | Timestamp of the Input Creation in ISO 8601 format        |
+--------------+----------------------------------------------------------+

Source Information
------------------

+------------+--------------------------------------+
| Field      | Description                          |
+============+======================================+
| source     | Name of the Source (e.g., publication|
|            | , website, author)                   |
+------------+--------------------------------------+
| city       | City where the source is located     |
+------------+--------------------------------------+
| country    | Country where the source is located  |
+------------+--------------------------------------+
| location   | Geographical coordinates (latitude,  |
|            | longitude) of the Source             |
+------------+--------------------------------------+

Content Analysis
----------------

+---------------------+---------------------------------------------+
| Field               | Description                                 |
+=====================+=============================================+
| detailed_description| A detailed description of the content       |
+---------------------+---------------------------------------------+
| summary             | A concise summary of the content            |
+---------------------+---------------------------------------------+
| keywords            | List of primary keywords                    |
+---------------------+---------------------------------------------+

AI Analysis
-----------

+-------------------+--------------------------------------------------+
| Field             | Description                                      |
+===================+==================================================+
| emotion_analysis  | Analysis of primary and secondary emotions       |
+-------------------+--------------------------------------------------+
| object_detection  | Details of objects detected (name, status, action|
|                   | )                                                |
+-------------------+--------------------------------------------------+
| text_extraction   | Segments of extracted text                       |
+-------------------+--------------------------------------------------+

Additional Metadata
-------------------

+----------------------+--------------------------------------------------+
| Field                | Description                                      |
+======================+==================================================+
| source_attributes    | Attributes of the Source                          |
+----------------------+--------------------------------------------------+
| content_themes       | Main themes of the Content                        |
+----------------------+--------------------------------------------------+
| audience             | Intended Audience Types                          |
+----------------------+--------------------------------------------------+
| geographic_relevance | Geographic Areas relevant to the Content         |
+----------------------+--------------------------------------------------+
| temporal_relevance   | Relevant Time Periods or Dates                   |
+----------------------+--------------------------------------------------+
| technical_level      | Technical Complexity Levels of the Content       |
+----------------------+--------------------------------------------------+
| sentiment_trends     | Predominant Sentiment Trends in the Content      |
+----------------------+--------------------------------------------------+
| influencer_tags      | Tags related to Key Influencers or Stakeholders  |
+----------------------+--------------------------------------------------+

Each of these features are designed to provide a comprehensive understanding of the content, making Seramik a versatile tool for content analysis.
