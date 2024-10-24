from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME = (By.ID, 'formEmail')
    PASSWORD = (By.ID, 'formPassword')
    SUBMIT = (By.XPATH, '//*[@id="root"]/div/div/div/form/button')
    ERROR_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-danger")]')
