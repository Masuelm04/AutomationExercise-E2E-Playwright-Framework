from playwright.sync_api import Page
from config.settings import BASE_URL
from pages.base_page import BasePage

class CartPage(BasePage):

    URL = f"{BASE_URL}/view_cart"

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_products = page.locator(
            "#cart_info_table tbody tr"
        )

    def navigate(self):
        self.page.goto(self.URL)

    def get_product_count(self) -> int:
        return self.cart_products.count()

    def get_cart_product(self, product_name: str):

        return self.cart_products.filter(has_text=product_name)

    def get_product_quantity(self, product_name: str):

        product = self.get_cart_product(product_name)

        return product.locator(".cart_quantity button")

    def remove_product(self, product_name: str):

        product = self.get_cart_product(product_name)

        product.locator(".cart_quantity_delete" ).click()