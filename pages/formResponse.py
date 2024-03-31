import pytest
from selenium.webdriver.common.by import By
from utilities.baseClass import baseClass as BC, baseClass


class response(baseClass):
    def __init__(self, driver):
        self.driver = driver

    message_lc = (By.ID, "message")

    def submittedResponse(self):
        log = self.getLogger()
        message = BC.get_text(self, response.message_lc)
        assert message == "Received!"
        log.info("the message was:" + message)
