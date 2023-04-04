import time

import pytest
import requests
import selenium.webdriver
import selenium.webdriver.chrome.service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.manage_pages import ManagerPages

driver = None
web_driver = "Chrome"
action = None

@pytest.fixture(scope="class")
def init_web_driver(request):
    globals()["driver"] = get_web_driver()
    driver = globals()["driver"]
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://localhost:3000/")
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagerPages.init_web_pages()
    yield
    time.sleep(3)
    driver.quit()

def get_web_driver():
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
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver

def get_firefox():
    ff_driver=selenium.webdriver.Firefox(GeckoDriverManager().install())
    return ff_driver

def get_edge():
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver