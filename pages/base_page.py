from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        return self

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        self.find_element(locator).click()
        return self

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator):
        return self.find_element(locator).text