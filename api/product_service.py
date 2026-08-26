from api.api_client import ApiClient

class ProductService:

    def __init__(self):
        self.client = ApiClient()

    def get_products(self):

        return self.client.get("/api/productsList")

    def search_product(self, search_term: str):

        return self.client.post("/api/searchProduct", data={"search_product": search_term})