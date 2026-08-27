import pytest
from playwright.sync_api import Page, sync_playwright
from config.settings import HEADLESS
from utils.data_generator import generate_email
from test_data.users import TEST_USER_DATA
from test_data.users import EXISTING_USER
from test_data.payment import PAYMENT_DATA
from api.user_service import UserService
from utils.user_payload import build_create_user_payload

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=[
            "chromium",
            "firefox",
            "webkit",
        ],
        help="Browser used for test execution",
    )

@pytest.fixture
def browser_name(request):

    return request.config.getoption(
        "--browser"
    )

@pytest.fixture
def page(browser_name):

    with sync_playwright() as playwright:

        browser_type = getattr(playwright, browser_name)

        browser = browser_type.launch(headless=False)

        page = browser.new_page()

        yield page

        browser.close()

@pytest.fixture
def new_user():
    user = TEST_USER_DATA.copy()

    user["email"] = generate_email()

    return user

@pytest.fixture
def existing_user():

    return EXISTING_USER.copy()

@pytest.fixture
def payment_data():

    return PAYMENT_DATA.copy()

@pytest.fixture
def api_user(new_user):

    service = UserService()

    payload = build_create_user_payload(new_user)

    response = service.create_user(payload)

    body = response.json()

    assert body["responseCode"] == 201

    yield new_user

    service.delete_user(
        new_user["email"],
        new_user["password"]
    )