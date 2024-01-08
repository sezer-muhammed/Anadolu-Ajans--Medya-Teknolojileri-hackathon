from django.shortcuts import render, redirect
from django.views import View
from .forms import CombinedUploadForm, SearchForm
from .models import InputRecord

class HomeView(View):
    """
    View class for the home page.

    This class handles the GET and POST requests for the home page.
    GET request renders the home.html template with a new form instance.
    POST request validates the form data, saves the form, and handles file and text uploads.
    If the form is valid, it redirects to a new URL or the same URL with a success message.
    If the form is not valid, it renders the home.html template with the form and displays errors.
    """

    def get(self, request, *args, **kwargs):
        form = CombinedUploadForm()
        return render(request, 'meta_models_management/home.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CombinedUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('/meta_models_management/home/')

        return render(request, 'meta_models_management/home.html', {'form': form})
    

class SmartSearch(View):
    """
    A class-based view for performing smart search functionality.

    This view handles both GET and POST requests. GET request renders the search form,
    while POST request processes the form input and applies filters to the queryset.

    Attributes:
        None

    Methods:
        get: Renders the search form.
        post: Processes the form input and applies filters to the queryset.

    Usage:
        To use this view, simply include it in your URL configuration and specify the appropriate
        template for rendering the search form and displaying the search results.
    """
    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, 'meta_models_management/smart_search.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            input_records = InputRecord.objects.all()

            # Dynamically build filter arguments based on form input
            filter_args = {}
            for field, value in form.cleaned_data.items():
                if value:
                    # Determine if the field is related to InputRecord directly or through a related model
                    if hasattr(InputRecord, field):
                        # Direct field
                        filter_key = f'{field}__icontains'
                    else:
                        # Related model field
                        # This assumes a naming convention where form fields for related models are named
                        # as the related model's name in lowercase followed by an underscore and the field name
                        # Adjust this according to your actual field naming and model structure
                        related_model, related_field = field.split('_', 1)
                        filter_key = f'{related_model}__{related_field}__icontains'
                    filter_args[filter_key] = value

            # Apply the filters to the queryset
            input_records = input_records.filter(**filter_args)

            return render(request, 'smart_search_results.html', {
                'form': form,
                'input_records': input_records
            })
        else:
            return render(request, 'smart_search.html', {'form': form})
