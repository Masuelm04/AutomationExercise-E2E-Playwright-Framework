from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.delivery_address = page.locator("#address_delivery")

        self.billing_address = page.locator("#address_invoice")

        self.order_products = page.locator("#cart_info tbody tr")

        self.comment_input = page.locator("textarea[name='message']")

        self.place_order_button = page.get_by_role("link", name="Place Order")

    def get_delivery_address_text(self) -> str:
        return self.delivery_address.inner_text()

    def get_billing_address_text(self) -> str:
        return self.billing_address.inner_text()

    def get_order_product(self, product_name: str):
        return self.order_products.filter(has_text=product_name)

    def get_order_product_price(self, product_name: str):
        product = self.get_order_product(product_name)

        return product.locator(".cart_price")

    def get_order_product_quantity(self, product_name: str):
        product = self.get_order_product(product_name)

        return product.locator(".cart_quantity")