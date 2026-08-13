import pytest
from playwright.sync_api import Page, sync_playwright
from config.settings import HEADLESS
from utils.data_generator import generate_email
from test_data.users import TEST_USER_DATA
from test_data.users import EXISTING_USER

@pytest.fixture
def page():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=HEADLESS)

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