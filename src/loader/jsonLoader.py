import json


class Tokens:
    def __init__(self):
        with open("resources/config/tokens.json", "r") as c:
            self.__config = json.load(c)

    def token(self):
        return self.__config["token"]

    def wavelink(self):
        return self.__config["wavelink"]["host"], self.__config["wavelink"]["port"], self.__config["wavelink"][
            "password"]

    def maria_db(self):
        return self.__config["mariadb"]["host"], self.__config["mariadb"]["user"], self.__config["mariadb"]["password"], \
            self.__config["mariadb"]["database"]

    def youtube(self):
        return self.__config["social_media"]["youtube"]
