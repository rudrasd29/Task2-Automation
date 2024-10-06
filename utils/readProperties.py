from configparser import ConfigParser

config = ConfigParser()
configFile= config.read('./Configurations/config.ini')

# data = ConfigParser()
# dataFile = config.read('./Data/data.txt')

class ReadProperties:
    @staticmethod
    def getBaseUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getData_Name():
        with open('./Data/data.txt') as dataFile:
            lines = dataFile.readlines()
        for line in lines:
            name = line.strip()
            return name
