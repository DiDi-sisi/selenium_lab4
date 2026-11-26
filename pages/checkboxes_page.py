from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckboxesPage(BasePage):
    CHECKBOXES = (By.TAG_NAME, "input")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, "input:first-child")
    
    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def check_first_checkbox(self):
        checkbox = self.find_element(self.FIRST_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_first_checkbox(self):
        checkbox = self.find_element(self.FIRST_CHECKBOX)
        if checkbox.is_selected():
            checkbox.click()
            
    def is_first_checkbox_selected(self):
        return self.find_element(self.FIRST_CHECKBOX).is_selected()