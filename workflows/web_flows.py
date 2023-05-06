import page_objects.web_objects.server_admin_page as page
import page_objects.web_objects.main_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import For, wait
class WebFlows:
    @staticmethod
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_user_name(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())
        UiActions.click(page.web_login.get_skip())
    @staticmethod
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXISTS, page_objects.web_objects.main_page.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_assert(elems)
    @staticmethod
    def verify_menu_buttons_flow():
        elems = [page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_displayed(elems)

    @staticmethod
    def open_user():
        elem1 = page.web_left_menu.get_server_admin()
        elem2 = page.web_server_admin_menu_page.get_user()
        UiActions.mouse_hover(elem1, elem2)

    @staticmethod
    def create_user(name, email, user, password):
        UiActions.click(page.web_server_admin_page.get_new_user())
        UiActions.update_text(page.web_server_admin_new_user.get_name(), name)
        UiActions.update_text(page.web_server_admin_new_user.get_email(), email)
        UiActions.update_text(page.web_server_admin_new_user.get_user_name(), user)
        UiActions.update_text(page.web_server_admin_new_user.get_password(), password)
        UiActions.click(page.web_server_admin_new_user.get_create_user())

    @staticmethod
    def verify_number_of_users(number):
        if number > 0:
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.server_admin_page.users_list)
            Verifications.verify_number_of_elements(page.web_server_admin_page.get_users_list(), number)

    @staticmethod
    def delete_user(by, value):
        if by == 'user':
            UiActions.click(page.web_server_admin_page.get_user_by_user_name(value))
        elif by == 'index':
            UiActions.click(page.web_server_admin_page.get_user_by_index(value))
        UiActions.click(page.web_server_admin_page.get_delete_user())
        UiActions.click(page.web_server_admin_page.get_confirm_delete())