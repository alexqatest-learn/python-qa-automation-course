import pytest
from tests.api.post_checks import assert_valid_post


pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_get_post_by_id(jp_client):
    assert_valid_post(jp_client, 1)


def test_get_all_posts(jp_client):
    response = jp_client.get_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]


def test_get_non_existent_post(jp_client):
    response = jp_client.get_post(999)
    assert response.status_code == 404


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id_parametrized(jp_client, post_id):
    assert_valid_post(jp_client, post_id)


def test_get_post_by_id_logging_client(jp_logging_client):
    assert_valid_post(jp_logging_client, 1)
