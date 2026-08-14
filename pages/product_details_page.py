from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductDetailsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.product_name = page.locator(".product-information h2")

        self.product_price = page.locator(".product-information span span")

        self.product_category = page.get_by_text("Category:")

    def get_product_name(self) -> str:
        return self.product_name.inner_text()

    def get_product_price(self) -> str:
        return self.product_price.inner_text()