from selenium.webdriver.remote.webelement import WebElement


class Verifications:

    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, "verify Equals is failed, Actual: " + str(
            actual) + "is not Equals to Expected: " + str(
            expected)

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "Verify is Displayed failed, Element: " + elem.text + "is not Displayed"
