from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = HomePageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located(element)
        )

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(
            ec.url_contains(url)
        )

    def click_login_button(self):
        self.wait_for_element(self.locator.LOGIN_BUTTON)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        self.wait_for_url("/login")
        return HomePage(self.driver)

    def click_register_button(self):
        self.wait_for_element(self.locator.REGISTER_BUTTON)
        self.driver.find_element(*self.locator.REGISTER_BUTTON).click()
        self.wait_for_url("/register")
        return HomePage(self.driver)
