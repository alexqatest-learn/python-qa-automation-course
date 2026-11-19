import pytest
import requests

pytestmark = pytest.mark.api


def test_update_user(api_headers):
    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "morpheus",
        "job": "zion resident",
    }

    response = requests.put(url, json=payload, headers=api_headers)

    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"
    assert "updatedAt" in response.json()


def test_update_post(jp_client):
    payload = {
        "title": "Updated Post",
        "body": "This is an updated post",
        "userId": 1,
    }
    response = jp_client.update_post(1, payload)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Updated Post"
    assert "id" in data