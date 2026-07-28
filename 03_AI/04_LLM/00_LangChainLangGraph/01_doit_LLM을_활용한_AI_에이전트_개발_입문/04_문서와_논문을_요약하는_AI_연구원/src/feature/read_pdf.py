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
        # 텍스트 추출
        text = page.get_text(clip=(0, header_height, rect.width, rect.height - footer_height))
        full_text += text + "\n---------------------------------\n"
    return full_text