from django.contrib import admin
from .models import (Keyword, AssociatedEmotion, Object, TextExtraction, SourceAttribute,
                     ContentTheme, Audience, GeographicRelevance, TemporalRelevance,
                     TechnicalLevel, SentimentTrend, InfluencerTag, SourceLocation,
                     SourceInfo, ContentAnalysis, EmotionAnalysis, AIDetection,
                     AdditionalMetadata, InputRecord)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('value',)
    search_fields = ('value',)

admin.site.register(Keyword, KeywordAdmin)

class AssociatedEmotionAdmin(admin.ModelAdmin):
    list_display = ('emotion',)
    search_fields = ('emotion',)

admin.site.register(AssociatedEmotion, AssociatedEmotionAdmin)

class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'action')
    search_fields = ('name', 'status', 'action')
    list_filter = ('status',)

admin.site.register(Object, ObjectAdmin)

class TextExtractionAdmin(admin.ModelAdmin):
    list_display = ('text_excerpt',)
    search_fields = ('text',)

    def text_excerpt(self, obj):
        """Returns a shorter excerpt of the text for the admin list display."""
        return obj.__str__()
    text_excerpt.short_description = 'Excerpt'

admin.site.register(TextExtraction, TextExtractionAdmin)

class SourceAttributeAdmin(admin.ModelAdmin):
    list_display = ('attribute',)
    search_fields = ('attribute',)

admin.site.register(SourceAttribute, SourceAttributeAdmin)

class ContentThemeAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    search_fields = ('theme',)

admin.site.register(ContentTheme, ContentThemeAdmin)

class AudienceAdmin(admin.ModelAdmin):
    list_display = ('audience_type',)
    search_fields = ('audience_type',)

admin.site.register(Audience, AudienceAdmin)

class GeographicRelevanceAdmin(admin.ModelAdmin):
    list_display = ('geography',)
    search_fields = ('geography',)

admin.site.register(GeographicRelevance, GeographicRelevanceAdmin)

class TemporalRelevanceAdmin(admin.ModelAdmin):
    list_display = ('temporal',)
    search_fields = ('temporal',)

admin.site.register(TemporalRelevance, TemporalRelevanceAdmin)

class TechnicalLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    search_fields = ('level',)

admin.site.register(TechnicalLevel, TechnicalLevelAdmin)

class SentimentTrendAdmin(admin.ModelAdmin):
    list_display = ('trend',)
    search_fields = ('trend',)

admin.site.register(SentimentTrend, SentimentTrendAdmin)

class InfluencerTagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    search_fields = ('tag',)

admin.site.register(InfluencerTag, InfluencerTagAdmin)

class SourceLocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude',)
    search_fields = ('latitude', 'longitude',)

admin.site.register(SourceLocation, SourceLocationAdmin)

class SourceInfoAdmin(admin.ModelAdmin):
    list_display = ('source', 'city', 'country', 'location')
    search_fields = ('source', 'city', 'country')
    raw_id_fields = ('location',)

admin.site.register(SourceInfo, SourceInfoAdmin)

class ContentAnalysisAdmin(admin.ModelAdmin):
    list_display = ('summary_short',)
    search_fields = ('summary', 'detailed_description',)
    filter_horizontal = ('keywords',)

    def summary_short(self, obj):
        return obj.summary[:50] + "..."
    summary_short.short_description = 'Summary Excerpt'

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ContentAnalysisAdmin, self).get_search_results(request, queryset, search_term)
        if search_term:
            queryset |= self.model.objects.filter(keywords__value__icontains=search_term)
        return queryset, use_distinct

admin.site.register(ContentAnalysis, ContentAnalysisAdmin)


class EmotionAnalysisAdmin(admin.ModelAdmin):
    list_display = ('emotions_short',)
    filter_horizontal = ('associated_emotions',)

    def emotions_short(self, obj):
        emotions = ", ".join([emotion.emotion for emotion in obj.associated_emotions.all()[:3]])
        return f"{emotions}..." if obj.associated_emotions.count() > 3 else emotions
    emotions_short.short_description = 'Associated Emotions (Preview)'

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(EmotionAnalysisAdmin, self).get_search_results(request, queryset, search_term)
        if search_term:
            queryset |= self.model.objects.filter(associated_emotions__emotion__icontains=search_term)
        return queryset, use_distinct

admin.site.register(EmotionAnalysis, EmotionAnalysisAdmin)

class AIDetectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'emotion_analysis_preview',)
    filter_horizontal = ('object_detection', 'text_extraction',)
    raw_id_fields = ('emotion_analysis',)

    def emotion_analysis_preview(self, obj):
        return str(obj.emotion_analysis)
    emotion_analysis_preview.short_description = 'Emotion Analysis'

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(AIDetectionAdmin, self).get_search_results(request, queryset, search_term)
        if search_term:
            queryset |= self.model.objects.filter(
                emotion_analysis__associated_emotions__emotion__icontains=search_term
            ) | self.model.objects.filter(
                object_detection__name__icontains=search_term
            ) | self.model.objects.filter(
                text_extraction__text__icontains=search_term
            )
        return queryset, use_distinct

admin.site.register(AIDetection, AIDetectionAdmin)

class AdditionalMetadataAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('source_attributes', 'content_themes', 'audience', 'geographic_relevance', 'temporal_relevance', 'technical_level', 'sentiment_trends', 'influencer_tags',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(AdditionalMetadataAdmin, self).get_search_results(request, queryset, search_term)
        if search_term:
            queryset |= self.model.objects.filter(
                source_attributes__attribute__icontains=search_term
            ) | self.model.objects.filter(
                content_themes__theme__icontains=search_term
            ) | self.model.objects.filter(
                audience__audience_type__icontains=search_term
            ) | self.model.objects.filter(
                geographic_relevance__geography__icontains=search_term
            ) | self.model.objects.filter(
                temporal_relevance__temporal__icontains=search_term
            ) | self.model.objects.filter(
                technical_level__level__icontains=search_term
            ) | self.model.objects.filter(
                sentiment_trends__trend__icontains=search_term
            ) | self.model.objects.filter(
                influencer_tags__tag__icontains=search_term
            )
        return queryset, use_distinct

admin.site.register(AdditionalMetadata, AdditionalMetadataAdmin)


class InputRecordAdmin(admin.ModelAdmin):
    list_display = ('input_id', 'input_type', 'timestamp', 'source_info', 'content_analysis', 'ai_analysis', 'additional_metadata',)
    search_fields = ('input_id', 'input_type', 'timestamp',)
    raw_id_fields = ('source_info', 'content_analysis', 'ai_analysis', 'additional_metadata',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(InputRecordAdmin, self).get_search_results(request, queryset, search_term)
        if search_term:
            queryset |= self.model.objects.filter(
                source_info__source__icontains=search_term
            ) | self.model.objects.filter(
                content_analysis__summary__icontains=search_term
            ) | self.model.objects.filter(
                ai_analysis__emotion_analysis__associated_emotions__emotion__icontains=search_term
            ) | self.model.objects.filter(
                additional_metadata__source_attributes__attribute__icontains=search_term
            )
        return queryset, use_distinct

admin.site.register(InputRecord, InputRecordAdmin)
