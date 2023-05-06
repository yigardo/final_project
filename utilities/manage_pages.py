import test_cases.conftest as conf
from page_objects.web_objects.left_menu_page import LaftManunPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.server_admin_menu_page import ServerAdminManunPage
from page_objects.web_objects.server_admin_new_user import ServerAdminNewUser
from page_objects.web_objects.server_admin_page import ServerAdminPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage

web_login = None
web_main = None
web_upper_menu = None
web_left_menu = None
web_server_admin_page = None
web_server_admin_new_user = None
web_server_admin_menu_page = None

class ManagerPages:
    @staticmethod
    def init_web_pages():
        globals()["web_login"] = LoginPage(conf.driver)
        globals()["web_main"] = MainPage(conf.driver)
        globals()["web_upper_menu"] = UpperMenuPage(conf.driver)
        globals()["web_left_menu"] = LaftManunPage(conf.driver)
        globals()["web_server_admin_page"] = ServerAdminPage(conf.driver)
        globals()["web_server_admin_new_user"] = ServerAdminNewUser(conf.driver)
        globals()["web_server_admin_menu_page"] = ServerAdminManunPage(conf.driver)