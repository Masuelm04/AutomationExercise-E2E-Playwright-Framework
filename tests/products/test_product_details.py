from playwright.sync_api import expect
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage

def test_open_product_details(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.click_view_product(0)

    product_details_page = ProductDetailsPage(page)

    expect(
        product_details_page.product_name
    ).to_have_text("Blue Top")