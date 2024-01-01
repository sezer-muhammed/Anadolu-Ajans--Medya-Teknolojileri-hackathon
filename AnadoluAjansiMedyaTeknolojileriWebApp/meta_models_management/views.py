from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Your logic for handling GET requests
        return render(request, 'meta_models_management/home.html')

    def post(self, request, *args, **kwargs):
        # Your logic for handling POST requests
        # For now, it just renders the same page
        return render(request, 'meta_models_management/home.html')
