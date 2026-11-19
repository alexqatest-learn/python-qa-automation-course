import pytest
import requests

pytestmark = pytest.mark.api


def test_delete_user(api_headers):
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url, headers=api_headers)

    assert response.status_code == 204
    assert response.text == ""


def test_delete_post(jp_client):
    response = jp_client.delete_post(1)
    assert response.status_code == 200
    assert response.json() == {}