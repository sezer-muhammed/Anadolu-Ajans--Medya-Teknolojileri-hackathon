from django.db import models
from .validators import validate_file_extension
from django.utils import timezone
from .callbacks import ImageCallback, TextCallback


class ImageUpload(models.Model):
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ImageCallback.process_image(self)  # Pass the whole object

class TextUpload(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        TextCallback.process_text(self)  # Pass the whole object

class VoiceUpload(models.Model):
    voice_file = models.FileField(
        upload_to="voices/", validators=[validate_file_extension]
    )
    transcript = models.TextField(blank=True)  # Add a field for the transcript
