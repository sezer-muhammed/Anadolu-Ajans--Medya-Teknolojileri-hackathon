from django.db import models
from .validators import validate_file_extension


class ImageUpload(models.Model):
    image = models.ImageField(upload_to="images/")

class TextUpload(models.Model):
    text = models.TextField()

class VoiceUpload(models.Model):
    voice_file = models.FileField(
        upload_to="voices/", validators=[validate_file_extension]
    )
    transcript = models.TextField(blank=True)  # Add a field for the transcript
