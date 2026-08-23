from playwright.sync_api import Page
from pages.base_page import BasePage

class PaymentPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.name_on_card_input = page.locator('[data-qa="name-on-card"]')

        self.card_number_input = page.locator('[data-qa="card-number"]')

        self.cvc_input = page.locator('[data-qa="cvc"]')

        self.expiry_month_input = page.locator('[data-qa="expiry-month"]')

        self.expiry_year_input = page.locator('[data-qa="expiry-year"]')

        self.pay_button = page.locator('[data-qa="pay-button"]')

    def enter_payment_information(self, name_on_card: str, card_number: str, cvc: str, expiry_month: str, expiry_year: str,):
        self.name_on_card_input.fill(name_on_card)

        self.card_number_input.fill(card_number )

        self.cvc_input.fill(cvc)

        self.expiry_month_input.fill(expiry_month)

        self.expiry_year_input.fill(expiry_year)

    def pay_and_confirm(self):
        self.pay_button.click()