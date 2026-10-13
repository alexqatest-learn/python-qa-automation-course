


def assert_valid_post(client, post_id: int):
    response = client.get_post(post_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data    
    assert "body" in data    
    assert "userId" in data     
    
