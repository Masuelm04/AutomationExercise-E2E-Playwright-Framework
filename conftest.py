import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from config.settings import (HEADLESS, DEFAULT_TIMEOUT, SCREENSHOTS_DIR, TRACES_DIR)
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )

@pytest.fixture
def browser_name(request):

    return request.config.getoption(
        "--browser"
    )

@pytest.fixture
def page(request, browser_name):

    with sync_playwright() as playwright:

        browser_type = getattr(playwright, browser_name)

        browser = browser_type.launch(headless=HEADLESS)

        page = browser.new_page()

        page.set_default_timeout(DEFAULT_TIMEOUT)

        Path(SCREENSHOTS_DIR).mkdir(parents=True, exist_ok=True)

        Path(TRACES_DIR).mkdir(parents=True, exist_ok=True)

        page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield page

        test_failed = (hasattr(request.node, "rep_call")and request.node.rep_call.failed)

        if test_failed:

            test_name = request.node.name

            screenshot_path = (Path(SCREENSHOTS_DIR) / f"{test_name}_{browser_name}.png")

            trace_path = (Path(TRACES_DIR) / f"{test_name}_{browser_name}.zip")

            page.screenshot(path=str(screenshot_path), full_page=True)

            page.context.tracing.stop(path=str(trace_path))

        else:

            page.context.tracing.stop()

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