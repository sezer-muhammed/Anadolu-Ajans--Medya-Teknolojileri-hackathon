from rest_framework import viewsets

from .models import ImageUpload, TextUpload, VoiceUpload
from .serializers import (
    ImageUploadSerializer,
    TextUploadSerializer,
    VoiceUploadSerializer,
)

class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer


class TextUploadViewSet(viewsets.ModelViewSet):
    queryset = TextUpload.objects.all()
    serializer_class = TextUploadSerializer


class VoiceUploadViewSet(viewsets.ModelViewSet):
    queryset = VoiceUpload.objects.all()
    serializer_class = VoiceUploadSerializer


