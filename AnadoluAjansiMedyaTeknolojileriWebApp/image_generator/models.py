from django.db import models

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

# User Customizations Model
class UserCustomizations(models.Model):
    additionalText = models.TextField()
    userUploads = models.TextField()
    specificRequests = models.TextField()
    feedbackLoop = models.TextField()
    templates = models.TextField()

    def __str__(self):
        return self.additionalText

# Main Image Generation Model
class ImageGeneration(models.Model):
    news_context = models.OneToOneField(NewsContext, on_delete=models.CASCADE)
    visual_elements = models.OneToOneField(VisualElements, on_delete=models.CASCADE)
    style_preferences = models.OneToOneField(StylePreferences, on_delete=models.CASCADE)
    user_customizations = models.OneToOneField(UserCustomizations, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image Generation for {self.news_context.headline}"
