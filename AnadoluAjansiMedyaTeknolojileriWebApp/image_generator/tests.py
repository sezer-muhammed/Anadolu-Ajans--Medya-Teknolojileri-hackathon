from django.test import TestCase
from .models import ImageGeneration, Keyword, Subcategory, ObjectDetail, Character, NewsContext, VisualElements, StylePreferences, UserCustomizations
from .views import ImageGenerationViewSet
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

class ImageGenerationTestCase(TestCase):
    def setUp(self):
      # Create a user
      self.user = User.objects.create_user(username='testuser', password='12345')

      # Create instances of your models here
      self.keyword = Keyword.objects.create(word='test')  # Create a Keyword instance with the word 'test'
      self.subcategory = Subcategory.objects.create(name='test')  # Create a Subcategory instance with the name 'test'
      self.object_detail = ObjectDetail.objects.create(description='test')  # Create an ObjectDetail instance with the description 'test'
      self.character = Character.objects.create(type='test', action='test')  # Create a Character instance with the type 'test' and action 'test'
      self.news_context = NewsContext.objects.create(
        headline='test',  # Create a NewsContext instance with the headline 'test'
        category='test',  # Set the category of the NewsContext instance to 'test'
        emotionTone='test',  # Set the emotionTone of the NewsContext instance to 'test'
        emotionalIntensity=3,  # Set the emotionalIntensity of the NewsContext instance to 3
        geographicalContext='test',  # Set the geographicalContext of the NewsContext instance to 'test'
        temporalContext='test',  # Set the temporalContext of the NewsContext instance to 'test'
        sourceCredibility=3,  # Set the sourceCredibility of the NewsContext instance to 3
        audienceAgeGroup='test'  # Set the audienceAgeGroup of the NewsContext instance to 'test'
      )
      self.visual_elements = VisualElements.objects.create(
        mainSubject='test',  # Create a VisualElements instance with the mainSubject 'test'
        backgroundScene='test',  # Set the backgroundScene of the VisualElements instance to 'test'
        colorPalette='test',  # Set the colorPalette of the VisualElements instance to 'test'
        texture='test'  # Set the texture of the VisualElements instance to 'test'
      )
      self.style_preferences = StylePreferences.objects.create(
        artStyle='test',  # Create a StylePreferences instance with the artStyle 'test'
        composition='test',  # Set the composition of the StylePreferences instance to 'test'
        lighting='test',  # Set the lighting of the StylePreferences instance to 'test'
        aspectRatio='test'  # Set the aspectRatio of the StylePreferences instance to 'test'
      )
      self.user_customizations = UserCustomizations.objects.create(additionalText='test')  # Create a UserCustomizations instance with the additionalText 'test'
      self.image_generation = ImageGeneration.objects.create(
        news_context=self.news_context,  # Set the news_context of the ImageGeneration instance to the created NewsContext instance
        visual_elements=self.visual_elements,  # Set the visual_elements of the ImageGeneration instance to the created VisualElements instance
        style_preferences=self.style_preferences,  # Set the style_preferences of the ImageGeneration instance to the created StylePreferences instance
        user_customizations=self.user_customizations  # Set the user_customizations of the ImageGeneration instance to the created UserCustomizations instance
      )


    def test_setup_successful(self):
            # Check if the user is created successfully
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(self.user.username, 'testuser')
            self.assertEqual(self.user.check_password('12345'), True)

            # Check if the models are created successfully
            self.assertEqual(Keyword.objects.count(), 1)

            self.assertEqual(Subcategory.objects.count(), 1)

            self.assertEqual(ObjectDetail.objects.count(), 1)

            self.assertEqual(Character.objects.count(), 1)

            self.assertEqual(NewsContext.objects.count(), 1)

            self.assertEqual(VisualElements.objects.count(), 1)

            self.assertEqual(StylePreferences.objects.count(), 1)

            self.assertEqual(UserCustomizations.objects.count(), 1)

            self.assertEqual(ImageGeneration.objects.count(), 1)