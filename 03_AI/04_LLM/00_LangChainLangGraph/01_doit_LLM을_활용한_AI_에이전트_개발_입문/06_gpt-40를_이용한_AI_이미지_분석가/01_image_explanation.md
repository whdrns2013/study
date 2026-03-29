
## GPT 비전 사용법

### 설명 요청하기  

```python
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
```

- 결과  

```plaintext
'이 이미지는 도시 거리의 장면을 보여줍니다. 중심에는 빨간색 택시가 있으며, 그 위에 "TAXI"라는 표시가 있습니다. 주변에는 사람들이 걸어다니고 있고, 건물들이 양 옆에 배치되어 있습니다. 거리의 분위기가 도시적이고 활기찬 느낌을 줍니다.',

이 이미지는 도시의 거리 풍경을 담고 있습니다. 이미지의 중심에는 빨간색 택시가 정차해 있고, 택시 위에는 "TAXI" 표시가 있습니다. 주변에는 상점들이 늘어서 있으며, 몇몇 행인들이 거리를 걷고 있습니다. 거리에는 다양한 건물들이 있고, 도시는 바쁜 분위기를 느끼게 합니다
```