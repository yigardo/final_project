from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:

    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, "verify Equals is failed, Actual: " + str(
            actual) + "is not Equals to Expected: " + str(
            expected)

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "Verify is Displayed failed, Element: " + elem.text + "is not Displayed"

# Verify menu Buttons  Using smart-assertions
    @staticmethod
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    # Verify menu Buttons  Using My Implementations
    @staticmethod
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print("Soft Displayed failed, Elements which have failed: " + str(failed_elems))
            raise AssertionError("Soft Displayed Failed")

    @staticmethod
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, 'Number of elements in list: ' + str(len(elems)) + 'does not match expected :' + str(size)