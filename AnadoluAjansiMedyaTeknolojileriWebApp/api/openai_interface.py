import openai
import os
import json

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

            response = response.choices[0].message.content
            response = response.split("```json")[1]
            response = response.split("```")[0]
            response = response.replace("\n", "")

            response_json = json.loads(response)

            return response_json
        except Exception as e:
            print(e)
            return None
