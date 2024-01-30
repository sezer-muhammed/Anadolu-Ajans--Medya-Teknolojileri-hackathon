import requests
import json

host = "http://127.0.0.1:8888"

def text2img(params: dict) -> dict:
    """
    text to image
    """
    result = requests.post(url=f"{host}/v1/generation/text-to-image",
                           data=json.dumps(params),
                           headers={"Content-Type": "application/json"})
    return result.json()

result =text2img({
  "prompt": "Capture the resilient spirit of a vintage yellow car on a flooded rural road during twilight or dusk. Highlight the car's timeless journey through the rural landscape as it navigates the challenges of floods and isolation. Use earthy tones with pops of yellow and green in the color palette, emphasizing the smooth water reflections and the rough road. Create a horizontal frame with the car off-center, under natural, dim evening light. Depict the serene stillness of the flooded road and the strength of nature. Add a news agency watermark for authenticity.",
  "negative_prompt": "Avoid depicting the scene in a way that diminishes the resilient spirit of the vintage car or the challenges of the flooded rural road. Do not compromise the color palette or the composition with the car off-center. Ensure that the natural, dim evening light is accurately represented. Avoid introducing motion effects. Maintain the focus on the car's timeless journey and the mood of resilience. Do not include additional text or templates.",
  "image_number": 4,
    "async_process": False})
print(result)