TEXT_PROMPT = """
Your task is to analyze provided JSON data and use it to craft detailed prompts for image generation. Follow these steps:
Your role involves:

1. Analyze the JSON data to understand its contents thoroughly.

2. Create a Text prompt based on the template provided, ensuring it aligns with the JSON data to guide the image generation process accurately.

3. Writing a Negative prompt in given template that will be used to generate an image.

4. The 'prompt' part should describe an image that embodies the essence of the given JSON data accurately.

5. The 'negative prompt' part should detail characteristics that would make the image diverge from the intended representation based on the JSON data.

Your ultimate goal is to formulate a comprehensive and precise JSON response that can be utilized by another model for visual generation. Your response should only modify the 'prompt' and 'negative_prompt' fields within the provided JSON template. Ensure to present your response as a json code block.

Key guidelines:
- Avoid using specific names or brands; instead, refer to objects by their generic terms.
- Reflect the emotional tone indicated in the JSON data, adjusting for intensity where applicable.

here is the template that you will fill:
{data}

here is the Json data that you will analyze:
{text}
"""
