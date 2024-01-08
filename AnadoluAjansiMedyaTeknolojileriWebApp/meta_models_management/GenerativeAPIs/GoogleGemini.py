import google.generativeai as genai
from decouple import config


class GeminiModel:
    """
    A class to interact with Google's Gemini Generative AI model.

    It configures the model with specific generation settings and safety settings to
    ensure the generated content adheres to certain standards. It provides a method
    to generate content based on a given prompt.

    Attributes
    ----------
    generation_config : dict
        Configuration settings for the generative model including temperature,
        top_p, top_k, and max_output_tokens.
    safety_settings : list
        A list of dictionaries specifying the safety categories and thresholds for content generation.
    model : genai.GenerativeModel
        The Gemini Generative AI model configured with the specified settings.

    Methods
    -------
    __init__()
        Initializes the GeminiModel with specified generation and safety settings.
    generate_content(prompt_parts: str, media=None) -> str
        Generates content based on the given prompt and optional media.
    """
    def __init__(self):
        """
        Initializes the GeminiModel with specified generation and safety settings.

        It configures the model using the GOOGLE_GEMINI_API_KEY from the environment
        and sets up the generation and safety configurations. It initializes the
        genai.GenerativeModel with these settings.
        """
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
        Generates content based on the given prompt and optional media.

        It uses the configured Gemini generative model to generate content based
        on the provided prompt. It can optionally include media in the generation
        process. The method returns the generated text.

        Parameters
        ----------
        prompt_parts : str
            The prompt to guide the content generation.
        media
            Optional media to include in the content generation process.

        Returns
        -------
        str
            The generated content as a text string.
        """
        response = self.model.generate_content(prompt_parts)
        return response.text
