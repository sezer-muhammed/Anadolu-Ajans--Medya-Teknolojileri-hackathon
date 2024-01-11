import json
import os
from django.conf import settings

def aggregated_navbar(request):
    """
    Retrieve and aggregate navbar data from the core project and different apps.

    This function first reads a "config.json" file from the core project home, then iterates over the 
    installed apps in the Django settings and looks for a "navbar.json" file in each app's "config" directory.
    It reads the JSON data from these files and appends it to the aggregated_navbar list, which is then returned 
    as a context variable.

    Parameters:
        request (HttpRequest): The current HTTP request object.

    Returns:
        dict: A dictionary containing the aggregated navbar data.

    Raises:
        FileNotFoundError: If the "config.json" or "navbar.json" file is not found.
        json.JSONDecodeError: If there is an error decoding the JSON data from the files.
    """
    aggregated_navbar = []

    # Read the config.json from the core project home
    core_config_path = os.path.join(settings.BASE_DIR, "config.json")
    
    if os.path.isfile(core_config_path):
        with open(core_config_path, "r") as file:
            try:
                core_config_data = json.load(file)
                aggregated_navbar.append(core_config_data)
                print(aggregated_navbar)
            except json.JSONDecodeError:
                print(f"Error decoding JSON from {core_config_path}")
    else:
        print(f"File {core_config_path} not found")
    # Read the navbar.json from each installed app
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
