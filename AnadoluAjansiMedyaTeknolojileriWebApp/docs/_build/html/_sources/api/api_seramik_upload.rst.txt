InputRecord API Endpoints
=========================

The InputRecord API provides a comprehensive interface for managing and accessing a wide range of media-related data. This includes input records, source information, content analysis, AI detection, and additional metadata.

Models and Serializers
----------------------

.. csv-table:: Models and Corresponding Serializers
   :header: "Model", "Serializer", "Description"
   :widths: 20, 30, 50

   "InputRecord", "InputRecordSerializer", "Main model for storing input records."
   "SourceInfo", "SourceInfoSerializer", "Contains source-related information like source, city, country."
   "SourceLocation", "SourceLocationSerializer", "Details the geographic location with latitude and longitude."
   "ContentAnalysis", "ContentAnalysisSerializer", "Captures detailed description and summary of the content along with keywords."
   "Keyword", "KeywordSerializer", "Stores individual keywords."
   "EmotionAnalysis", "EmotionAnalysisSerializer", "Handles analysis of emotions associated with the content."
   "AssociatedEmotion", "AssociatedEmotionSerializer", "Records specific emotions associated with the content."
   "Object", "ObjectSerializer", "Details objects identified within the content."
   "TextExtraction", "TextExtractionSerializer", "Manages extracted text data from the content."
   "AIDetection", "AIDetectionSerializer", "Encapsulates AI-based detections like emotion analysis, object detection, and text extraction."
   "AdditionalMetadata", "AdditionalMetadataSerializer", "Stores extra metadata like source attributes, content themes, audience, etc."
   "SourceAttribute", "SourceAttributeSerializer", "Records additional attributes of the source."
   "ContentTheme", "ContentThemeSerializer", "Details the themes associated with the content."
   "Audience", "AudienceSerializer", "Captures information about the intended audience."
   "GeographicRelevance", "GeographicRelevanceSerializer", "Indicates the geographic relevance of the content."
   "TemporalRelevance", "TemporalRelevanceSerializer", "Details the temporal relevance of the content."
   "TechnicalLevel", "TechnicalLevelSerializer", "Indicates the technical level of the content."
   "SentimentTrend", "SentimentTrendSerializer", "Captures the trend in sentiment around the content."
   "InfluencerTag", "InfluencerTagSerializer", "Stores tags related to influencers mentioned in the content."


API Endpoints
-------------

- **URL**: `/api/inputrecords/`
  - **Supported Methods**:
    - `GET`: Retrieve a list of input records.
    - `POST`: Create a new input record.
  - **Specific Record**:
    - **URL**: `/api/inputrecords/{id}/`
    - **Supported Methods**:
      - `GET`: Retrieve a specific input record.
      - `PUT/PATCH`: Update a specific input record.
      - `DELETE`: Delete a specific input record.
