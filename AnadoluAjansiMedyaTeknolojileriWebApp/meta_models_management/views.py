from django.shortcuts import render, redirect
from django.views import View
from .forms import CombinedUploadForm, SearchForm
from .models import InputRecord

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Instantiate a new form instance
        form = CombinedUploadForm()
        return render(request, 'meta_models_management/home.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # Create a form instance with POST data and files
        form = CombinedUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Save the form and handle the file and text uploads
            form.save()
            # Redirect to a new URL or the same with a success message (optional)
            return redirect('/meta_models_management/home/')  # Replace with the actual URL name for success

        # If the form is not valid, render the page again with the form (errors will show)
        return render(request, 'meta_models_management/home.html', {'form': form})
    

class SmartSearch(View):
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
