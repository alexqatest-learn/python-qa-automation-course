import requests


class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str):
        url = f"{self.base_url}/{path}"
        response = requests.get(url)
        return response

    