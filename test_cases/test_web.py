from utilities.common_ops import get_data, By, wait, For
from workflows.web_flows import WebFlows
import pytest


@pytest.mark.usefixtures("init_web_driver")
class Test_Web:
    def test_verify_login(self):
        WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        WebFlows.verify_grafana_title("Welcome to Grafana")
    def test_verify_upper_menu(self):
        #WebFlows.verify_menu_buttons_flow()                 # My Implementations
        WebFlows.verify_menu_buttons_flow_smart_assertions()  #smart_assertions
    def test_verify_new_user(self):
        WebFlows.open_user()
        WebFlows.create_user('yigardo', 'yigardo0@gmail.com','yigardoa', '1234')
        WebFlows.create_user('avi', 'avii@gmail.com','avia', '1238')
        WebFlows.verify_number_of_users(3)

    def test_verify_delete_user(self):
        WebFlows.delete_user(By.USER, 'yigardoa') #OPTION 1
        WebFlows.delete_user(By.INDEX, 1) #OPTION 2
        WebFlows.verify_number_of_users(1)



