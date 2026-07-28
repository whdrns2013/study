from openai import OpenAI
from core.config import config
from schemas.dto import OpenAIMessage

def chat_gpt(user_message:str|None=None,
             system_message:str|None=None,
             assistant_message:str|None=None,
             messages:list[OpenAIMessage]|list[dict]|None=None,
             model:str="gpt-4o",
             temperature:float=0.1):
    
    api_key = config["apikey"]["openai"]
    client = OpenAI(api_key = api_key)
    if messages:
        response = client.chat.completions.create(
            model = model,
            temperature = temperature,
            messages = [message.__dict__ for message in messages] if isinstance(messages[0], OpenAIMessage) else messages
        )
    else:
        messages = []
        
        if system_message:
            messages.append({"role":"system", "content":system_message})
        if user_message:
            messages.append({"role":"user", "content":user_message})
        if assistant_message:
            messages.append({"role":"assistant", "content":assistant_message})
        
        response = client.chat.completions.create(
            model = model,
            temperature = temperature,
            messages = messages
        )    
    
    return response

# 결과 텍스트 출력
# response.choices[0].message.content

# TODO: 스트리밍 적용