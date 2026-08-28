import pytest
from conftest import existing_user
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from playwright.sync_api import expect

@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.regression
def test_proceed_to_checkout(page, existing_user):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        existing_user["email"],
        existing_user["password"]
    )

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()

    cart_page = CartPage(page)

    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)

    expect(checkout_page.delivery_address).to_be_visible()

@pytest.mark.checkout
@pytest.mark.critical
@pytest.mark.regression
def test_checkout_displays_correct_delivery_and_billing_addresses(page, existing_user):

    login_page = LoginPage(page)
    
    login_page.navigate()
    
    login_page.login(
        existing_user["email"],
        existing_user["password"]
    )
    
    products_page = ProductsPage(page)
    
    products_page.navigate()
    
    products_page.add_product_to_cart(
        "Blue Top"
    )
    
    products_page.view_cart()
    
    cart_page = CartPage(page)
    
    cart_page.proceed_to_checkout()
    
    checkout_page = CheckoutPage(page)

    delivery_address = (checkout_page.get_delivery_address_text())

    assert existing_user["first_name"] in delivery_address
    assert existing_user["last_name"] in delivery_address
    assert existing_user["address"] in delivery_address

    billing_address = (checkout_page.get_billing_address_text())

    assert existing_user["first_name"] in billing_address
    assert existing_user["last_name"] in billing_address
    assert existing_user["address"] in billing_address