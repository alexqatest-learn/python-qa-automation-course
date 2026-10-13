from clients.base_api_client import BaseApiClient

class JsonPlaceholderClient(BaseApiClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)


    def get_post(self, post_id: int):
        return self._get(f"posts/{post_id}")


class LoggingJsonPlaceholderClient(JsonPlaceholderClient):
    
    def get_post(self, post_id: int):
        print(f"GET /posts/{post_id}")
        return super().get_post(post_id)



