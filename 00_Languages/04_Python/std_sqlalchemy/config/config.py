from configparser import ConfigParser

def load_conifg(path:str):
    config = ConfigParser()
    config.read(path)
    return config

config = load_conifg("config/config.ini")