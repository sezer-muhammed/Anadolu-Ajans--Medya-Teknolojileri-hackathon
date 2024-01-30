from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', MediaUploadView.as_view(), name='upload_media'),
    path('image-generations/', ImageGenerationListView.as_view(), name='image-generation-list'),
    path('imagegeneration-detail/<int:pk>/', ImageGenerationDetailView.as_view(), name='imagegeneration_detail'),
    path('generate-images/<int:pk>/', GenerateImagesView.as_view(), name='generate_images'),

]
