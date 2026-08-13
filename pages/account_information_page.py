from playwright.sync_api import Page
from pages.base_page import BasePage

class AccountInformationPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.password_input = page.locator('[data-qa="password"]')

        self.first_name_input = page.locator('[data-qa="first_name"]')

        self.last_name_input = page.locator('[data-qa="last_name"]')

        self.address_input = page.locator('[data-qa="address"]')

        self.create_account_button = page.locator('[data-qa="create-account"]')
