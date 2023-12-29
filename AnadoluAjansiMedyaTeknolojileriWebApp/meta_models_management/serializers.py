from rest_framework import serializers
from .models import (InputRecord, SourceInfo, SourceLocation, ContentAnalysis, Keyword, EmotionAnalysis,
                     AssociatedEmotion, Object, TextExtraction, AIDetection, AdditionalMetadata,
                     SourceAttribute, ContentTheme, Audience, GeographicRelevance, TemporalRelevance,
                     TechnicalLevel, SentimentTrend, InfluencerTag)

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('value',)

class AssociatedEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociatedEmotion
        fields = ('emotion',)

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('name', 'status', 'action')

class TextExtractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextExtraction
        fields = ('text',)

class SourceAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceAttribute
        fields = ('attribute',)

class ContentThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTheme
        fields = ('theme',)

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ('audience_type',)

class GeographicRelevanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicRelevance
        fields = ('geography',)

class TemporalRelevanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporalRelevance
        fields = ('temporal',)

class TechnicalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalLevel
        fields = ('level',)

class SentimentTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentTrend
        fields = ('trend',)

class InfluencerTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerTag
        fields = ('tag',)

class SourceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceLocation
        fields = ('latitude', 'longitude')

class SourceInfoSerializer(serializers.ModelSerializer):
    location = SourceLocationSerializer()

    class Meta:
        model = SourceInfo
        fields = ('source', 'city', 'country', 'location')

class ContentAnalysisSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = ContentAnalysis
        fields = ('detailed_description', 'summary', 'keywords')

class EmotionAnalysisSerializer(serializers.ModelSerializer):
    associated_emotions = AssociatedEmotionSerializer(many=True)

    class Meta:
        model = EmotionAnalysis
        fields = ('associated_emotions',)

class AIDetectionSerializer(serializers.ModelSerializer):
    emotion_analysis = EmotionAnalysisSerializer()
    object_detection = ObjectSerializer(many=True)
    text_extraction = TextExtractionSerializer(many=True)

    class Meta:
        model = AIDetection
        fields = ('emotion_analysis', 'object_detection', 'text_extraction')

class AdditionalMetadataSerializer(serializers.ModelSerializer):
    source_attributes = SourceAttributeSerializer(many=True)
    content_themes = ContentThemeSerializer(many=True)
    audience = AudienceSerializer(many=True)
    geographic_relevance = GeographicRelevanceSerializer(many=True)
    temporal_relevance = TemporalRelevanceSerializer(many=True)
    technical_level = TechnicalLevelSerializer(many=True)
    sentiment_trends = SentimentTrendSerializer(many=True)
    influencer_tags = InfluencerTagSerializer(many=True)

    class Meta:
        model = AdditionalMetadata
        fields = ('source_attributes', 'content_themes', 'audience', 'geographic_relevance', 'temporal_relevance',
                  'technical_level', 'sentiment_trends', 'influencer_tags')

class InputRecordSerializer(serializers.ModelSerializer):
    source_info = SourceInfoSerializer()
    content_analysis = ContentAnalysisSerializer()
    ai_analysis = AIDetectionSerializer()
    additional_metadata = AdditionalMetadataSerializer()

    class Meta:
        model = InputRecord
        fields = ('input_id', 'input_type', 'timestamp', 'source_info', 'content_analysis',
                  'ai_analysis', 'additional_metadata')
