import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('../utilities/properties.ini')
    return config


def getTestData():
    td = configparser.ConfigParser()
    td.read('../testDataConfig/propertiesTestData.ini')
    return td


