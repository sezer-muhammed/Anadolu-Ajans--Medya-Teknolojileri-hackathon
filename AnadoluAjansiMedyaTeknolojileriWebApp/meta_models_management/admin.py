from django.contrib import admin
from .models import (Keyword, AssociatedEmotion, Object, TextExtraction, SourceAttribute,
                     ContentTheme, Audience, GeographicRelevance, TemporalRelevance,
                     TechnicalLevel, SentimentTrend, InfluencerTag, SourceLocation,
                     SourceInfo, ContentAnalysis, EmotionAnalysis, AIDetection,
                     AdditionalMetadata, InputRecord)

# Simple registration for models with no special display requirements
admin.site.register([Keyword, AssociatedEmotion, Object, TextExtraction, SourceAttribute,
                     ContentTheme, Audience, GeographicRelevance, TemporalRelevance,
                     TechnicalLevel, SentimentTrend, InfluencerTag, SourceLocation])

# Customizing admin for more complex models
class SourceInfoAdmin(admin.ModelAdmin):
    list_display = ('source', 'city', 'country', 'location')  # Customize as needed
    search_fields = ('source', 'city', 'country')

class ContentAnalysisAdmin(admin.ModelAdmin):
    list_display = ('detailed_description', 'summary')  # Customize as needed
    filter_horizontal = ('keywords',)

class EmotionAnalysisAdmin(admin.ModelAdmin):
    filter_horizontal = ('associated_emotions',)

class AIDetectionAdmin(admin.ModelAdmin):
    list_display = ('emotion_analysis',)  # Customize as needed
    filter_horizontal = ('object_detection', 'text_extraction')

class AdditionalMetadataAdmin(admin.ModelAdmin):
    filter_horizontal = ('source_attributes', 'content_themes', 'audience',
                         'geographic_relevance', 'temporal_relevance',
                         'technical_level', 'sentiment_trends', 'influencer_tags')

class InputRecordAdmin(admin.ModelAdmin):
    list_display = ('input_id', 'input_type', 'timestamp', 'source_info',
                    'content_analysis', 'ai_analysis', 'additional_metadata')  # Customize as needed

# Registering models with the custom admin classes
admin.site.register(SourceInfo, SourceInfoAdmin)
admin.site.register(ContentAnalysis, ContentAnalysisAdmin)
admin.site.register(EmotionAnalysis, EmotionAnalysisAdmin)
admin.site.register(AIDetection, AIDetectionAdmin)
admin.site.register(AdditionalMetadata, AdditionalMetadataAdmin)
admin.site.register(InputRecord, InputRecordAdmin)
