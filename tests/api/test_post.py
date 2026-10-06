import requests


def test_create_user(api_headers):
    url = "https://reqres.in/api/users"
    payload = {
    "name": "morpheus",
    "job": "leader"}

    response = requests.post(url, json=payload, headers=api_headers)

    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"
    assert "id" in response.json()


def test_create_post(api_base_url):
    url = f"{api_base_url}/posts"
    payload = {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "Test Post"
    assert "id" in data
