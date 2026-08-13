from playwright.sync_api import Page
from config.settings import BASE_URL
from pages.base_page import BasePage

class AccountPage(BasePage):

    URL = BASE_URL

    def __init__(self, page: Page):
        super().__init__(page)

        self.logged_in_user = page.get_by_text("Logged in as")

        self.logout_link = page.get_by_text("Logout")

    def is_user_logged(self) -> bool:
        return self.logged_in_user.is_visible()

    def logout(self):
        self.logout_link.click()