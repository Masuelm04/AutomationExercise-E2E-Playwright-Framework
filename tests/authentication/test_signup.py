import pytest
from pages.account_information_page import AccountInformationPage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage

@pytest.mark.authentication
@pytest.mark.critical
@pytest.mark.regression
def test_user_registration(page, new_user):

    signup_page = SignupPage(page)

    signup_page.navigate()

    signup_page.signup(
        new_user["name"],
        new_user["email"]
    )

    account_information_page = AccountInformationPage(page)

    account_information_page.fill_account_information(
        password=new_user["password"],
        first_name=new_user["first_name"],
        last_name=new_user["last_name"],
        address=new_user["address"],
        country=new_user["country"],
        state=new_user["state"],
        city=new_user["city"],
        zipcode=new_user["zipcode"],
        mobile_number=new_user["mobile_number"],
    )

    account_information_page.create_account()

    assert account_information_page.is_account_created()

    account_information_page.continue_to_account()

    account_page = AccountPage(page)

    assert account_page.is_user_logged()

@pytest.mark.authentication
@pytest.mark.regression
def test_registration_with_existing_email(page, existing_user):

    signup_page = SignupPage(page)

    signup_page.navigate()

    signup_page.signup(
        existing_user["name"],
        existing_user["email"]
    )

    assert signup_page.is_existing_email_error_visible()