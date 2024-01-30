# image_generation/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (KeywordViewSet, SubcategoryViewSet, ObjectDetailViewSet, 
                    CharacterViewSet, NewsContextViewSet, VisualElementsViewSet, 
                    StylePreferencesViewSet, UserCustomizationsViewSet, 
                    ImageGenerationViewSet)

router = DefaultRouter()
router.register(r'keywords', KeywordViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'objectdetails', ObjectDetailViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'newscontexts', NewsContextViewSet)
router.register(r'visualelements', VisualElementsViewSet)
router.register(r'stylepreferences', StylePreferencesViewSet)
router.register(r'usercustomizations', UserCustomizationsViewSet)
router.register(r'imagegenerations', ImageGenerationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
