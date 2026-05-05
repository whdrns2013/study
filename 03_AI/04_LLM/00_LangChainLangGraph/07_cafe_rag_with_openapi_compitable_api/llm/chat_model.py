from langchain_google_genai import ChatGoogleGenerativeAI
import os
from config.config import secret

# 모델 로딩
def load_model(api_key:str|None=None,
               model_name:str|None="gemini-2.5-flash",
               streaming:bool=False):
    if api_key is None:
        api_key = secret["apikey"]["google"]
    os.environ["GOOGLE_API_KEY"] = api_key
    model = ChatGoogleGenerativeAI(model=model_name, streaming=streaming)
    return model