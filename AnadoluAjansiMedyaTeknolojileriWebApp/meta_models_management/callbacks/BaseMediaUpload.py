from ..GenerativeAPIs.GoogleGemini import GeminiModel
from ..serializers import InputRecordSerializer

#load json meta_models_management\config\InputRecordSerializerJson.json

import json

with open('meta_models_management/config/InputRecordSerializerJson.json') as f:
    data = json.load(f)

def clean_json_string(result: str) -> str:
    """
    Removes the specified markers from the input string.

    Parameters:
    result (str): The input string containing the JSON data with extra markers.

    Returns:
    str: The cleaned string with the markers removed.
    """
    # Define the markers to be removed
    markers = ["```json", "```"]

    # Iterate over each marker and remove it from the string
    for marker in markers:
        result = result.replace(marker, "")


    return result.strip()

def uploaded_file_analyse_callback(instance):
    # Instantiate the Gemini model
    gemini_model = GeminiModel()
    # Define the prompt for content generation
    prompt_parts = ["Analyze the uploaded file: ", str(instance.text), f"And fill the json with realistic values fill as much as possible. use the json: {data}. Only response as json code. put \" for json str and use ' for text."]
    
    # Generate and process the response
    response = gemini_model.generate_content(prompt_parts)
    json_data = clean_json_string(response)

    json_data = json.loads(json_data)

    serializer = InputRecordSerializer(data=json_data)
    if serializer.is_valid():
        serializer.save()