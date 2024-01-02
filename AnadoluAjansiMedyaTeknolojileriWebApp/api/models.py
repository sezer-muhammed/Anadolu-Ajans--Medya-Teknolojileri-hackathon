from django.db import models
from .validators import validate_file_extension

def my_callback(instance):
    # Your callback logic here
    pass

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        my_callback(self)

class TextUpload(models.Model):
    text = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        my_callback(self)

class VoiceUpload(models.Model):
    voice_file = models.FileField(upload_to='voices/', validators=[validate_file_extension])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        my_callback(self)
