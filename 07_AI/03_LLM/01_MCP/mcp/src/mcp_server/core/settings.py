from configparser import ConfigParser

config = ConfigParser()
config.read("core/config.ini")

class ServerSettings:
    def __init__(self, config):
        self.host = config["server"]["host"]
        self.port = config["server"]["port"]

class AddressBookSettings:
    def __init__(self, config):
        self.db_type = config["address_book"]["db.db_type"]
        self.db_conf = {
            "user": config["address_book"]["db.user"],
            "password": config["address_book"]["db.passwd"],
            "host": config["address_book"]["db.host"],
            "port": config["address_book"]["db.port"],
            "dbname": config["address_book"]["db.db_name"],
        }
        self.table_name = config["address_book"]["db.table_name"]
        self.email_col = config["address_book"]["db.col.email"]
        self.name_col = config["address_book"]["db.col.name"]
        self.group_name_col = config["address_book"]["db.col.group_name"]

class Settings:
    def __init__(self, config):
        self.server = ServerSettings(config)
        self.address_book = AddressBookSettings(config)

settings = Settings(config)