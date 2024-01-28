from django.contrib import admin
from .models import Keyword, Subcategory, ObjectDetail, Character, NewsContext, VisualElements, StylePreferences, UserCustomizations, ImageGeneration

# Register your models here.

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word')

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(ObjectDetail)
class ObjectDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'action')

@admin.register(NewsContext)
class NewsContextAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'category', 'emotionTone', 'emotionalIntensity', 'geographicalContext', 'temporalContext', 'sourceCredibility', 'audienceAgeGroup')
    filter_horizontal = ('keywords', 'subcategories')
    list_select_related = ('category', 'emotionTone', 'geographicalContext', 'temporalContext', 'sourceCredibility', 'audienceAgeGroup')

@admin.register(VisualElements)
class VisualElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'mainSubject', 'backgroundScene', 'colorPalette', 'texture')
    filter_horizontal = ('characters', 'object_details')
    list_select_related = ('mainSubject', 'backgroundScene', 'colorPalette', 'texture')

@admin.register(StylePreferences)
class StylePreferencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'artStyle', 'composition', 'lighting', 'aspectRatio')

@admin.register(UserCustomizations)
class UserCustomizationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'additionalText')

@admin.register(ImageGeneration)
class ImageGenerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_context', 'visual_elements', 'style_preferences', 'user_customizations')
    list_select_related = ('news_context', 'visual_elements', 'style_preferences', 'user_customizations')
