from clients.http_client import HttpClient


class BaseApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.http = HttpClient(base_url)

    def _get(self, path: str):
        return self.http.get(path)

