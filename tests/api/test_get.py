import pytest
import requests

def test_get_post_by_id(api_base_url):
    url = f"{api_base_url}/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data    
    assert "body" in data    
    assert "userId" in data     


def test_get_all_posts(api_base_url):
    url = f"{api_base_url}/posts"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]

def test_get_non_existent_post(api_base_url):
    url = f"{api_base_url}/posts/999"
    response = requests.get(url)
    assert response.status_code == 404


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id_parametrized(api_base_url, post_id):
    url = f"{api_base_url}/posts/{post_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data    
    assert "body" in data    
    assert "userId" in data     
