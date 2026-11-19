import requests


class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str):
        url = f"{self.base_url}/{path}"
        return requests.get(url)

    def post(self, path: str, json: dict | None = None, headers: dict | None = None):
        url = f"{self.base_url}/{path}"
        return requests.post(url, json=json, headers=headers)

    def put(self, path: str, json: dict | None = None, headers: dict | None = None):
        url = f"{self.base_url}/{path}"
        return requests.put(url, json=json, headers=headers)

    def delete(self, path: str, headers: dict | None = None):
        url = f"{self.base_url}/{path}"
        return requests.delete(url, headers=headers)