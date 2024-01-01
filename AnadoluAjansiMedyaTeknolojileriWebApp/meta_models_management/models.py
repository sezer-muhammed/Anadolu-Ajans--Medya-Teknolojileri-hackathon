from django.db import models

# Models for each list of strings
class Keyword(models.Model):
    value = models.CharField(max_length=200)

class AssociatedEmotion(models.Model):
    emotion = models.CharField(max_length=200)

class Object(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    action = models.CharField(max_length=200)

class TextExtraction(models.Model):
    text = models.CharField(max_length=1000)

class SourceAttribute(models.Model):
    attribute = models.CharField(max_length=200)

class ContentTheme(models.Model):
    theme = models.CharField(max_length=200)

class Audience(models.Model):
    audience_type = models.CharField(max_length=200)

class GeographicRelevance(models.Model):
    geography = models.CharField(max_length=200)

class TemporalRelevance(models.Model):
    temporal = models.CharField(max_length=200)

class TechnicalLevel(models.Model):
    level = models.CharField(max_length=200)

class SentimentTrend(models.Model):
    trend = models.CharField(max_length=200)

class InfluencerTag(models.Model):
    tag = models.CharField(max_length=200)

# Main models
class SourceLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class SourceInfo(models.Model):
    source = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    location = models.OneToOneField(SourceLocation, on_delete=models.CASCADE)

class ContentAnalysis(models.Model):
    detailed_description = models.TextField()
    summary = models.TextField()
    keywords = models.ManyToManyField(Keyword, related_name='content_analysis_keywords')

class EmotionAnalysis(models.Model):
    associated_emotions = models.ManyToManyField(AssociatedEmotion, related_name='emotion_analysis_emotions')

class AIDetection(models.Model):
    emotion_analysis = models.OneToOneField(EmotionAnalysis, on_delete=models.CASCADE)
    object_detection = models.ManyToManyField(Object, related_name='ai_detection_objects')
    text_extraction = models.ManyToManyField(TextExtraction, related_name='ai_detection_texts')

class AdditionalMetadata(models.Model):
    """
    Represents additional metadata associated with a model.
    
    Attributes:
        source_attributes (ManyToManyField): The source attributes associated with the metadata.
        content_themes (ManyToManyField): The content themes associated with the metadata.
        audience (ManyToManyField): The audience associated with the metadata.
        geographic_relevance (ManyToManyField): The geographic relevance associated with the metadata.
        temporal_relevance (ManyToManyField): The temporal relevance associated with the metadata.
        technical_level (ManyToManyField): The technical level associated with the metadata.
        sentiment_trends (ManyToManyField): The sentiment trends associated with the metadata.
        influencer_tags (ManyToManyField): The influencer tags associated with the metadata.
    """
    source_attributes = models.ManyToManyField(SourceAttribute, related_name='additional_metadata_source_attributes')
    content_themes = models.ManyToManyField(ContentTheme, related_name='additional_metadata_content_themes')
    audience = models.ManyToManyField(Audience, related_name='additional_metadata_audience')
    geographic_relevance = models.ManyToManyField(GeographicRelevance, related_name='additional_metadata_geographic_relevance')
    temporal_relevance = models.ManyToManyField(TemporalRelevance, related_name='additional_metadata_temporal_relevance')
    technical_level = models.ManyToManyField(TechnicalLevel, related_name='additional_metadata_technical_level')
    sentiment_trends = models.ManyToManyField(SentimentTrend, related_name='additional_metadata_sentiment_trends')
    influencer_tags = models.ManyToManyField(InfluencerTag, related_name='additional_metadata_influencer_tags')

class InputRecord(models.Model):
    """
    Represents an input record in the system.

    Attributes:
        input_id (str): The ID of the input.
        input_type (str): The type of the input.
        timestamp (str): The timestamp of the input. Consider using DateTimeField if the format is consistent.
        source_info (SourceInfo): The source information associated with the input.
        content_analysis (ContentAnalysis): The content analysis associated with the input.
        ai_analysis (AIDetection): The AI analysis associated with the input.
        additional_metadata (AdditionalMetadata): Additional metadata associated with the input.
    """
    input_id = models.CharField(max_length=200)
    input_type = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)  # Consider using DateTimeField if the format is consistent
    source_info = models.OneToOneField(SourceInfo, on_delete=models.CASCADE)
    content_analysis = models.OneToOneField(ContentAnalysis, on_delete=models.CASCADE)
    ai_analysis = models.OneToOneField(AIDetection, on_delete=models.CASCADE)
    additional_metadata = models.OneToOneField(AdditionalMetadata, on_delete=models.CASCADE)
