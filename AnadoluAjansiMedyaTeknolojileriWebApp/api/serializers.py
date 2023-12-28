from rest_framework import serializers
from .models import ImageUpload, TextUpload, VoiceUpload

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['image']

class TextUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextUpload
        fields = ['text']

class VoiceUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceUpload
        fields = ['voice_file']
