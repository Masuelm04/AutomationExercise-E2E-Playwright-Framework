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

    def add_product_to_cart(self, product_name: str):

        product = self.product_cards.filter(has_text=product_name)

        product.get_by_text("Add to cart").click()