import json
from .config.openai_prompt import TEXT_PROMPT

class ImageCallback:
    @staticmethod
    def process_image(image):
        print(image.id)
        print(image.image.url)

        # Code to call OpenAI API with the image

class TextCallback:
    @staticmethod
    def process_text(text):
        news_article_text = text.text
        with open("image_generator/config/image_upload.json", 'r') as file:
            data = json.load(file)
            json_template_data = json.dumps(data, indent=4)
        filled_prompt = TEXT_PROMPT.format(data=json_template_data, text=news_article_text)
        print(filled_prompt)

        # Code to call OpenAI API with the text
