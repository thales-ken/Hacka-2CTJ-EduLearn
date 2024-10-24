from selenium.webdriver.common.by import By


class HomePageLocators(object):
    REGISTER_BUTTON = (By.XPATH, '//a[@href="/register"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@href="/login"]')


class LoginPageLocators(object):
    USERNAME = (By.ID, 'formEmail')
    PASSWORD = (By.ID, 'formPassword')
    SUBMIT = (By.XPATH, '//*[@id="root"]/div/div/div/form/button')
    ERROR_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-danger")]')


class DashboardPageLocators(object):
    TITLE = (By.XPATH, '//div[@class="card-title h5"]')
    VIDEO_PLAYER = (By.XPATH, '//iframe[@title="YouTube video player"]')
    TEXT = (By.XPATH, '//p[@class]')
    CURRENT_VIDEO = (By.XPATH,
                     '//div[@class="card"]//table[@class="table table-striped table-bordered table-hover"]//button[contains(@class, "active")]')
    NAVBAR_BUTTON = (By.CLASS_NAME, 'navbar-toggler collapsed')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="#" and text()="Sair"]')
