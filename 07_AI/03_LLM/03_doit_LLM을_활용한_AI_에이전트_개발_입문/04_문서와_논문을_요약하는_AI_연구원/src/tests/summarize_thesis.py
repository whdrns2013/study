from configparser import ConfigParser
from feature.gemini_api import gemini_api
import os

config = ConfigParser()
config.read("core/config.ini")

def summarize_thesis(text):
    # prompt
    prompt_file = os.path.join(config["path"]["data"], config["file"]["prompt.summarize.0.1"])
    with open(prompt_file, "r", encoding="utf-8") as f:
        prompt = f.read()
    prompt += "\n" + text
    # Gemini API
    result = gemini_api(prompt)
    return result