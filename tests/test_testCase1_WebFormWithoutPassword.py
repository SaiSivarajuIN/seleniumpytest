import pytest
from pages.pageObjects import pageObjects as pb
from utilities.baseClass import baseClass


class TestCase1_webForm(baseClass):
    def test_testCase1_WebFormWithPassword(self):
        log = self.getLogger()
        try:
            pb.webForm(self).checkTheWebForm("HI")
            pb.responseForm(self).submittedResponse()
        except Exception:
            log.exception("Test Case1 WebForm Without Password got Failed")
            pytest.fail("Test Case1 WebForm Without Password got Failed")
