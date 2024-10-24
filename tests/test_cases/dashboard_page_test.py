import time

from test_cases.base_test import BaseTest
from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


class DashboardPageTest(BaseTest):
    def setUp(self):
        super().setUp()
        home_page = HomePage(self.driver)
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_credentials()

    def test_check_content(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.list_elements()

    def test_logout_button(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_logout_button()
        self.assertIn("/home", self.driver.current_url)
