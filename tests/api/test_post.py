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
