import openai

class OpenAIInterface:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_text(self, prompt, model = "gpt-4-turbo-preview"):
        try:
            response = openai.Completion.create(
                model=model,
                prompt=prompt
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return None
