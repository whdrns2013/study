import pymupdf
from configparser import ConfigParser
import os

config = ConfigParser()
config.read("core/config.ini")

def read_pdf(path:str):
    doc = pymupdf.open(path)
    full_text = ""
    for page in doc:
        # preprocessing : Header 와 Footer 제거
        rect = page.rect # 페이지 크기
        header_height = int(config["header_and_footer"]["header.height"])
        footer_height = int(config["header_and_footer"]["footer.height"])
        header = page.get_text(clip=(0, 0, rect.width, header_height))
        footer = page.get_text(clip=(0, rect.height - footer_height, rect.width, rect.height))
        # 텍스트 추출
        text = page.get_text(clip=(0, header_height, rect.width, rect.height - footer_height))
        full_text += text + "\n---------------------------------\n"
    text_file_path = f"{config['path']['artifact']}/{os.path.splitext(os.path.basename(path))[0]}_with_preprocessing.txt"
    with open(text_file_path, 'w', encoding="utf-8") as f:
        f.write(full_text)
    return full_text