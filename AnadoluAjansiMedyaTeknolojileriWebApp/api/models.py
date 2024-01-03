from django.db import models
from .validators import validate_file_extension

from meta_models_management.callbacks.BaseMediaUpload import uploaded_file_analyse_callback

def uploaded_file_callback(instance):
    uploaded_file_analyse_callback(instance)

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #uploaded_file_callback(self)

class TextUpload(models.Model):
    text = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        uploaded_file_callback(self)

class VoiceUpload(models.Model):
    voice_file = models.FileField(upload_to='voices/', validators=[validate_file_extension])
    transcript = models.TextField(blank=True)  # Add a field for the transcript
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #uploaded_file_callback(self)
