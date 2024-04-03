import pytest

from pages.pageObjects import pageObjects as pb
from utilities.baseClass import baseClass
from utilities.configurations import *


class TestCase2_webForm(baseClass):
    def test_testCase2_WebFormWithPassword(self):
        log = self.getLogger()
        data = getTestData()
        try:
            pb.webForm(self).checkTheWebFormWithPassword(data['testcase2']['enterTheText'],data['testcase2']['enterThePassword'])
            pb.responseForm(self).submittedResponse()
        except Exception:
            log.exception("Test Case2 WebForm With Password got Failed")
            pytest.fail("Test Case2 WebForm With Password got Failed")
