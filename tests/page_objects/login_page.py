from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located(element)
        )

    def enter_username(self, username):
        self.wait_for_element(self.locator.USERNAME)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.locator.PASSWORD)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.wait_for_element(self.locator.SUBMIT)
        self.driver.find_element(*self.locator.SUBMIT).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        WebDriverWait(self.driver, 10).until(ec.url_contains("/dashboard"))

    def login_with_valid_credentials(self):
        self.login("usuario@aluno.com", "123456")
        return LoginPage(self.driver)

    def login_with_invalid_credentials(self):
        self.login("usuario@errado.com", "111111")
        self.wait_for_element(self.locator.ERROR_MESSAGE)
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text

