import pytest
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from api.user_service import UserService

@pytest.mark.api_ui
@pytest.mark.authentication
@pytest.mark.regression
def test_user_authentication_ui_and_api(page, api_user):

    login_page = LoginPage(page)
    account_page = AccountPage(page)

    login_page.navigate()

    login_page.login(
        api_user["email"],
        api_user["password"]
    )

    assert account_page.is_user_logged()

    service = UserService()

    response = service.verify_login(
        api_user["email"],
        api_user["password"]
    )

    body = response.json()

    assert body["responseCode"] == 200