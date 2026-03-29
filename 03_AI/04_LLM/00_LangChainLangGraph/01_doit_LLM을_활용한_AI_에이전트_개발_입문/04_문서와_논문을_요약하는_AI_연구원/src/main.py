from configparser import ConfigParser
import os

config = ConfigParser()
config.read("core/config.ini")

def main():
    pass

def test():
    from tests import read_pdf_01, read_pdf_with_preprocessing_02, summarize_thesis
    # 01. read_pdf
    pdf_path = "data/KCI_FI003103066.pdf"
    result = read_pdf_01.read_pdf(pdf_path)
    # 02. read_pdf with preprocessing
    pdf_path = "data/KCI_FI003103066.pdf"
    result = read_pdf_with_preprocessing_02.read_pdf(pdf_path)
    # 03. summarize
    result = summarize_thesis.summarize_thesis(result)
    print(result)
    
    

if __name__ == "__main__":
    if config["debug"]["mode.debug.activate"]:
        test()
    main()
