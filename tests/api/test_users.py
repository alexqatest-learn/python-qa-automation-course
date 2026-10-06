import pytest
import requests



def test_get_user_by_id(api_base_url):
    url = f"{api_base_url}/users/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data
