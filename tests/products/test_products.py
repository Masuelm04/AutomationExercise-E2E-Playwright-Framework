from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage

def test_product_page_is_displayed(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    assert products_page.is_products_page_visible()

def test_products_are_displayed(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    product_count = products_page.get_product_count()

    assert product_count > 0

def test_view_product_details(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.click_view_product(0)

    products_details_page = ProductDetailsPage(page)

    assert products_details_page.product_name.is_visible()
    assert products_details_page.product_price.is_visible()