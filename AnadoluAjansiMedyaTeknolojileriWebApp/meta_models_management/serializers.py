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
        
"""
    def create(self, validated_data):
        # Extract and remove the nested data from validated_data
        source_info_data = validated_data.pop('source_info')
        content_analysis_data = validated_data.pop('content_analysis')
        ai_analysis_data = validated_data.pop('ai_analysis')
        additional_metadata_data = validated_data.pop('additional_metadata')
        
        # Create SourceLocation instance
        location_data = source_info_data.pop('location')
        location = SourceLocation.objects.create(**location_data)

        # Create SourceInfo instance
        source_info = SourceInfo.objects.create(location=location, **source_info_data)

        # Create EmotionAnalysis instance
        emotion_analysis_data = ai_analysis_data.pop('emotion_analysis')
        emotion_analysis = EmotionAnalysis.objects.create(**emotion_analysis_data)

        # Create AIDetection instance
        ai_detection = AIDetection.objects.create(emotion_analysis=emotion_analysis, **ai_analysis_data)

        # Create AdditionalMetadata instance
        additional_metadata = AdditionalMetadata.objects.create(**additional_metadata_data)

        content_analysis_data['detailed_description'] = "test"
        content_analysis_data['summary'] = "test"
        content_analysis = ContentAnalysis.objects.create(**content_analysis_data)
        # Handle many-to-many fields for content_analysis (Keywords)
        keywords_data = content_analysis_data.pop('keywords', [])
        keyword_instances = [Keyword.objects.create(**kw_data) for kw_data in keywords_data]
        content_analysis.keywords.set(keyword_instances)

        # Handle many-to-many fields for ai_analysis (AssociatedEmotions)
        emotions_data = ai_analysis_data.get('emotion_analysis', {}).pop('associated_emotions', [])
        emotion_instances = [AssociatedEmotion.objects.create(**emo_data) for emo_data in emotions_data]
        ai_detection.emotion_analysis.associated_emotions.set(emotion_instances)

        # Handle many-to-many fields for ai_analysis (Object Detection)
        objects_data = ai_analysis_data.pop('object_detection', [])
        object_instances = [Object.objects.create(**obj_data) for obj_data in objects_data]
        ai_detection.object_detection.set(object_instances)

        # Handle many-to-many fields for ai_analysis (Text Extraction)
        texts_data = ai_analysis_data.pop('text_extraction', [])
        text_instances = [TextExtraction.objects.create(**text_data) for text_data in texts_data]
        ai_detection.text_extraction.set(text_instances)

        # Source Attributes
        source_attrs = [SourceAttribute.objects.create(**attr_data) for attr_data in additional_metadata_data.pop('source_attributes', [])]
        additional_metadata.source_attributes.set(source_attrs)

        # Content Themes
        content_themes = [ContentTheme.objects.create(**theme_data) for theme_data in additional_metadata_data.pop('content_themes', [])]
        additional_metadata.content_themes.set(content_themes)

        # Audience
        audiences = [Audience.objects.create(**audience_data) for audience_data in additional_metadata_data.pop('audience', [])]
        additional_metadata.audience.set(audiences)

        # Geographic Relevance
        geographics = [GeographicRelevance.objects.create(**geo_data) for geo_data in additional_metadata_data.pop('geographic_relevance', [])]
        additional_metadata.geographic_relevance.set(geographics)

        # Temporal Relevance
        temporals = [TemporalRelevance.objects.create(**temporal_data) for temporal_data in additional_metadata_data.pop('temporal_relevance', [])]
        additional_metadata.temporal_relevance.set(temporals)

        # Technical Level
        technical_levels = [TechnicalLevel.objects.create(**tech_level_data) for tech_level_data in additional_metadata_data.pop('technical_level', [])]
        additional_metadata.technical_level.set(technical_levels)

        # Sentiment Trends
        sentiments = [SentimentTrend.objects.create(**sentiment_data) for sentiment_data in additional_metadata_data.pop('sentiment_trends', [])]
        additional_metadata.sentiment_trends.set(sentiments)

        # Influencer Tags
        tags = [InfluencerTag.objects.create(**tag_data) for tag_data in additional_metadata_data.pop('influencer_tags', [])]
        additional_metadata.influencer_tags.set(tags)

        # Create the main InputRecord instance without many-to-many fields
        input_record = InputRecord.objects.create(
            source_info=source_info,
            content_analysis=content_analysis,
            ai_analysis=ai_detection,
            additional_metadata=additional_metadata,
            **validated_data
        )

        return input_record
"""