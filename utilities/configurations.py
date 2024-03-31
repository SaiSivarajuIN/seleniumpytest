import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('/home/sivaraju/Desktop/code/python-selenuim/pythonProject2/utilities/properties.ini')
    return config


