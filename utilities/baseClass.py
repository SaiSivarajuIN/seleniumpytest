import inspect
import logging

import pytest
from datetime import datetime
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class baseClass:
    def getLogger(self):

        # get current date and time
        current_datetime = datetime.now().strftime("%d-%m-%Y")     # ("%d-%m-%Y:%H-%M-%S")
        # convert datetime obj to string
        str_current_datetime = str(current_datetime)

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../seleniumpytest/logFile/'+current_datetime+' .log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger


    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, keys):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(keys)

    def get_text(self, locator):
        by_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return by_element.text

