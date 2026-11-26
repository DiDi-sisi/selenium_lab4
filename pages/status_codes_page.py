from selenium.webdriver.common.by import By
from .base_page import BasePage

class StatusCodesPage(BasePage):
    PAGE_TEXT = (By.CSS_SELECTOR, "div.example p")

    def click_code_link(self, code):
        locator = (By.LINK_TEXT, str(code))
        self.click(locator)
        return self

    def get_page_text(self):
        return self.get_text(self.PAGE_TEXT)