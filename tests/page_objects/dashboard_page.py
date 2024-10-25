import time

from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DashboardPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = DashboardPageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(element)
        )

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(
            ec.url_contains(url)
        )

    def wait_dashboard_loading(self):
        if "Seu professor ainda não postou nenhum vídeo. " \
           "Entre em contato com nosso suporte ao aluno!" in self.locator.TEXT:
            print("Erro")
        else:
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(self.locator.VIDEO_PLAYER)
            )

    def list_elements(self):
        self.wait_for_element(self.locator.TITLE)
        print("\n" + self.driver.find_element(*self.locator.TITLE).text)
        self.wait_for_element(self.locator.VIDEO_PLAYER)
        print("\n" + self.driver.find_element(*self.locator.VIDEO_PLAYER).get_attribute("src"))
        self.wait_for_element(self.locator.TEXT)
        print("\n" + self.driver.find_element(*self.locator.TEXT).text)
        self.wait_for_element(self.locator.CURRENT_VIDEO)
        print("\n" + self.driver.find_element(*self.locator.CURRENT_VIDEO).text)

    def click_logout_button(self):
        self.wait_for_url("/dashboard")
        self.wait_dashboard_loading()
        hamburger_button = self.driver.find_elements(*self.locator.NAVBAR_BUTTON)
        if hamburger_button and hamburger_button[0].is_displayed():
            hamburger_button[0].click()
        self.wait_for_element(self.locator.LOGOUT_BUTTON)
        self.driver.find_element(*self.locator.LOGOUT_BUTTON).click()
        self.wait_for_url('/')
