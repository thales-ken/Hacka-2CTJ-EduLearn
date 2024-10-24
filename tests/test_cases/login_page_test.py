from test_cases.base_test import BaseTest
from page_objects.login_page import LoginPage


class LoginPageTest(BaseTest):
    def test_login_with_valid_user(self):
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_credentials()
        self.assertIn("logged-in-successfully", self.driver.current_url)
