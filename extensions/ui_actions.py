from selenium.webdriver.remote.webelement import WebElement

from test_cases.conftest import action


class UiActions:
    @staticmethod
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    def update_text(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        action.move_to_element(elem1).move_to_element(elem2).clikc().perform()

    @staticmethod
    def right_click(elem: WebElement):
        action.context_clikc(elem).perform()

    @staticmethod
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    def clear(elem: WebElement):
        elem.clear()