from pages.login_page import LoginPage
from pages.account_page import AccountPage

def test_invalid_login(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login("test@example.com", "password123")

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
