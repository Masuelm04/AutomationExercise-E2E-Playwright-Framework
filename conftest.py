import pytest
from playwright.sync_api import Page, sync_playwright
from config.settings import HEADLESS

@pytest.fixture
def page():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=HEADLESS)

        page = browser.new_page()

        yield page

        browser.close()