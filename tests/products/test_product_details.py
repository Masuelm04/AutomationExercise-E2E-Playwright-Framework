import pytest
from playwright.sync_api import expect
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage

@pytest.mark.products
@pytest.mark.regression
def test_open_product_details(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.click_view_product(0)

    product_details_page = ProductDetailsPage(page)

    expect(
        product_details_page.product_name
    ).to_have_text("Blue Top")

@pytest.mark.products
@pytest.mark.regression
def test_product_details_information(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.click_view_product(0)

    product_details_page = ProductDetailsPage(page)

    expect(
        product_details_page.product_name
    ).to_have_text("Blue Top")

    expect(
        product_details_page.product_price
    ).to_be_visible()

    expect(
        product_details_page.product_availability
    ).to_be_visible()

    expect(
        product_details_page.product_condition
    ).to_be_visible()

    expect(
        product_details_page.product_brand
    ).to_be_visible()

@pytest.mark.products
@pytest.mark.regression
def test_open_searched_product_details(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.search_product("Blue Top")

    products_page.click_view_product(0)

    product_details_page = ProductDetailsPage(page)

    expect(
        product_details_page.product_name
    ).to_have_text("Blue Top")