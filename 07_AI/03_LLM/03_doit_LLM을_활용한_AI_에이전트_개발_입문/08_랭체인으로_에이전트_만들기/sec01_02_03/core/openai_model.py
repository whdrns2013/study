from langchain_openai import ChatOpenAI
import os
from config.config import config

def get_model(model:str="gpt-4o-mini",
              api_key:str|None=None):
    if api_key is None:
        os.environ["OPENAI_API_KEY"] = config.get("apikey", "openai")
    model = ChatOpenAI(model=model)
    return model