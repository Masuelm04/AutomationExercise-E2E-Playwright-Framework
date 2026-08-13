from pages.account_information_page import AccountInformationPage
from pages.signup_page import SignupPage
from test_data.users import TEST_USER_REGISTRATION_DATA
from utils.data_generator import generate_email
from pages.account_page import AccountPage

def test_user_registration(page):

    signup_page = SignupPage(page)

    signup_page.navigate()

    email = generate_email()

    signup_page.signup(
        TEST_USER_REGISTRATION_DATA["name"],
        email
    )

    account_information_page = AccountInformationPage(page)

    account_information_page.fill_account_information(
        password=TEST_USER_REGISTRATION_DATA["password"],
        first_name=TEST_USER_REGISTRATION_DATA["first_name"],
        last_name=TEST_USER_REGISTRATION_DATA["last_name"],
        address=TEST_USER_REGISTRATION_DATA["address"],
        country=TEST_USER_REGISTRATION_DATA["country"],
        state=TEST_USER_REGISTRATION_DATA["state"],
        city=TEST_USER_REGISTRATION_DATA["city"],
        zipcode=TEST_USER_REGISTRATION_DATA["zipcode"],
        mobile_number=TEST_USER_REGISTRATION_DATA["mobile_number"],
    )

    account_information_page.create_account()

    assert account_information_page.is_account_created()

    account_information_page.continue_to_account()

    account_page = AccountPage(page)

    assert account_page.is_user_logged()