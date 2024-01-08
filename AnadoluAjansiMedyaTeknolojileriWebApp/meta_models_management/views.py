from django.shortcuts import render, redirect
from django.views import View
from .forms import CombinedUploadForm, SearchForm
from .models import InputRecord


class HomeView(View):
    """
    A view that handles the main page requests for the Meta Models Management module.

    This view responds to both GET and POST requests.
    For GET, it simply displays a form. For POST, it processes submitted data.
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
            input_records = InputRecord.objects.all()

            # Dynamically build filter arguments based on form input
            filter_args = {}
            for field, value in form.cleaned_data.items():
                if value:
                    if hasattr(InputRecord, field):
                        filter_key = f"{field}__icontains"
                    else:
                        related_model, related_field = field.split("_", 1)
                        filter_key = f"{related_model}__{related_field}__icontains"
                    filter_args[filter_key] = value

            input_records = input_records.filter(**filter_args)

            return render(
                request,
                "meta_models_management/smart_search_results.html",
                {"form": form, "input_records": input_records},
            )
        else:
            return render(request, "smart_search.html", {"form": form})
