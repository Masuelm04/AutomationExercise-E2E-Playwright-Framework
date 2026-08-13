from pages.account_page import AccountPage
from pages.login_page import LoginPage

def test_logout(page, existing_user):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        existing_user["email"],
        existing_user["password"]
    )

    account_page = AccountPage(page)

    assert account_page.is_user_logged()

    account_page.logout()

    assert page.url.endswith("/login")