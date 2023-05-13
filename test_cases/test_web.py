import allure

from utilities.common_ops import get_data, By, wait, For, read_csv
from workflows import web_flows
from workflows.web_flows import WebFlows
import pytest
import test_cases.conftest as conf


@pytest.mark.usefixtures("init_web_driver")
class Test_Web:
    #@allure.title('Test Verify Login Grafana')
    #@allure.description("this test verifies successful login")
    #def test_verify_login(self):
        #WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        #WebFlows.verify_grafana_title("Welcome to Grafana")

    #@allure.title("Test02: Verify Upper Menu Buttons")
    #@allure.description("this test verifies upper menu buttons are displayed")
    #def test_verify_upper_menu(self):
                   #WebFlows.verify_menu_buttons_flow()   # My Implementations
        #WebFlows.verify_menu_buttons_flow_smart_assertions()  #smart_assertions

    #@allure.title("Test03: Verify New User")
    #@allure.description("this test creates and verifies a new user")
    #def test_verify_new_user(self):
        #WebFlows.open_user()
        #WebFlows.create_user('avi', 'avii@gmail.com','avia', '1238')
        #WebFlows.create_user('yigardo', 'yigardo0@gmail.com', 'yigardoa', '1234')
        #WebFlows.verify_number_of_users(3)

    #@allure.title("Test04: Filtering Users")
    #@allure.description("this test filters users")
    #@pytest.mark.parametrize('search_value, expected_users', web_flows.testdata)
    #def test_csv(self, search_value, expected_users):
        #WebFlows.open_user()
        #WebFlows.search_user(search_value)
        #WebFlows.verify_number_of_users(int(expected_users))

    #@allure.title("Test05: Delete User")
    #@allure.description("this test verifies delete users")
    #def test_verify_delete_user(self):
        #WebFlows.open_user()
        #WebFlows.delete_user(By.USER, 'avia')  #OPTION 1
        #WebFlows.delete_user(By.USER, 'yigardoa')
                #WebFlows.delete_user(By.INDEX, 1) #OPTION 2
        #WebFlows.verify_number_of_users(1)

    #def teardown_method(self):
        #WebFlows.grafana_home(self)

    @allure.title("Test06: Visual testing")
    @allure.description("this test verifies visually users table")
    @pytest.mark.skipif(get_data('Execute_Applitools') == 'no', reason='run this test only on selenium 3.14.0 & appium 1.3.0')
    def test_visual_verify_delete_user(self):
        conf.eyes.open(self.drvier, 'Grafana', 'Grafana Testing User Table')
        WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        conf.driver.get('http://localhost:3000/admin/users')
        conf.eyes.check_window('Users Table')




