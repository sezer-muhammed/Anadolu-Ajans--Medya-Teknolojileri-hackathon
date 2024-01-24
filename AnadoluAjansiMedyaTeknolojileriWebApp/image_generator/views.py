# image_generation/views.py

from rest_framework import viewsets
from .models import (Keyword, Subcategory, ObjectDetail, Character, 
                     NewsContext, VisualElements, StylePreferences, 
                     UserCustomizations, ImageGeneration)
from .serializers import (KeywordSerializer, SubcategorySerializer, 
                          ObjectDetailSerializer, CharacterSerializer, 
                          NewsContextSerializer, VisualElementsSerializer, 
                          StylePreferencesSerializer, UserCustomizationsSerializer, 
                          ImageGenerationSerializer)

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class ObjectDetailViewSet(viewsets.ModelViewSet):
    queryset = ObjectDetail.objects.all()
    serializer_class = ObjectDetailSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class NewsContextViewSet(viewsets.ModelViewSet):
    queryset = NewsContext.objects.all()
    serializer_class = NewsContextSerializer

class VisualElementsViewSet(viewsets.ModelViewSet):
    queryset = VisualElements.objects.all()
    serializer_class = VisualElementsSerializer

class StylePreferencesViewSet(viewsets.ModelViewSet):
    queryset = StylePreferences.objects.all()
    serializer_class = StylePreferencesSerializer

class UserCustomizationsViewSet(viewsets.ModelViewSet):
    queryset = UserCustomizations.objects.all()
    serializer_class = UserCustomizationsSerializer

class ImageGenerationViewSet(viewsets.ModelViewSet):
    queryset = ImageGeneration.objects.all()
    serializer_class = ImageGenerationSerializer
