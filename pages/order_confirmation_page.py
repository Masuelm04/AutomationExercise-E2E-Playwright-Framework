from playwright.sync_api import Page
from pages.base_page import BasePage

class OrderConfirmationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.order_placed_message = page.get_by_text("Order Placed!")

        self.download_invoice_button = page.get_by_text("Download Invoice")

    def is_order_placed(self) -> bool:
        return self.order_placed_message.is_visible()

    def download_invoice(self):

        with self.page.expect_download() as download_info:

            self.download_invoice_button.click()

        return download_info.value