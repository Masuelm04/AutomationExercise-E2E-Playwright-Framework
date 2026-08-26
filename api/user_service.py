from api.api_client import ApiClient

class UserService:

    def __init__(self):
        self.client = ApiClient()

    def create_user(self, user_data: dict):

        return self.client.post("/api/createAccount", data=user_data)

    def verify_login(self, email: str, password: str):

        return self.client.post("/api/verifyLogin", data={"email": email, "password": password})

    def delete_user(self, email: str, password: str):

        return self.client.delete("/api/deleteAccount", data={"email": email, "password": password})