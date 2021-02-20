import configparser

config = configparser.RawConfigParser()
config.read("D:\\Python Programs\\SeleniumPavanSDET\\NopCommerce\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():    # Static method...Can access method using classname only
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
