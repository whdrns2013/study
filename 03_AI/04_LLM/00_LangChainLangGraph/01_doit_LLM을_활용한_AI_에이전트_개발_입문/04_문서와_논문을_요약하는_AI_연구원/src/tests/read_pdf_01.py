import pymupdf
from configparser import ConfigParser
import os

config = ConfigParser()
config.read("core/config.ini")

def read_pdf(path:str):
    doc = pymupdf.open(path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        full_text += text
    text_file_path = f"{config['path']['artifact']}/{os.path.splitext(os.path.basename(path))[0]}.txt"
    with open(text_file_path, 'w', encoding="utf-8") as f:
        f.write(full_text)
    return full_text