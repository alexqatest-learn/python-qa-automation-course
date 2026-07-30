from http.client import responses

import requests


def test_update_user(api_headers):
    url = "https://reqres.in/api/users/2"
    payload = {
    "name": "morpheus",
    "job": "zion resident"}

    response = requests.put(url, json=payload, headers=api_headers)

    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"
    assert "updatedAt" in response.json()
