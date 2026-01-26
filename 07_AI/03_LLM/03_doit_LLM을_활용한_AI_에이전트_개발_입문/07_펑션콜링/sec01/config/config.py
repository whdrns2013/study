from configparser import ConfigParser

def get_config(config_path:str="config/secret.ini"):
    config = ConfigParser()
    config.read(config_path)
    return config

config = get_config()