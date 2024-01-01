from django.contrib import admin
from .models import (
    Keyword, AssociatedEmotion, Object, TextExtraction, SourceAttribute,
    ContentTheme, Audience, GeographicRelevance, TemporalRelevance,
    TechnicalLevel, SentimentTrend, InfluencerTag, SourceLocation, SourceInfo,
    ContentAnalysis, EmotionAnalysis, AIDetection, AdditionalMetadata, InputRecord
)

admin.site.register(Keyword)
admin.site.register(AssociatedEmotion)
admin.site.register(Object)
admin.site.register(TextExtraction)
admin.site.register(SourceAttribute)
admin.site.register(ContentTheme)
admin.site.register(Audience)
admin.site.register(GeographicRelevance)
admin.site.register(TemporalRelevance)
admin.site.register(TechnicalLevel)
admin.site.register(SentimentTrend)
admin.site.register(InfluencerTag)
admin.site.register(SourceLocation)
admin.site.register(SourceInfo)
admin.site.register(ContentAnalysis)
admin.site.register(EmotionAnalysis)
admin.site.register(AIDetection)
admin.site.register(AdditionalMetadata)
admin.site.register(InputRecord)
