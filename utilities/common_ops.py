import csv

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse('C:/Automation/test_Automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text



def wait(for_element, elem):

    if for_element == 'element_exists':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located((elem[0], elem[1])))

    def read_csv(file_name):
        data = []
        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.insert(len(data), row)
            return data


class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'

class By:
    USER = 'user'
    INDEX = 'index'