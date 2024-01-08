import google.generativeai as genai
from decouple import config


class GeminiModel:
    def __init__(self):
        # Configure the API key
        genai.configure(api_key=config("GOOGLE_GEMINI_API_KEY"))

        # Set up the generation configuration
        self.generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 32500,
        }

        # Set up the safety settings
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

        # Initialize the model
        self.model = genai.GenerativeModel(
            model_name="gemini-pro",
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
        )

    def generate_content(self, prompt_parts, media=None):
        """
        Generates content based on the given prompt parts.

        Parameters:
        prompt_parts (list): A list of strings, each representing a part of the prompt.

        Returns:
        str: The generated text response.
        """
        # TODO Add media handler for images
        response = self.model.generate_content(prompt_parts)
        return response.text
