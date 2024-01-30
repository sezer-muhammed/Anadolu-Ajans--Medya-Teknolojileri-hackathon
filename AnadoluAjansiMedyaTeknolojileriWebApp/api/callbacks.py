import json
from .config.openai_prompt import TEXT_PROMPT
from .openai_interface import OpenAIInterface
import requests  # Import the requests library


class ImageCallback:
    @staticmethod
    def process_image(image):
        pass

        # Code to call OpenAI API with the image

class TextCallback:
    @staticmethod
    def process_text(text):
        """
        Process the given text by generating an image based on the text.

        Parameters:
        text (str): The text to be processed.

        Returns:
        None
        """
        news_article_text = text.text
        with open("image_generator/config/image_upload.json", 'r') as file:
          data = json.load(file)
          json_template_data = json.dumps(data, indent=4)
        filled_prompt = TEXT_PROMPT.format(data=json_template_data, text=news_article_text)

        open_ai_engine = OpenAIInterface()
        # response is dumped json   
        response: dict = open_ai_engine.generate_text(filled_prompt)
        # Make a POST request to the /image_generator/imagegenerations/ endpoint
        from image_generator.serializers import ImageGenerationSerializer
        serializer = ImageGenerationSerializer(data=response)
        if serializer.is_valid():
          saved_model = serializer.save()
          saved_model.text_upload = text
          saved_model.save()
        else:
          print(serializer.errors)
