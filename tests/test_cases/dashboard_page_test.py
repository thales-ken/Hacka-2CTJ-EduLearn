from test_cases.base_test import BaseTest
from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import LoginPage


class DashboardPageTest(BaseTest):
    def setUp(self):
        super().setUp()

        login_page = LoginPage(self.driver)
        login_page.login_with_valid_credentials()

    def print_locators(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.list_elements()
