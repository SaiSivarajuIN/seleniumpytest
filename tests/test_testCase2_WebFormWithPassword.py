import pytest

from pages.pageObjects import pageObjects as pb
from utilities.baseClass import baseClass
from testDataConfig.testDataConfigurations import *


class TestCase2_webForm(baseClass):
    def test_testCase2_WebFormWithPassword(self):
        log = self.getLogger()
        getData = getTestDat(self)
        try:
            pb.webForm(self).checkTheWebFormWithPassword(getData['test_webForm2']['enterTheText'], getData['test_webForm2']['enterThePassword'])
            pb.responseForm(self).submittedResponse()
        except Exception:
            log.exception("Test Case2 WebForm With Password got Failed")
            pytest.fail("Test Case2 WebForm With Password got Failed")
