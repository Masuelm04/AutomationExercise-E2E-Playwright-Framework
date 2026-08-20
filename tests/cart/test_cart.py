from pages.cart_page import CartPage
from pages.products_page import ProductsPage

def test_add_product_to_cart(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    cart_page = CartPage(page)

    cart_page.navigate()

    assert cart_page.get_product_count() == 1