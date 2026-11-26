import pytest
from pages.login_page import LoginPage
from pages.checkboxes_page import CheckboxesPage
from pages.status_codes_page import StatusCodesPage

BASE_URL = "https://the-internet.herokuapp.com"

# --- Данные для тестов Логина ---
login_test_data = [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", "valid_login"),
    ("tomsmith", "WrongPassword", "Your password is invalid!", "invalid_password"),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!", "nonexistent_user"),
    ("", "", "Your username is invalid!", "empty_fields"),
    ("tomsmith", "", "Your password is invalid!", "empty_password"),
]

@pytest.mark.parametrize("username, password, expected_text, test_id", login_test_data, ids=[x[3] for x in login_test_data])
def test_login(browser, username, password, expected_text, test_id):
    page = LoginPage(browser)
    page.open(f"{BASE_URL}/login").login(username, password)
    assert expected_text in page.get_flash_message()

# --- Данные для тестов Checkboxes ---
checkbox_test_data = [
    (True, True, "check_first"),
    (False, False, "uncheck_first"),
]

@pytest.mark.parametrize("action_state, expected_state, test_id", checkbox_test_data, ids=[x[2] for x in checkbox_test_data])
def test_checkboxes(browser, action_state, expected_state, test_id):
    page = CheckboxesPage(browser)
    page.open(f"{BASE_URL}/checkboxes")
    
    if action_state:
        page.check_first_checkbox()
    else:
        page.uncheck_first_checkbox()
        
    assert page.is_first_checkbox_selected() is expected_state

# --- Данные для тестов Status Codes ---
status_codes_data = [
    ("200", "200", "code_200"),
    ("404", "404", "code_404"),
    ("500", "500", "code_500"),
]

@pytest.mark.parametrize("code, expected_code_text, test_id", status_codes_data, ids=[x[2] for x in status_codes_data])
def test_status_codes(browser, code, expected_code_text, test_id):
    page = StatusCodesPage(browser)
    page.open(f"{BASE_URL}/status_codes").click_code_link(code)
    assert expected_code_text in page.get_page_text()