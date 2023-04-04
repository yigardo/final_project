import test_cases
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage

web_login = None
web_main = None

class ManagerPages:
    @staticmethod
    def init_web_pages():
        globals()["web_login"] = LoginPage(test_cases.conftest.driver)
        globals()["web_main"] = MainPage(test_cases.conftest.driver)