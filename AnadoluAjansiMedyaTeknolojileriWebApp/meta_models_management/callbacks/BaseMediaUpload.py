from ..GenerativeAPIs.GoogleGemini import GeminiModel
from ..serializers import InputRecordSerializer
import json


class InputRecordGenerator:
    """
    A class to generate InputRecord instances based on configuration data and input instances.

    It reads configuration data from a JSON file and generates prompts for a text generation model. 
    It also provides methods to clean and process the generated text into valid JSON for InputRecord creation.

    Methods
    -------
    __init__()
        Initializes the generator by loading the configuration data.
    clean_json_string(result: str) -> str
        Cleans the JSON string by removing specified markers and text outside the markers.
    generate_optimized_prompt(instance, data) -> str
        Generates a prompt for the Gemini model based on an input instance and configuration data.
    uploaded_file_analyse_callback(instance)
        Callback function to process an uploaded file and create an InputRecord instance.
    """
    def __init__(self):
        """
        Initializes the InputRecordGenerator by loading configuration data from a JSON file.

        It reads the JSON file and stores the data in the 'data' attribute for use in generating prompts.
        """
        # Load the configuration data for the Gemini model
        with open("meta_models_management/config/InputRecordSerializerJson.json") as f:
            self.data = json.load(f)

    def clean_json_string(self, result: str) -> str:
        """
        Cleans the JSON string by removing markers and text outside the markers.

        Parameters
        ----------
        result : str
            The input string containing JSON data with extra markers and additional text.

        Returns
        -------
        str
            The cleaned JSON string with markers and outside text removed.
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

    def generate_optimized_prompt(self, instance, data):
        """
        Generates a prompt for the Gemini model based on an input instance and configuration data.

        Parameters
        ----------
        instance
            The input instance containing the text to be analyzed.
        data
            The configuration data loaded from the JSON file.

        Returns
        -------
        str
            A string representing the optimized prompt to be sent to the Gemini model.
        """
        prompt_parts = [
            "Analyze the uploaded text and generate a response in JSON format. ",
            "The uploaded text is: '",
            str(instance.text),
            "'. ",
            "Fill the JSON with realistic and relevant values. ",
            "Ensure all fields are complete and adhere to these rules: ",
            "- 'input_id' should not exceed 200 characters. ",
            "- 'timestamp' should be a current and valid timestamp. ",
            "- 'source_info' should include 'city', 'country', 'latitude', and 'longitude', none of which can be null. ",
            "- 'content_analysis.keywords' should be a list of dictionaries, not strings. ",
            "Use the following JSON as a guide: ",
            str(data),
            " ",
            "Remember, use double quotes (\") for JSON strings and single quotes (') for the text within this prompt. ",
        ]
        return "".join(prompt_parts)

    def uploaded_file_analyse_callback(self, instance):
        """
        Processes an uploaded file, generates a response, cleans the JSON data, and creates an InputRecord.

        This method uses the Gemini model to generate a response based on the uploaded file. It then cleans
        the response to obtain valid JSON data and attempts to create an InputRecord instance using the data.

        Parameters
        ----------
        instance
            The instance representing the uploaded file to be analyzed.

        Returns
        -------
        None
        """
        # Instantiate the Gemini model
        gemini_model = GeminiModel()

        # Generate and process the response
        response = gemini_model.generate_content(
            self.generate_optimized_prompt(instance, self.data)
        )
        json_data = self.clean_json_string(response)

        json_data = json.loads(json_data)

        # Validate and save the data
        serializer = InputRecordSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
        else:
            # Log or print the errors for debugging
            print("Serializer errors:", serializer.errors)
