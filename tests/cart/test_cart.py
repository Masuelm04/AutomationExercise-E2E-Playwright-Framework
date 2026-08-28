import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.products_page import ProductsPage

@pytest.mark.cart
@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.regression
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

@pytest.mark.cart
@pytest.mark.critical
@pytest.mark.regression
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

    products_page.view_cart()

    cart_page = CartPage(page)

    assert cart_page.get_product_count() == 2

@pytest.mark.cart
@pytest.mark.regression
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

@pytest.mark.cart
@pytest.mark.regression
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

@pytest.mark.cart
@pytest.mark.regression
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

@pytest.mark.cart
@pytest.mark.regression
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

@pytest.mark.cart
@pytest.mark.e2e
@pytest.mark.critical
@pytest.mark.regression
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

@pytest.mark.cart
@pytest.mark.regression
def test_product_price_is_visible(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    expect(cart_page.get_product_price("Blue Top")).to_be_visible()

@pytest.mark.cart
@pytest.mark.regression
def test_product_subtotal_is_correct(page):

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

    price = cart_page.get_product_price_value(
        "Blue Top"
    )

    quantity = cart_page.get_product_quantity_value(
        "Blue Top"
    )

    subtotal = cart_page.get_product_total_value(
        "Blue Top"
    )

    assert subtotal == price * quantity
@pytest.mark.cart
@pytest.mark.regression
def test_cart_persistence(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    expect(
        cart_page.get_cart_product("Blue Top")
    ).to_be_visible()

    products_page.navigate()

    cart_page.navigate()

    expect(
        cart_page.get_cart_product("Blue Top")
    ).to_be_visible()