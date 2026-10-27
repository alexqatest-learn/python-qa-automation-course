import pytest
import requests



def test_get_user_by_id(jp_client):
    user_id = 1
    response = jp_client.get_user(user_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert "name" in data
    assert "username" in data
    assert "email" in data
