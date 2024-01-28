from rest_framework import serializers
from .models import Keyword, Subcategory, ObjectDetail, Character, NewsContext, VisualElements, StylePreferences, UserCustomizations, ImageGeneration
from django.db import transaction

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'word']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name']

class ObjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectDetail
        fields = ['id', 'description']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'type', 'action', 'appearance']

class NewsContextSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True)
    subcategories = SubcategorySerializer(many=True)

    @transaction.atomic
    def create(self, validated_data):
        keywords_data = validated_data.pop('keywords', [])
        subcategories_data = validated_data.pop('subcategories', [])
        news_context = NewsContext.objects.create(**validated_data)

        for keyword_data in keywords_data:
            keyword = Keyword.objects.filter(word=keyword_data['word']).first()
            if not keyword:
                keyword = Keyword.objects.create(**keyword_data)
            news_context.keywords.add(keyword)

        for subcategory_data in subcategories_data:
            subcategory = Subcategory.objects.filter(name=subcategory_data['name']).first()
            if not subcategory:
                subcategory = Subcategory.objects.create(**subcategory_data)
            news_context.subcategories.add(subcategory)

        return news_context

    class Meta:
        model = NewsContext
        fields = ['id', 'headline', 'category', 'emotionTone', 'emotionalIntensity', 'geographicalContext', 'temporalContext', 'sourceCredibility', 'audienceAgeGroup', 'audienceInterests', 'keywords', 'subcategories']

class VisualElementsSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)
    object_details = ObjectDetailSerializer(many=True)

    @transaction.atomic
    def create(self, validated_data):
        characters_data = validated_data.pop('characters', [])
        object_details_data = validated_data.pop('object_details', [])
        visual_elements = VisualElements.objects.create(**validated_data)

        for character_data in characters_data:
            character = Character.objects.filter(type=character_data['type'], action=character_data['action']).first()
            if not character:
                character = Character.objects.create(**character_data)
            visual_elements.characters.add(character)

        for object_detail_data in object_details_data:
            object_detail = ObjectDetail.objects.filter(description=object_detail_data['description']).first()
            if not object_detail:
                object_detail = ObjectDetail.objects.create(**object_detail_data)
            visual_elements.object_details.add(object_detail)

        return visual_elements

    class Meta:
        model = VisualElements
        fields = ['id', 'mainSubject', 'backgroundScene', 'colorPalette', 'texture', 'dynamicElements', 'textOverlayStyle', 'motionEffects', 'characters', 'object_details']

class StylePreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = StylePreferences
        fields = ['id', 'artStyle', 'composition', 'lighting', 'aspectRatio']

class UserCustomizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomizations
        fields = ['id', 'additionalText', 'userUploads', 'specificRequests', 'feedbackLoop', 'templates']

class ImageGenerationSerializer(serializers.ModelSerializer):
    news_context = NewsContextSerializer()
    visual_elements = VisualElementsSerializer()
    style_preferences = StylePreferencesSerializer()
    user_customizations = UserCustomizationsSerializer()

    def create(self, validated_data):
        news_context_data = validated_data.pop('news_context', {})
        visual_elements_data = validated_data.pop('visual_elements', {})
        style_preferences_data = validated_data.pop('style_preferences', {})
        user_customizations_data = validated_data.pop('user_customizations', {})

        news_context = NewsContextSerializer().create(news_context_data)
        visual_elements = VisualElementsSerializer().create(visual_elements_data)
        style_preferences = StylePreferencesSerializer().create(style_preferences_data)
        user_customizations = UserCustomizationsSerializer().create(user_customizations_data)

        image_generation = ImageGeneration.objects.create(
            news_context=news_context,
            visual_elements=visual_elements,
            style_preferences=style_preferences,
            user_customizations=user_customizations
        )

        return image_generation

    class Meta:
        model = ImageGeneration
        fields = ['id', 'news_context', 'visual_elements', 'style_preferences', 'user_customizations']
