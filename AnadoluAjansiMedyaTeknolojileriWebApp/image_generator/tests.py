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
      self.character = Character.objects.create(
          type='test', action='test', appearance='test'
      )

      # Create additional Keyword and Subcategory instances for NewsContext
      self.keyword2 = Keyword.objects.create(word='test2')
      self.subcategory2 = Subcategory.objects.create(name='test2')

      # Update NewsContext instance creation
      self.news_context = NewsContext.objects.create(
          headline='test', 
          category='test', 
          emotionTone='test',
          emotionalIntensity=3,
          geographicalContext='test', 
          temporalContext='test',
          sourceCredibility=3, 
          audienceAgeGroup='test',
          audienceInterests='test'
      )
      self.news_context.keywords.add(self.keyword, self.keyword2)
      self.news_context.subcategories.add(self.subcategory, self.subcategory2)

      # Update VisualElements instance creation
      self.visual_elements = VisualElements.objects.create(
          mainSubject='test', 
          backgroundScene='test', 
          colorPalette='test', 
          texture='test',
          dynamicElements='test', 
          textOverlayStyle='test', 
          motionEffects='test'
      )
      self.visual_elements.characters.add(self.character)
      self.visual_elements.object_details.add(self.object_detail)

      # Update UserCustomizations instance creation
      self.user_customizations = UserCustomizations.objects.create(
          additionalText='test', 
          userUploads='test', 
          specificRequests='test', 
          feedbackLoop='test', 
          templates='test'
      )     

      self.style_preferences = StylePreferences.objects.create(
          artStyle='test',
          composition='test',
          lighting='test',
          aspectRatio='test'
      )
    
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
        self.assertEqual(Keyword.objects.count(), 2)  # Two keywords are created
        self.assertEqual(Subcategory.objects.count(), 2)  # Two subcategories are created
        self.assertEqual(ObjectDetail.objects.count(), 1)
        self.assertEqual(Character.objects.count(), 2)
        self.assertEqual(NewsContext.objects.count(), 1)
        self.assertEqual(VisualElements.objects.count(), 1)
        self.assertEqual(StylePreferences.objects.count(), 1)
        self.assertEqual(UserCustomizations.objects.count(), 1)
        self.assertEqual(ImageGeneration.objects.count(), 1)

        # Check relationships in NewsContext
        self.assertEqual(self.news_context.keywords.count(), 2)
        self.assertEqual(self.news_context.subcategories.count(), 2)

        # Check relationships in VisualElements
        self.assertEqual(self.visual_elements.characters.count(), 1)
        self.assertEqual(self.visual_elements.object_details.count(), 1)


    def test_image_generation_relationships(self):
        self.assertEqual(self.image_generation.news_context, self.news_context)
        self.assertEqual(self.image_generation.visual_elements, self.visual_elements)
        self.assertEqual(self.image_generation.style_preferences, self.style_preferences)
        self.assertEqual(self.image_generation.user_customizations, self.user_customizations)
