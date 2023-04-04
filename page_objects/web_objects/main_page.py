from selenium.webdriver.common.by import By

main_titel = (By.CLASS_NAME, 'css-1aanzv4')

class MainPage():

    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        return self.driver.find_element(main_titel[0], main_titel[1])