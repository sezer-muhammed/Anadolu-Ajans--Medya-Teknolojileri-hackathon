from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'images', views.ImageUploadViewSet)
router.register(r'texts', views.TextUploadViewSet)
router.register(r'voices', views.VoiceUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
