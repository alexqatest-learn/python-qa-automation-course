import requests


def test_get_single_user(api_headers):
    url = "https://reqres.in/api/users/2"
    response = requests.get(url, headers=api_headers)

    assert response.status_code == 200

    data = response.json()
    assert data["data"]["id"] == 2
    assert data["data"]["first_name"] == "Janet"
    assert "email" in data["data"]