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

    def get_cart_product(self, product_name: str):

        return self.cart_products.filter(has_text=product_name)

    def get_product_price(self, product_name: str):

        product = self.get_cart_product(product_name)

        return product.locator(".cart_price")

    def get_product_quantity(self, product_name: str):

        product = self.get_cart_product(product_name)

        return product.locator( ".cart_quantity button")

    def get_product_total(self, product_name: str):

        product = self.get_cart_product(product_name)

        return product.locator(".cart_total_price")

    def get_product_price_value(self, product_name: str) -> int:

        price_text = (self.get_product_price(product_name).inner_text())

        return int(price_text.replace("Rs. ", ""))

    def get_product_quantity_value(self, product_name: str) -> int:

        quantity_text = (self.get_product_quantity(product_name).inner_text())

        return int(quantity_text)

    def get_product_total_value(self, product_name: str) -> int:

        total_text = (self.get_product_total(product_name).inner_text())

        return int(total_text.replace("Rs. ", ""))