from django.shortcuts import render, redirect
from django.views import View
from django import forms
from django.db.models import Q

from .forms import CombinedUploadForm, SearchForm
from .models import InputRecord


class HomeView(View):
    """
    A view that handles the main page requests for the Meta Models Management module.

    This view responds to both GET and POST requests.
    For GET, it simply displays a form. For POST, it processes submitted data.
    """

    """
    View class for the home page.

    This class handles the GET and POST requests for the home page.
    GET request renders the home.html template with a new form instance.
    POST request validates the form data, saves the form, and handles file and text uploads.
    If the form is valid, it redirects to a new URL or the same URL with a success message.
    If the form is not valid, it renders the home.html template with the form and displays errors.
    """

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests: instantiate a new form instance and render the home page.

        Parameters
        ----------
        request : HttpRequest
            The request object used to generate the HttpResponse.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.

        Returns
        -------
        HttpResponse
            Rendered web page with the context data (form instance).
        """
        form = CombinedUploadForm()  # Instantiate a new form instance
        return render(request, "meta_models_management/home.html", {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: create a form instance with POST data and files,
        then check if it's valid, save it, and redirect or re-render with errors.

        Parameters
        ----------
        request : HttpRequest
            The request object used to generate the HttpResponse.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.

        Returns
        -------
        HttpResponse
            Redirects to a new URL on successful form submission or
            re-renders the page with form errors if the form is invalid.
        """
        form = CombinedUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()  # Save the form and handle the file and text uploads
            return redirect("/meta_models_management/")  # Redirect to success URL

        # If the form is not valid, render the page again with the form (errors will show)
        return render(request, "meta_models_management/home.html", {"form": form})


class SmartSearch(View):
    """
    A view that handles smart search requests for input records.

    It responds to both GET and POST requests. For GET, it displays the search form.
    For POST, it processes the form, applies filters based on the input, and returns the search results.
    """

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests: instantiate a new search form instance and render the search page.

        Parameters
        ----------
        request : HttpRequest
            The request object used to generate the HttpResponse.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.

        Returns
        -------
        HttpResponse
            Rendered web page with the context data (search form instance).
        """
        form = SearchForm()  # Instantiate a new search form instance
        return render(
            request, "meta_models_management/smart_search.html", {"form": form}
        )

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: create a form instance with POST data,
        apply dynamic filters based on the form input, and render the results page or re-render with errors.

        Parameters
        ----------
        request : HttpRequest
            The request object used to generate the HttpResponse.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.

        Returns
        -------
        HttpResponse
            Redirects to the results page with the search results and form data or
            re-renders the search page with form errors if the form is invalid.
        """
        form = SearchForm(request.POST)

        if form.is_valid():
            input_records_query  = InputRecord.objects.all()

            input_records_query = self.apply_multichoice_filters(form, input_records_query)

            return render(request, "meta_models_management/smart_search_results.html", {"input_records": input_records_query })
        else:
            return render(request, "meta_models_management/smart_search.html", {"form": form})
        
    @staticmethod
    def apply_multichoice_filters(form, queryset):
        """
        Applies filters to the queryset based on selected options in multichoice fields of the form.

        Parameters:
        - form: The submitted Django form with cleaned data.
        - queryset: The initial queryset to apply filters on.

        Returns:
        - A queryset with applied filters.
        """
        for field_name, field in form.fields.items():
            if isinstance(field, forms.ModelMultipleChoiceField):
                selected_options = form.cleaned_data.get(field_name)
                if selected_options:
                    # Define a mapping from form field names to model field names
                    field_mapping = {
                        'keyword': 'content_analysis__keywords',
                        'emotion': 'ai_analysis__emotion_analysis__associated_emotions',
                        # Add other mappings here as needed
                    }
                    model_field_name = field_mapping.get(field_name, field_name)

                    # Constructing the filter argument dynamically
                    filter_arg = {f"{model_field_name}__in": selected_options}

                    # Applying the filter
                    queryset = queryset.filter(**filter_arg).distinct()

        return queryset