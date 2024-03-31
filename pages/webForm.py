from selenium.webdriver.common.by import By
from utilities.baseClass import baseClass as BC, baseClass
from pages.formResponse import response

class webForm(baseClass):
    def __init__(self, driver):
        self.driver = driver

    inputText_lc = (By.XPATH, "//input[@id='my-text-id']")
    passTxt_lc = (By.XPATH,"//input[@name='my-password']")
    submit_btn = (By.XPATH, "//button[@type='submit']")

    def enterText(self, enterTheText):
        return BC.do_send_keys(self, webForm.inputText_lc, enterTheText)

    def enterPassword(self, enterPassTxt):
        return BC.do_send_keys(self, webForm.passTxt_lc, enterPassTxt)

    def clickOnSumbit(self):
        BC.do_click(self, webForm.submit_btn)

    def checkTheWebForm(self, enterTheText):
        log = self.getLogger()
        log.info("Enter the 'Hello'")
        webForm.enterText(self, enterTheText)
        log.info("Click on Submit button")
        webForm.clickOnSumbit(self)


    def checkTheWebFormWithPassword(self, enterTheText, enterThePassword):
        log = self.getLogger()
        log.info("Enter the 'Hello' : "+enterTheText)
        webForm.enterText(self, enterTheText)
        log.info("Enter the 'Password' : "+enterThePassword)
        webForm.enterPassword(self, enterThePassword)
        log.info("Click on Submit button")
        webForm.clickOnSumbit(self)