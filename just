*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://example.com

*** Keywords ***
Open Incognito Browser
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --incognito
    Create WebDriver    Chrome    chrome_options=${options}
    Go To    ${URL}

*** Test Cases ***
Open Chrome In Incognito Mode
    Open Incognito Browser
