from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DashboardPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = DashboardPageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located(element)
        )

    def list_elements(self):
        self.wait_for_element(self.locator.TEXT)
        print(self.driver.find_element(*self.locator.TEXT).text)
