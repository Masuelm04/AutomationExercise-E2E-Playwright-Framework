from playwright.sync_api import Page
from pages.base_page import BasePage

class AccountInformationPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.mr_radio = page.locator("#id_gender1")
        self.mrs_radio = page.locator("#id_gender2")

        self.password_input = page.locator('[data-qa="password"]')

        self.days_select = page.locator('[data-qa="days"]')

        self.months_select = page.locator('[data-qa="months"]')

        self.years_select = page.locator('[data-qa="years"]')

        self.first_name_input = page.locator('[data-qa="first_name"]')

        self.last_name_input = page.locator('[data-qa="last_name"]')

        self.company_input = page.locator('[data-qa="company"]')

        self.address_input = page.locator('[data-qa="address"]')

        self.country_select = page.locator('[data-qa="country"]')

        self.state_input = page.locator('[data-qa="state"]')

        self.city_input = page.locator('[data-qa="city"]')

        self.zipcode_input = page.locator('[data-qa="zipcode"]')

        self.mobile_number_input = page.locator('[data-qa="mobile_number"]')

        self.create_account_button = page.locator('[data-qa="create-account"]')

        self.account_created_message = page.get_by_text("Account Created!")

        self.continue_button = page.locator('[data-qa="continue-button"]')

    def fill_account_information(
        self,
        password: str,
        first_name: str,
        last_name: str,
        address: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile_number: str,
    ):
        self.mr_radio.check()

        self.password_input.fill(password)

        self.days_select.select_option("10")
        self.months_select.select_option("5")
        self.years_select.select_option("1995")

        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)

        self.company_input.fill("Automation Company")

        self.address_input.fill(address)

        self.country_select.select_option(
            label=country
        )

        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_number_input.fill(mobile_number)

    def create_account(self):
        self.create_account_button.click()

    def is_account_created(self) -> bool:
        return self.account_created_message.is_visible()

    def continue_to_account(self):
        self.continue_button.click()