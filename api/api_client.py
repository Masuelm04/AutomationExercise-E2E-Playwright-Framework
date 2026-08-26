import requests
from config.settings import BASE_URL

class ApiClient:

    API_BASE_URL = BASE_URL

    def get(self, endpoint: str):
        return requests.get(f"{self.API_BASE_URL}{endpoint}", verify=False)

    def post(self, endpoint: str, data=None):
        return requests.post(f"{self.API_BASE_URL}{endpoint}", data=data, verify=False)

    def put(self, endpoint: str, data=None):
        return requests.put(f"{self.API_BASE_URL}{endpoint}", data=data, verify=False)

    def delete(self, endpoint: str, data=None):
        return requests.delete(f"{self.API_BASE_URL}{endpoint}", data=data, verify=False)