import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\Configuration\\config.ini")

class Readvalue:

    @staticmethod
    def getusername():
        username = config.get('login info', 'username')
        return username
    @staticmethod
    def getpassword():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def get_url():
        url = config.get("login info", "url")
        return url



# noncommerce
# php travel
# lorri
# IRCTC
# https://automation.credence.in/shop