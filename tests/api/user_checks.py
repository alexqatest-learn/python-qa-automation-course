
def assert_valid_user(client, user_id: int):
    response = client.get_user(user_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert "name" in data
    assert "username" in data
    assert "email" in data