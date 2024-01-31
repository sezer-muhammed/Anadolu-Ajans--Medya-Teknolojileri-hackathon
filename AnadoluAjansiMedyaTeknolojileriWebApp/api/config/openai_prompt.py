TEXT_PROMPT = """
You will be provided with a news article and a structured JSON template. Your task is to read and analyze the news article thoroughly to extract key information relevant to the various fields in the JSON template. The template is designed to capture various aspects of the news story, including its context, visual elements, style preferences, and user customizations.

Your role involves:

1. Parsing the News Article: Carefully read the news article to identify essential details like the headline, emotional tone, main subjects, geographical and temporal context, audience age group, keywords, and specific actions or appearances of characters mentioned in the story.

2. Filling the JSON Template: Accurately fill in each section of the JSON template with the identified information from the news article. This includes:
   - news_context: Populate with the headline, emotional tone, and other context-specific details.
   - visual_elements: Include descriptions of the main subject, background scene, color palette, and any dynamic elements or characters.
   - style_preferences: Define the art style, composition, and lighting based on the tone and content of the news.
   - user_customizations: Add any additional text, specific requests, or feedback loops as per user requirements or based on the news content.

3. Ensuring Clarity and Completeness: Make sure the JSON is filled comprehensively and clearly, providing a detailed and accurate representation of the news story. This filled JSON will serve as a guide for another AI model to create an image prompt.
4. Also use general terms for keywords so we can get same keywrods for different inputs.

The end goal is to create a detailed and accurate JSON file as code block that another model can use to generate a visual thumbnail or image that represents the essence of the news article. Your analysis and input must be thorough to ensure the final image accurately reflects the content and tone of the news story.



here is the template that you will fill:
{data}

here is the news article that you will analyze:
{text}
"""

IMAGE_PROMPT = """
You will be provided with an image. Your task is to closely analyze the image to extract key visual information relevant to the various fields in the JSON template. The template is designed to capture various aspects of the image, including its visual elements, contextual details, perceived emotions, and any notable features.

Your role involves:

1. Analyzing the Image: Examine the image to identify essential details such as the main subject, background elements, color palette, any characters or objects present, and the overall mood or tone.

2. Filling the JSON Template: Accurately fill in each section of the JSON template with the information identified from the image. This includes:
   - visual_elements: Describe the main subject, background scene, color palette, objects, characters, and any dynamic elements observed in the image.
   - contextual_details: Note any contextual clues that can be inferred from the image, such as possible geographical location, temporal context (time of day or historical period), or any text present in the image.
   - perceived_emotions: Detail any emotions or moods that the image evokes, based on the colors, composition, and subject matter.
   - notable_features: Mention any unique or striking features in the image that stand out.

3. Ensuring Clarity and Completeness: Ensure that the JSON is filled comprehensively and clearly, providing a detailed and accurate representation of the image. This filled JSON will serve as a guide for understanding the key elements and themes present in the image.
4. Also use general terms for keywords so we can get same keywrods for different inputs.

The end goal is to create a detailed and accurate JSON file as code block that captures the essence of the image. Your analysis and input must be thorough to ensure a comprehensive understanding of the visual story being told by the image.

Here is the template that you will fill:
{data}

"""