from openai import OpenAI
from config.settings import config
from utils.image_encoding import encode_image

def image_explanation(image_file_path:str|None=None,
                      image_url:str|None=None,
                      prompt:str|None=None):
    api_key = config["apikey"]["openai"]
    client = OpenAI(api_key=api_key)
    
    if not prompt:
        prompt = "이 이미지에 대해 설명해 주세요."
    
    if (image_url is not None) and (image_file_path is None):
        message = {
            "type" : "image_url",
            "image_url": {
                "url" : image_url
            }
        }
    elif (image_url is None) and (image_file_path is not None):
        emcoded_image = encode_image(image_file_path)
        message = {
            "type":"image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{emcoded_image}"
            }
        }
    
    messages = [
        {
            "role":"user",
            "content":[
                {"type":"text", "text":prompt},
                message
            ]
        }
    ]
    
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages
    )
    
    return response