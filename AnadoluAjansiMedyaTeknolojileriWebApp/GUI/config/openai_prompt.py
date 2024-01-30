TEXT_PROMPT = """
You will be provided a json data that includes all necesery information to generate an image.
Your role involves:

1. Understanding the json data.

2. Writing a Text prompt in given template that will be used to generate an image.

3. Writing a Negative prompt in given template that will be used to generate an image.

4. For prompt part describe the image reflects the given json data.

5. For negative prompt part describe the image does not reflect the given json data.

The end goal is to create a detailed and accurate JSON file that another model can use to generate a visual.

ONLY write one json response in given format just change prompt and negative_prompt values. write whole json code as code block


here is the template that you will fill:
{data}

here is the Json data that you will analyze:
{text}
"""