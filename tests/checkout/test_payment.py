import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage

@pytest.mark.checkout
@pytest.mark.critical
@pytest.mark.regression
def test_proceed_to_payment(page, existing_user, payment_data):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)

    login_page.navigate()

    login_page.login(
        existing_user["email"],
        existing_user["password"]
    )

    products_page.navigate()

    products_page.add_product_to_cart(
        "Blue Top"
    )

    products_page.view_cart()
    
    cart_page.proceed_to_checkout()

    checkout_page.enter_comment(
        "Automated checkout test"
    )

    checkout_page.place_order()

    expect(
        payment_page.name_on_card_input
    ).to_be_visible()

    payment_page.enter_payment_information(
        name_on_card=payment_data["name_on_card"],
        card_number=payment_data["card_number"],
        cvc=payment_data["cvc"],
        expiry_month=payment_data["expiry_month"],
        expiry_year=payment_data["expiry_year"],
    )

    expect(
        payment_page.name_on_card_input
    ).to_have_value(
        payment_data["name_on_card"]
    )