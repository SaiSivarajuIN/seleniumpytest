from pages.webForm import webForm
from pages.formResponse import response


class pageObjects():
    def __init__(self, driver):
        self.driver = driver

    def webForm(self):
        return webForm(self.driver)

    def responseForm(self):
        return response(self.driver)
