from playwright.sync_api import Page
from pages.base_page import BasePage
from config.settings import BASE_URL

class LoginPage(BasePage):

    URL = f"{BASE_URL}/login"

    def __init__(self, page):

        super().__init__(page)

        self.email_input = page.locator('[data-qa="login-email"]')

        self.password_input = page.locator('[data-qa="login-password"]')

        self.login_button = page.locator('[data-qa="login-button"]')

        self.login_error = page.get_by_text("Your email or password is incorrect!")

    def navigate(self):

        self.page.goto(self.URL)

    def login(self, email: str, password: str):

        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def is_login_error_visible(self) -> bool:
        return self.login_error.is_visible()