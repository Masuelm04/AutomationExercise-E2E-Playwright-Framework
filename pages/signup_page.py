from playwright.sync_api import Page
from config.settings import BASE_URL
from pages.base_page import BasePage

class SignupPage(BasePage):

    URL = f"{BASE_URL}/login"

    def __init__(self, page):

        super().__init__(page)

        self.name_input = page.locator('[data-qa="signup-name"]')

        self.email_input = page.locator('[data-qa="signup-email"]')

        self.signup_button = page.locator('[data-qa="signup-button"]')

        self.existing_email_error = page.get_by_text("Email Address already exist!")

    def navigate(self):
        self.page.goto(self.URL)

    def signup(self, name: str, email: str):

        self.name_input.fill(name)
        self.email_input.fill(email)

        self.signup_button.click()

    def is_existing_email_error_visible(self) -> bool:
        return self.existing_email_error.is_visible()