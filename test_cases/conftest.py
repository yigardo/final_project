import time

import allure
import pytest
import requests
import selenium.webdriver
import selenium.webdriver.chrome.service
from applitools.selenium import Eyes
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagerPages

driver = None
#web_driver = "Chrome"
action = None
eyes = Eyes()   #Applitools



@pytest.fixture(scope="class")
def init_web_driver(request):
    if get_data('Execute_Applitools').lower() == 'yes':
        globals()["driver"] = get_web_driver()
    else:
        edriver = get_web_driver()
        globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data("Url"))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagerPages.init_web_pages()

    if get_data('Execute_Applitools').lower() == 'yes':
        eyes.api_key = get_data('Appitools_key')
    yield
    driver.quit()
    if get_data('Execute_Applitools').lower() == 'yes':
        eyes.close()    #applitools
        eyes.abort()    #applitools



def get_web_driver():
    web_driver = get_data("Browser")
    if web_driver.lower() == "chrome":
      driver = get_chrome()
    elif web_driver.lower() == "firefox":
        driver = get_firefox()
    elif web_driver.lower() == "edge":
        driver = get_edge()
    else:
        driver = None
        raise Exception("Wrong input, Unrecognized Browser")
    return driver


def get_chrome():
    #srv = selenium.Service(ChromeDriverManager().install()) #selenium 04
    #chrome_driver = selenium.webdriver.chrome(service=srv) #selenium 04
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install()) #selenuim 04
    return chrome_driver


def get_firefox():
    ff_driver = selenium.webdriver.Firefox(GeckoDriverManager().install())
    return ff_driver


def get_edge():
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver


def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()["driver"] is not None:
            image = get_data('ScreenshotPath') + 'screen_' + str(get_time_stamp()) + '.png'
            globals()["driver"].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)