import pytest

from utilities.baseClass import baseClass
# from testDataConfig.testDataConfigurations import *
from utilities.configurations import *



class Test_case(baseClass):
    def test_sample(self):
        data = getTestData()
        print(data['testcase2']['enterTheText'])
        print(data['testcase2']['enterThePassword'])