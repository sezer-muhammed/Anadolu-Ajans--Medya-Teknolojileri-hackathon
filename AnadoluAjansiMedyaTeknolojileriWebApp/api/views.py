from rest_framework import viewsets

from .models import ImageUpload, TextUpload, VoiceUpload
from .serializers import ImageUploadSerializer, TextUploadSerializer, VoiceUploadSerializer

from meta_models_management.models import InputRecord
from meta_models_management.serializers import InputRecordSerializer

class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

class TextUploadViewSet(viewsets.ModelViewSet):
    queryset = TextUpload.objects.all()
    serializer_class = TextUploadSerializer

class VoiceUploadViewSet(viewsets.ModelViewSet):
    queryset = VoiceUpload.objects.all()
    serializer_class = VoiceUploadSerializer

class InputRecordViewSet(viewsets.ModelViewSet):
    queryset = InputRecord.objects.all()
    serializer_class = InputRecordSerializer