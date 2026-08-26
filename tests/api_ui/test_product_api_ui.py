from pages.products_page import ProductsPage
from api.product_service import ProductService

def test_product_search_api_ui(page):

    search_term = "Top"

    product_service = ProductService()

    api_response = product_service.search_product(search_term)

    api_data = api_response.json()

    assert api_data["responseCode"] == 200

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.search_product(search_term)

    api_products = api_data["products"]

    assert len(api_products) > 0

    for product in api_products:

        product_name = product["name"]

        assert (products_page.get_products_matching(product_name).count() > 0)