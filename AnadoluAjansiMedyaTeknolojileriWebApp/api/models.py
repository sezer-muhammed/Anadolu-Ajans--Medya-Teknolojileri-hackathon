from django.db import models
from .validators import validate_file_extension
from django.utils import timezone
from .callbacks import ImageCallback, TextCallback
from PIL import Image


class ImageUpload(models.Model):
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize the image
        img = Image.open(self.image.path)
        max_size = 1024
        if img.width > img.height:
            new_width = max_size
            new_height = int((max_size / img.width) * img.height)
        else:
            new_width = int((max_size / img.height) * img.width)
            new_height = max_size
        resized_img = img.resize((new_width, new_height))
        resized_img.save(self.image.path)

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
