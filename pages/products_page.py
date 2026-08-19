from playwright.sync_api import Page
from config.settings import BASE_URL
from pages.base_page import BasePage

class ProductsPage(BasePage):

    URL = f"{BASE_URL}/products"

    def __init__(self, page: Page):
        super().__init__(page)

        self.products_title = page.get_by_text("All Products")

        self.products_cards = page.locator(".product-image-wrapper")

        self.search_input = page.locator("#search_product")

        self.search_button = page.locator("#submit_search")

        self.searched_products_title = page.get_by_text("Searched Products")

        self.categories = page.locator("#accordian")

        self.category_title = page.locator(".features_items .title")

        self.brands = page.locator(".brands_products")

    def navigate(self):
        self.page.goto(self.URL)

    def is_products_page_visible(self) -> bool:
        return self.products_title.is_visible()

    def get_product_count(self) -> int:
        return self.products_cards.count()

    def get_product(self, index: int):
        return self.products_cards.nth(index)

    def get_product_name(self, index: int) -> str:
        product = self.products_cards.nth(index)

        return product.locator("p").inner_text()

    def click_view_product(self, index: int):
        product = self.products_cards.nth(index)

        product.get_by_text("View Product").click()

    def search_product(self, product_name: str):

        self.search_input.fill(product_name)

        self.search_button.click()

    def get_products_matching(self, text: str):

        return self.products_cards.filter(has_text=text)

    def select_category(self, category: str, subcategory: str):

        category_locator = self.categories.get_by_text(category, exact=True)

        category_locator.click()

        self.categories.get_by_text(subcategory, exact=True).click()

    def select_brand(self, brand: str):

        self.brands.get_by_text(brand).click()