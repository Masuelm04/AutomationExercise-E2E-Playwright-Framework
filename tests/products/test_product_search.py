from pages.products_page import ProductsPage

def test_search_product(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.search_product("Blue Top")

    assert products_page.searched_products_title.is_visible()

def test_search_results_contain_product(page):

    products_page = ProductsPage(page)

    products_page.navigate()

    products_page.search_product("Blue Top")

    matching_products = products_page.get_products_matching(
        "Blue Top"
    )

    assert matching_products.count() > 0