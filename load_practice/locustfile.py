from locust import HttpUser, task, between


class JsonPlaceholderUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_post(self):
        response = self.client.get("/posts/1", name="GetPost")
        if response.status_code != 200:
            response.failure(f"status {response.status_code}")

    @task(3)
    def get_posts_list(self):
        response = self.client.get("/posts", name="GetPostsList")
        if response.status_code != 200:
            response.failure(f"status {response.status_code}")