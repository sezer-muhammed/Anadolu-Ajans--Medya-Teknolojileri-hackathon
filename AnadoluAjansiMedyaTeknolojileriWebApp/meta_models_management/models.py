from django.db import models

# Models for each list of strings
class Keyword(models.Model):
    value = models.CharField(max_length=200)
    
    def __str__(self):
        return self.value

class AssociatedEmotion(models.Model):
    emotion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.emotion

class Object(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    action = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.status}"

class TextExtraction(models.Model):
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.text[:50]}..."  # Show first 50 characters

class SourceAttribute(models.Model):
    attribute = models.CharField(max_length=200)

    def __str__(self):
        return self.attribute

class ContentTheme(models.Model):
    theme = models.CharField(max_length=200)

    def __str__(self):
        return self.theme

class Audience(models.Model):
    audience_type = models.CharField(max_length=200)

    def __str__(self):
        return self.audience_type

class GeographicRelevance(models.Model):
    geography = models.CharField(max_length=200)

    def __str__(self):
        return self.geography

class TemporalRelevance(models.Model):
    temporal = models.CharField(max_length=200)

    def __str__(self):
        return self.temporal

class TechnicalLevel(models.Model):
    level = models.CharField(max_length=200)

    def __str__(self):
        return self.level

class SentimentTrend(models.Model):
    trend = models.CharField(max_length=200)

    def __str__(self):
        return self.trend

class InfluencerTag(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag

# Main models
class SourceLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class SourceInfo(models.Model):
    source = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    location = models.OneToOneField(SourceLocation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source} in {self.city}, {self.country}"

class ContentAnalysis(models.Model):
    detailed_description = models.TextField()
    summary = models.TextField()
    keywords = models.ManyToManyField(Keyword, related_name='content_analysis_keywords')

    def __str__(self):
        return f"{self.summary[:50]}..."

class EmotionAnalysis(models.Model):
    associated_emotions = models.ManyToManyField(AssociatedEmotion, related_name='emotion_analysis_emotions')

    def __str__(self) -> str:
        return f"{self.associated_emotions.all()}"

class AIDetection(models.Model):
    emotion_analysis = models.OneToOneField(EmotionAnalysis, on_delete=models.CASCADE)
    object_detection = models.ManyToManyField(Object, related_name='ai_detection_objects')
    text_extraction = models.ManyToManyField(TextExtraction, related_name='ai_detection_texts')

    def __str__(self):
        return f"{self.emotion_analysis} - {self.object_detection.all()} - {self.text_extraction.all()}"

class AdditionalMetadata(models.Model):

    source_attributes = models.ManyToManyField(SourceAttribute, related_name='additional_metadata_source_attributes', blank=True)
    content_themes = models.ManyToManyField(ContentTheme, related_name='additional_metadata_content_themes', blank=True)
    audience = models.ManyToManyField(Audience, related_name='additional_metadata_audience', blank=True)
    geographic_relevance = models.ManyToManyField(GeographicRelevance, related_name='additional_metadata_geographic_relevance', blank=True)
    temporal_relevance = models.ManyToManyField(TemporalRelevance, related_name='additional_metadata_temporal_relevance', blank=True)
    technical_level = models.ManyToManyField(TechnicalLevel, related_name='additional_metadata_technical_level', blank=True)
    sentiment_trends = models.ManyToManyField(SentimentTrend, related_name='additional_metadata_sentiment_trends', blank=True)
    influencer_tags = models.ManyToManyField(InfluencerTag, related_name='additional_metadata_influencer_tags', blank=True)

    def __str__(self):
        return f"{self.source_attributes.all()} - {self.content_themes.all()} - {self.audience.all()} - {self.geographic_relevance.all()} - {self.temporal_relevance.all()} - {self.technical_level.all()} - {self.sentiment_trends.all()} - {self.influencer_tags.all()}"

class InputRecord(models.Model):

    input_id = models.CharField(max_length=400)
    input_type = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)  # Consider using DateTimeField if the format is consistent
    source_info = models.OneToOneField(SourceInfo, on_delete=models.CASCADE)
    content_analysis = models.OneToOneField(ContentAnalysis, on_delete=models.CASCADE)
    ai_analysis = models.OneToOneField(AIDetection, on_delete=models.CASCADE)
    additional_metadata = models.OneToOneField(AdditionalMetadata, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.input_id} - {self.input_type} - {self.timestamp} - {self.source_info} - {self.content_analysis} - {self.ai_analysis} - {self.additional_metadata}"
