from django.db import models
from .validators import validate_file_extension

from meta_models_management.callbacks.BaseMediaUpload import InputRecordGenerator

class UploadedFileHandler:
    def __init__(self):
        # Initialize any necessary attributes or configurations
        self.generator = InputRecordGenerator()
        
    def uploaded_file_callback(self, instance):
        """
        Handles the callback for an uploaded file.

        Parameters:
        instance: The instance of the file or data that was uploaded.
        """
        # Use the uploaded_file_analyse_callback method from the generator instance
        self.generator.uploaded_file_analyse_callback(instance)

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # If you want to handle image uploads, uncomment the following lines
        # handler = UploadedFileHandler()
        # handler.uploaded_file_callback(self)

class TextUpload(models.Model):
    text = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Handle text uploads
        handler = UploadedFileHandler()
        handler.uploaded_file_callback(self)

class VoiceUpload(models.Model):
    voice_file = models.FileField(upload_to='voices/', validators=[validate_file_extension])
    transcript = models.TextField(blank=True)  # Add a field for the transcript

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # If you want to handle voice uploads, uncomment the following lines
        # handler = UploadedFileHandler()
        # handler.uploaded_file_callback(self)