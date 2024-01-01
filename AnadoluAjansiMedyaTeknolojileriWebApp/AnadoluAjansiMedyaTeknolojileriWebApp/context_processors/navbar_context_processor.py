# navbar_context_processor.py

import json
import os
from django.conf import settings

def aggregated_navbar(request):
    aggregated_navbar = []

    for app in settings.INSTALLED_APPS:
        navbar_path = os.path.join(settings.BASE_DIR, app, 'config', 'navbar.json')

        if os.path.isfile(navbar_path):
            with open(navbar_path, 'r') as file:
                try:
                    navbar_data = json.load(file)
                    aggregated_navbar.append(navbar_data)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {navbar_path}")

    return {'navbar': aggregated_navbar}
