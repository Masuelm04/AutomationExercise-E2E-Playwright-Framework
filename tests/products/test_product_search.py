import pytest
from playwright.sync_api import expect
from pages.products_page import ProductsPage
from utils.data_loader import load_json

def test_search_product(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.search_product("Blue Top")

    assert products_page.searched_products_title.is_visible()

PRODUCTS = load_json("products.json")

@pytest.mark.parametrize(
    "product",
    PRODUCTS,
    ids=[
        product["name"]
        for product in PRODUCTS
    ]
)

def test_search_results_contain_product(page, product):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.search_product(product["name"])

    matching_products = products_page.get_products_matching(product["name"]).first

    expect(matching_products).to_be_visible()
    
    # assert matching_products.count() > 0

def test_search_product_returns_no_results(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    search_term = "XYZProductDoesNotExist123"

    products_page.search_product(search_term)

    matching_products = products_page.get_products_matching(
            search_term
        )

    assert matching_products.count() == 0