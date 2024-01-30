from django.contrib import admin
from .models import Keyword, Subcategory, ObjectDetail, Character, NewsContext, VisualElements, StylePreferences, UserCustomizations, ImageGeneration

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word')
    search_fields = ('word',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(ObjectDetail)
class ObjectDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    search_fields = ('description',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'action', 'appearance')
    search_fields = ('type', 'action', 'appearance')

@admin.register(NewsContext)
class NewsContextAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'category', 'emotionTone', 'emotionalIntensity', 'geographicalContext', 'temporalContext', 'sourceCredibility', 'audienceAgeGroup', 'audienceInterests')
    list_filter = ('category', 'emotionTone', 'geographicalContext', 'temporalContext')
    search_fields = ('headline', 'category', 'emotionTone', 'geographicalContext', 'temporalContext')
    filter_horizontal = ('keywords', 'subcategories')

@admin.register(VisualElements)
class VisualElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'mainSubject', 'backgroundScene', 'colorPalette', 'texture', 'dynamicElements', 'textOverlayStyle', 'motionEffects')
    list_filter = ('mainSubject', 'backgroundScene', 'colorPalette', 'texture')
    search_fields = ('mainSubject', 'backgroundScene', 'colorPalette', 'texture', 'dynamicElements', 'textOverlayStyle', 'motionEffects')
    filter_horizontal = ('characters', 'object_details')

@admin.register(StylePreferences)
class StylePreferencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'artStyle', 'composition', 'lighting', 'aspectRatio')
    search_fields = ('artStyle', 'composition', 'lighting', 'aspectRatio')

@admin.register(UserCustomizations)
class UserCustomizationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'additionalText', 'userUploads', 'specificRequests', 'feedbackLoop', 'templates')
    search_fields = ('additionalText', 'userUploads', 'specificRequests', 'feedbackLoop', 'templates')

@admin.register(ImageGeneration)
class ImageGenerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_context', 'visual_elements', 'style_preferences', 'user_customizations')
    raw_id_fields = ('news_context', 'visual_elements', 'style_preferences', 'user_customizations')
    search_fields = ('news_context__headline',)
