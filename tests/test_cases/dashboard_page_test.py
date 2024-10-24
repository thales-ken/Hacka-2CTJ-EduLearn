from test_cases.base_test import BaseTest
from page_objects.dashboard_page import DashboardPage


class DashboardPageTest(BaseTest):


    def print_locators(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.list_elements()