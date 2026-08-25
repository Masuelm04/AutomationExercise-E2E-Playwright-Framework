import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from utils.data_loader import load_json

LOGIN_CASES = load_json(
    "login_cases.json"
)

@pytest.mark.parametrize(
    "login_case",
    LOGIN_CASES,
    ids=[
        case["case"]
        for case in LOGIN_CASES
    ]
)

def test_invalid_login(page, login_case):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(login_case["email"], login_case["password"])

    assert login_page.is_login_error_visible()

def test_login_with_empty_credentials(page):

    login_page = LoginPage(page)
    
    login_page.navigate()

    login_page.login("","")

    assert login_page.email_input.is_visible()
    assert login_page.password_input.is_visible()

def test_user_login(page, existing_user):

    login_page = LoginPage(page)
        
    login_page.navigate()

    login_page.login(
        existing_user["email"],
        existing_user["password"]
    )

    account_page = AccountPage(page)

    assert account_page.is_user_logged()
