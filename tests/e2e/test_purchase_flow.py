import pytest
from conftest import existing_user, payment_data
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.payment_page import PaymentPage
from pages.order_confirmation_page import OrderConfirmationPage
from playwright.sync_api import expect
from utils.data_loader import load_json

CHECKOUT_CASES = load_json(
    "checkout_data.json"
)

@pytest.mark.checkout
@pytest.mark.e2e
@pytest.mark.critical
@pytest.mark.regression
@pytest.mark.parametrize(
    "checkout_case",
    CHECKOUT_CASES,
    ids=[
        case["product"]
        for case in CHECKOUT_CASES
    ]
)
def test_complete_purchase(page, existing_user, payment_data, checkout_case):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    confirmation_page = OrderConfirmationPage(page)

    login_page.navigate()

    login_page.login(
        existing_user["email"],
        existing_user["password"]
    )

    products_page.navigate()

    products_page.add_product_to_cart(
        checkout_case["product"]
    )

    products_page.view_cart()

    expect(
        cart_page.get_cart_product(checkout_case["product"])
    ).to_be_visible()

    cart_page.proceed_to_checkout()

    expect(
        checkout_page.get_order_product(checkout_case["product"])
    ).to_be_visible()

    checkout_page.enter_comment(
        checkout_case["comment"]
    )

    checkout_page.place_order()

    payment_page.enter_payment_information(
        payment_data["name_on_card"],
        payment_data["card_number"],
        payment_data["cvc"],
        payment_data["expiry_month"],
        payment_data["expiry_year"],
    )

    payment_page.pay_and_confirm()

    expect(
        confirmation_page.order_placed_message
    ).to_be_visible()

    download = (confirmation_page.download_invoice())

    assert download.suggested_filename