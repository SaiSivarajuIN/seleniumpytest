import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('../seleniumpytest/utilities/properties.ini')
    return config


def getTestData():
    td = configparser.ConfigParser()
    td.read('../seleniumpytest/testDataConfig/propertiesTestData.ini')
    return td


