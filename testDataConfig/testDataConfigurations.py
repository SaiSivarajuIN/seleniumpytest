import configparser


def getTestDat():
    config = configparser.ConfigParser()
    config.read('../testDataConfig/testDataProperties.ini')
    return


'''config = configparser.ConfigParser()
config.read('../testDataConfig/testDataProperties.ini')
print(config['test_webForm2']['enterTheText'])
print(config['test_webForm2']['enterThePassword'])'''