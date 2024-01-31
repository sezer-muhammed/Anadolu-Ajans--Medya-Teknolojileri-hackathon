TEXT_PROMPT = """
Your task is to analyze a news article and use your insights to fill a structured JSON template accurately. This process aims to capture the article's essence, focusing on context, visual elements, stylistic preferences, and anticipated user customizations to guide an AI model in generating a relevant image.

Steps to follow:

1. **Parsing the News Article**: Carefully read the article to identify crucial information, including the headline, emotional tone, main subjects, geographical and temporal context, intended audience, keywords, and descriptions of characters or actions.

2. **Filling the JSON Template**: With the information extracted from the news article, fill in the JSON template accordingly. Each section is designed to encapsulate different aspects of the article's content and how it should be visually represented:

   - `news_context`: Input the headline, categorize the image, and specify the emotional tone and intensity. Include geographical and temporal contexts, assess the source's credibility, identify the target audience age group and interests, and as much as you can, list relevant keywords and subcategories.
   
   - `visual_elements`: Detail the main subject and background scene, specify the color palette and texture that match the mood of the article, describe any dynamic elements, motion effects, and characters (including their actions and appearances), and note unique objects or items within the scene.
   
   - `style_preferences`: Choose an art style, composition, and lighting that best convey the article's tone and content. Specify the desired aspect ratio to ensure the generated image aligns with the preferred visual presentation.
   
   - `user_customizations`: Anticipate additional elements the user might want to include,
   
3. **Ensuring Clarity and Completeness**: Your filled JSON should be detailed and clear, enabling the creation of an image that accurately reflects the news article. This comprehensive JSON will guide another AI model in generating an image that captures the story's essence and meets user expectations.

- Utilize generic terms for consistent keyword extraction.
- Assess emotional tone with a specific focus, such as considering Turkey's perspective for financial news.
- Fill all values, if they should be empty write N/A
- Fill in English

The objective is to develop a detailed JSON file, formatted as a code block, that can direct an AI model to produce a visual thumbnail or image. This visual should not only represent the news article's content and emotional tone accurately but also resonate with potential user preferences and the style that best communicates the story.

Template to fill:
{data}

News article to analyze:
{text}
"""


IMAGE_PROMPT = """
You are provided with an image and tasked with dissecting its visual components to populate a structured JSON template accurately. This exercise aims to capture the multifaceted nature of the image, including visual details, contextual nuances, emotional undertones, and distinctive features.

Proceed as follows:

1. **Analyzing the Image**: Scrutinize the image to pinpoint key elements such as the primary subject, background scenery, color scheme, any discernible characters or objects, and the overall atmosphere or sentiment it conveys.

2. **Filling the JSON Template**: Utilize the insights gathered from your analysis to meticulously complete each section of the JSON template, ensuring a holistic representation of the image:
   - `visual_elements`: Enumerate the principal subject, backdrop, color dynamics, characters, objects, and any motion or activity depicted.
   - `contextual_details`: Infer and document potential contextual indicators like the geographical setting, time of day, era, or explicit text seen in the image.
   - `perceived_emotions`: Express the emotions or moods elicited by the image, considering its coloration, layout, and thematic content.
   - `notable_features`: Highlight peculiar or particularly compelling aspects of the image that capture attention.

3. **Ensuring Clarity and Completeness**: Your goal is to craft a JSON response that is both comprehensive and precise, offering an in-depth visual and thematic analysis of the image. This document will facilitate a deeper understanding of the image's core elements and storytelling aspects.

- Employ generalized terminology for consistent keyword identification across various images.
- When analyzing images with financial themes, interpret emotional tones from a perspective relevant to the context, such as considering Turkey's viewpoint for financial imagery.
- Fill all values, if they should be empty write N/A
- Fill in English

Your comprehensive and detailed JSON documentation will encapsulate the essence of the image, enabling a nuanced appreciation of its visual narrative.

Template to fill:
{data}
"""