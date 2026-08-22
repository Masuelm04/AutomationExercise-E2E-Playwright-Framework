from conftest import existing_user
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from playwright.sync_api import expect

def test_order_summary(page, existing_user):

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

    cart_price = (
        cart_page.get_product_price_value("Blue Top")
    )
    
    cart_page.proceed_to_checkout()
    
    checkout_page = CheckoutPage(page)

    checkout_price_text = (
        checkout_page.get_order_product_price("Blue Top").inner_text()
    )

    checkout_price = int(
        checkout_price_text.replace("Rs. ", "")
    )

    product = checkout_page.get_order_product(
        "Blue Top"
    )

    assert checkout_price == cart_price

    expect(product).to_be_visible()

    expect(checkout_page.get_order_product_price("Blue Top")).to_be_visible()