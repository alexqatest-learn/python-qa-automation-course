from clients.http_client import HttpClient


class BaseApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.http = HttpClient(base_url)

    def _get(self, path: str):
        return self.http.get(path)

    def _post(self, path: str, json: dict | None = None, headers: dict | None = None):
        return self.http.post(path, json=json, headers=headers)

    def _put(self, path: str, json: dict | None = None, headers: dict | None = None):
        return self.http.put(path, json=json, headers=headers)

    def _delete(self, path: str, headers: dict | None = None):
        return self.http.delete(path, headers=headers)

