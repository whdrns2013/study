from openai import OpenAI
from config.settings import config

def whisper_translation_api(audio_file_path:str, model:str="whisper-1"):
    # API setting
    api_key = config["apikey"]["openai"]
    client = OpenAI(api_key = api_key)
    
    # audio prep
    with open(audio_file_path, "rb") as f:
        # API request
        transcription = client.audio.translations.create( # transcription -> translation
            model = model,
            file = (f)
        )
        
    return transcription
    