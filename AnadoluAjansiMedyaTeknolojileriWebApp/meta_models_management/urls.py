# urls.py
from django.urls import path
from .views import HomeView, SmartSearch

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('smart-search/', SmartSearch.as_view(), name='smart_search'),
]
