from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.products_page import ProductsPage

def test_add_product_to_cart(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    product = cart_page.get_cart_product("Blue Top")

    expect(product).to_be_visible()

def test_add_multiple_products_to_cart(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.continue_shopping()

    products_page.add_product_to_cart(
        "Men Tshirt"
    )

    cart_page = CartPage(page)

    cart_page.navigate()

    assert cart_page.get_product_count() == 2

    from playwright.sync_api import expect


def test_product_quantity_in_cart(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    cart_page = CartPage(page)

    products_page.view_cart()

    quantity = cart_page.get_product_quantity(
        "Blue Top"
    )

    expect(quantity).to_have_text("1")

def test_add_same_product_twice(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.continue_shopping()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    quantity = cart_page.get_product_quantity(
        "Blue Top"
    )

    expect(quantity).to_have_text("2")

def test_remove_product_from_cart(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    expect(cart_page.get_cart_product("Blue Top")).to_be_visible()

    cart_page.remove_product(
        "Blue Top"
    )

    expect(cart_page.get_cart_product("Blue Top")).to_have_count(0)

def test_remove_all_products_from_cart(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.continue_shopping()

    products_page.add_product_to_cart(
        "Men Tshirt"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    cart_page.remove_product(
        "Blue Top"
    )

    cart_page.remove_product(
        "Men Tshirt"
    )

    expect(
        cart_page.cart_products
    ).to_have_count(0)

def test_product_to_cart_e2e(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    expect(products_page.products_title).to_be_visible()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    product = cart_page.get_cart_product(
        "Blue Top"
    )

    expect(product).to_be_visible()

    quantity = cart_page.get_product_quantity(
        "Blue Top"
    )

    expect(quantity).to_have_text("1")