from datetime import datetime

import pytest
from selenium import webdriver
from utilities.configurations import *


conf = getConfig()
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()

    # headless
    options.add_argument("--headless=new")

    # connected to remote browser
    # driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)

    # local driver connection
    driver = webdriver.Chrome(options=options)

    # url
    driver.get(conf['url']['website'])
    driver.maximize_window() # maximize window
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


# report with failed screenshot
@pytest.hookimpl(hookwrapper=True) #@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    # get current date and time
    current_datetime = datetime.now().strftime("%d-%m-%Y:%H-%M-%S")
    # convert datetime obj to string
    str_current_datetime = str(current_datetime)
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = ("../reports/screenshots/" + report.nodeid.replace("::", "_") + " : "
                         + current_datetime + ".png")
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

