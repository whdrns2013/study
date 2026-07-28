from openai import OpenAI
from core.config import config

def chat_gpt(user_message:str|None=None,
             system_message:str|None=None,
             assistant_message:str|None=None,
             model:str="gpt-4o",
             temperature:float=0.1):
    
    api_key = config["apikey"]["openai"]
    client = OpenAI(api_key = api_key)
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