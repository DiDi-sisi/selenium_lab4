import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()