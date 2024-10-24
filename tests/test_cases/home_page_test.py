from test_cases.base_test import BaseTest
from page_objects.home_page import HomePage


class HomePageTest(BaseTest):
    def test_login_button(self):
        home_page = HomePage(self.driver)
        home_page.click_login_button()
        self.assertIn("/login", self.driver.current_url)

    def test_register_button(self):
        home_page = HomePage(self.driver)
        home_page.click_register_button()
        self.assertIn("/register", self.driver.current_url)
