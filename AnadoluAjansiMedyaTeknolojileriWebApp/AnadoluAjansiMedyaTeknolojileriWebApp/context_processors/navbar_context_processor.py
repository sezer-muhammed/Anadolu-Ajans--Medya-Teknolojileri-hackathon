# navbar_context_processor.py

import json
import os
from django.conf import settings


def aggregated_navbar(request):
    """
    Retrieve and aggregate navbar data from different apps.

    This function iterates over the installed apps in the Django settings and looks for a "navbar.json" file
    in each app's "config" directory. If found, it reads the JSON data from the file and appends it to the
    aggregated_navbar list. The aggregated_navbar list is then returned as a context variable.

    Parameters:
        request (HttpRequest): The current HTTP request object.

    Returns:
        dict: A dictionary containing the aggregated navbar data.

    Raises:
        FileNotFoundError: If the "navbar.json" file is not found in any app's "config" directory.
        json.JSONDecodeError: If there is an error decoding the JSON data from the "navbar.json" file.
    """
    aggregated_navbar = []

    for app in settings.INSTALLED_APPS:
        navbar_path = os.path.join(settings.BASE_DIR, app, "config", "navbar.json")

        if os.path.isfile(navbar_path):
            with open(navbar_path, "r") as file:
                try:
                    navbar_data = json.load(file)
                    aggregated_navbar.append(navbar_data)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {navbar_path}")

    return {"navbar": aggregated_navbar}
