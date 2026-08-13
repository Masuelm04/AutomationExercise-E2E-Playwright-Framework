from pages.account_page import AccountPage
from pages.login_page import LoginPage
from test_data.users import TEST_USER

def test_logout(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        TEST_USER["email"],
        TEST_USER["password"]
    )

    account_page = AccountPage(page)

    assert account_page.is_user_logged()

    account_page.logout()

    assert page.url.endswith("/login")