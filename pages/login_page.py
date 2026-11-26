from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)