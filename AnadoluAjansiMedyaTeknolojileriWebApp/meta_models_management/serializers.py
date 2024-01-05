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

    def create(self, validated_data):
        source_info_data = validated_data.pop('source_info')
        source_location_data = source_info_data.pop('location')
        content_analysis_data = validated_data.pop('content_analysis')
        ai_analysis_data = validated_data.pop('ai_analysis')
        additional_metadata_data = validated_data.pop('additional_metadata')

        # Handling SourceInfo and SourceLocation
        location = SourceLocation.objects.create(**source_location_data)
        source_info = SourceInfo.objects.create(location=location, **source_info_data)

        # Handling ContentAnalysis and nested Keywords
        keywords_data = content_analysis_data.pop('keywords')
        content_analysis = ContentAnalysis.objects.create(**content_analysis_data)
        # Now, create Keyword instances and add them to the ContentAnalysis
        for keyword_data in keywords_data:
            try:
                keyword_instance, created = Keyword.objects.get_or_create(**keyword_data)
                content_analysis.keywords.add(keyword_instance)
            except Keyword.MultipleObjectsReturned:
                # Handle the exception if multiple Keyword entries are found
                keyword_instances = Keyword.objects.filter(**keyword_data)
                for instance in keyword_instances:
                    content_analysis.keywords.add(instance)

        # Handling AIDetection and nested details
        emotion_analysis_data = ai_analysis_data.pop('emotion_analysis')
        object_detection_data = ai_analysis_data.pop('object_detection')
        text_extraction_data = ai_analysis_data.pop('text_extraction')

        associated_emotions_data = emotion_analysis_data.pop('associated_emotions')
        emotion_analysis = EmotionAnalysis.objects.create(**emotion_analysis_data)

        # After creating EmotionAnalysis, create AssociatedEmotion instances
        # Then, add them to the EmotionAnalysis using .set()
        associated_emotions_instances = []
        for associated_emotion_data in associated_emotions_data:
            try:
                # Try to get or create the AssociatedEmotion instance
                associated_emotion, created = AssociatedEmotion.objects.get_or_create(**associated_emotion_data)
                associated_emotions_instances.append(associated_emotion)
            except AssociatedEmotion.MultipleObjectsReturned:
                # Handle the case where multiple objects are returned.
                # You might want to log this issue, merge entries, or pick the first one.
                associated_emotions = AssociatedEmotion.objects.filter(**associated_emotion_data)
                if associated_emotions.exists():
                    # For simplicity, we're just taking the first one here.
                    associated_emotion = associated_emotions.first()
                    associated_emotions_instances.append(associated_emotion)


        # Use .set() to assign the associated emotions to the emotion_analysis instance
        emotion_analysis.associated_emotions.set(associated_emotions_instances)

        # Continue creating AIDetection and related instances
        ai_detection = AIDetection.objects.create(emotion_analysis=emotion_analysis, **ai_analysis_data)
        # Handling Object Detection Data
        for object_data in object_detection_data:
            try:
                object_instance, created = Object.objects.get_or_create(**object_data)
                ai_detection.object_detection.add(object_instance)
            except Object.MultipleObjectsReturned:
                # Handle the case where multiple objects are returned
                object_instances = Object.objects.filter(**object_data)
                if object_instances.exists():
                    # For simplicity, taking the first one here
                    object_instance = object_instances.first()
                    ai_detection.object_detection.add(object_instance)

        # Handling Text Extraction Data
        for text_data in text_extraction_data:
            try:
                text_instance, created = TextExtraction.objects.get_or_create(**text_data)
                ai_detection.text_extraction.add(text_instance)
            except TextExtraction.MultipleObjectsReturned:
                # Handle the case where multiple objects are returned
                text_instances = TextExtraction.objects.filter(**text_data)
                if text_instances.exists():
                    # For simplicity, taking the first one here
                    text_instance = text_instances.first()
                    ai_detection.text_extraction.add(text_instance)


        additional_metadata = AdditionalMetadata.objects.create()

        # Define a dictionary for mapping the field name to its corresponding model and serializer
        field_model_serializer_mapping = {
            'source_attributes': (SourceAttribute, SourceAttributeSerializer),
            'content_themes': (ContentTheme, ContentThemeSerializer),
            'audience': (Audience, AudienceSerializer),
            'geographic_relevance': (GeographicRelevance, GeographicRelevanceSerializer),
            'temporal_relevance': (TemporalRelevance, TemporalRelevanceSerializer),
            'technical_level': (TechnicalLevel, TechnicalLevelSerializer),
            'sentiment_trends': (SentimentTrend, SentimentTrendSerializer),
            'influencer_tags': (InfluencerTag, InfluencerTagSerializer)
        }

        # Iterate through each ManyToMany field in AdditionalMetadata
        for field_name, (ModelClass, SerializerClass) in field_model_serializer_mapping.items():
            detail_list = additional_metadata_data.get(field_name, [])
            instances = []
            for item_data in detail_list:
                try:
                    instance, created = ModelClass.objects.get_or_create(**item_data)
                    instances.append(instance)
                except ModelClass.MultipleObjectsReturned:
                    # Handle the exception if multiple entries are found
                    instance_list = ModelClass.objects.filter(**item_data)
                    instances.extend(instance_list)
            getattr(additional_metadata, field_name).set(instances)

        # Finally creating the InputRecord
        input_record = InputRecord.objects.create(
            source_info=source_info,
            content_analysis=content_analysis,
            ai_analysis=ai_detection,
            additional_metadata=additional_metadata,
            **validated_data
        )

        return input_record