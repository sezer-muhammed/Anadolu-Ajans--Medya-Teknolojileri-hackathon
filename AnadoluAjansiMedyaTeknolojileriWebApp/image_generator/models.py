from django.db import models
from api.models import ImageUpload, TextUpload
import random

class GeneratedImages(models.Model):
    image = models.ImageField(upload_to='generated_images/')
    image_generation = models.ForeignKey("ImageGeneration", on_delete=models.SET_NULL, null=True, blank=True, related_name='generated_images')
    def __str__(self):
        return f"Generated Image {self.id}"

# Shared Elements Models
class Keyword(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word

class Subcategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ObjectDetail(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

class Character(models.Model):
    type = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    appearance = models.TextField()

    def __str__(self):
        return f"{self.type} - {self.action}"

# News Context Model
class NewsContext(models.Model):
    headline = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    emotionTone = models.CharField(max_length=50)
    emotionalIntensity = models.IntegerField()
    geographicalContext = models.CharField(max_length=100)
    temporalContext = models.CharField(max_length=100)
    sourceCredibility = models.IntegerField()
    audienceAgeGroup = models.CharField(max_length=50)
    audienceInterests = models.TextField()
    keywords = models.ManyToManyField(Keyword)
    subcategories = models.ManyToManyField(Subcategory)

    def __str__(self):
        return self.headline

# Visual Elements Model
class VisualElements(models.Model):
    mainSubject = models.CharField(max_length=255)
    backgroundScene = models.CharField(max_length=100)
    colorPalette = models.CharField(max_length=100)
    texture = models.CharField(max_length=100)
    dynamicElements = models.TextField()
    textOverlayStyle = models.TextField()
    motionEffects = models.TextField()
    characters = models.ManyToManyField(Character)
    object_details = models.ManyToManyField(ObjectDetail)

    def __str__(self):
        return self.mainSubject

# Style Preferences Model
class StylePreferences(models.Model):
    artStyle = models.CharField(max_length=100)
    composition = models.CharField(max_length=100)
    lighting = models.CharField(max_length=100)
    aspectRatio = models.CharField(max_length=50)

    def __str__(self):
        return self.artStyle

class UserCustomizations(models.Model):
    additionalText = models.TextField(blank=True)
    userUploads = models.TextField(blank=True)
    specificRequests = models.TextField(blank=True)
    feedbackLoop = models.TextField(blank=True)
    templates = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.additionalText = self.additionalText if self.additionalText.strip() else "Not Available"
        self.userUploads = self.userUploads if self.userUploads.strip() else "Not Available"
        self.specificRequests = self.specificRequests if self.specificRequests.strip() else "Not Available"
        self.feedbackLoop = self.feedbackLoop if self.feedbackLoop.strip() else "Not Available"
        self.templates = self.templates if self.templates.strip() else "Not Available"

        super(UserCustomizations, self).save(*args, **kwargs)

    def __str__(self):
        return self.additionalText


# Main Image Generation Model
class ImageGeneration(models.Model):
    news_context = models.OneToOneField(NewsContext, on_delete=models.CASCADE)
    visual_elements = models.OneToOneField(VisualElements, on_delete=models.CASCADE)
    style_preferences = models.OneToOneField(StylePreferences, on_delete=models.CASCADE)
    user_customizations = models.OneToOneField(UserCustomizations, on_delete=models.CASCADE)


    # Adding the optional one-to-one fields
    image_upload = models.OneToOneField(ImageUpload, on_delete=models.SET_NULL, null=True, blank=True)
    text_upload = models.OneToOneField(TextUpload, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Image Generation for {self.news_context.headline}"
    
    @property
    def random_image_url(self):
        if self.image_upload and self.image_upload.image:
            return self.image_upload.image.url
        else:
            images = self.generated_images.all()
            if images:
                return random.choice(images).image.url
        return None  # or a default image URL
