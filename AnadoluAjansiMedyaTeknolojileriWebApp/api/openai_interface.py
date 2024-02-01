import openai
import os
import json
import base64

os.environ["OPENAI_API_KEY"] = "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"

class OpenAIInterface:
    """
    A class that provides an interface for generating text using OpenAI models.

    Attributes:
        None

    Methods:
        generate_text: Generates text based on a given prompt using the specified OpenAI model.

    """

    def generate_text(self, prompt, model="gpt-4-turbo-preview"):
        """
        Generates text based on a given prompt using the specified OpenAI model.

        Args:
            prompt (str): The prompt for generating text.
            model (str, optional): The OpenAI model to use for text generation. Defaults to "gpt-4-turbo-preview".

        Returns:
            dict: The generated text as a JSON object.

        Raises:
            Exception: If an error occurs during text generation.

        """

        client = openai.OpenAI()

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. designed to response as json."},
                    {"role": "user", "content": f"{prompt}"},
                ]
            )

            response_content = response.choices[0].message.content

            # Extract content between the first and last triple backticks
            if '```json' in response_content:
                start = response_content.find('```json') + len('```json')
            elif '```' in response_content:
                start = response_content.find('```') + len('```')

            end = response_content.rfind('```')

            response_content = response_content[start:end].strip()
            response_content = response_content.replace("\n", "")

            response_json = json.loads(response_content)

            return response_json
        except Exception as e:
            print(e)
            return None
        
    def generate_image(self, prompt, image_path, model="gpt-4-vision-preview"):
        def encode_image(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        
        base64_image = encode_image(image_path)

        client = openai.OpenAI()

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": f'{prompt}'},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                    "detail": "low"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=3000,
            )

            response_content = response.choices[0].message.content

            if '```json' in response_content:
                start = response_content.find('```json') + len('```json')
            elif '```' in response_content:
                start = response_content.find('```') + len('```')

            end = response_content.rfind('```')

            response_content = response_content[start:end].strip()
            response_content = response_content.replace("\n", "")
            response_json = json.loads(response_content)
            return response_json
        except Exception as e:
            print(e)
            return None