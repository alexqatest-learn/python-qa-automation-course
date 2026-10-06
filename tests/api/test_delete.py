import requests


def test_delete_user(api_headers):
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url, headers=api_headers)

    assert response.status_code == 204
    assert response.text == ""

def test_delete_post(api_base_url):
    url = f"{api_base_url}/posts/1"
    response = requests.delete(url)
    data = response.json()
    assert response.status_code == 200
    assert data == {}