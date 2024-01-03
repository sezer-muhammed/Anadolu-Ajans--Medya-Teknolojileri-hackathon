from ..GenerativeAPIs.GoogleGemini import GeminiModel
from ..serializers import InputRecordSerializer
import json

class InputRecordGenerator:
    def __init__(self):
        # Load the configuration data for the Gemini model
        with open('meta_models_management/config/InputRecordSerializerJson.json') as f:
            self.data = json.load(f)
    
    def clean_json_string(self, result: str) -> str:
        """
        Removes the specified markers and any text outside the markers from the input string.

        Parameters:
        result (str): The input string containing the JSON data with extra markers and additional text.

        Returns:
        str: The cleaned string with the markers and outside text removed.
        """
        # Define the markers to identify the JSON portion
        start_marker = "```json"
        end_marker = "```"

        # Find the position of the markers
        start_pos = result.find(start_marker) + len(start_marker)
        end_pos = result.find(end_marker, start_pos)

        # Extract the JSON part and remove the markers
        if start_pos > -1 and end_pos > -1:
            json_part = result[start_pos:end_pos].strip()
        else:
            # If the markers are not found, return the original string
            json_part = result

        return json_part

    def uploaded_file_analyse_callback(self, instance):
        # Instantiate the Gemini model
        gemini_model = GeminiModel()

        # Define the prompt for content generation
        prompt_parts = [
            "Analyze the uploaded file: ", 
            str(instance.text), 
            f"And fill the json with realistic values fill as much as possible. use the json: {self.data}. Only response as json code. put \" for json str and use ' for text."
        ]
        
        # Generate and process the response
        response = gemini_model.generate_content(prompt_parts)
        json_data = self.clean_json_string(response)

        json_data = json.loads(json_data)

        # Validate and save the data
        serializer = InputRecordSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
