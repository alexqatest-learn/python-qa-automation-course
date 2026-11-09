import pytest
from tests.api.user_checks import assert_valid_user

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_get_user_not_found(jp_client):
    non_existent_user_id = 999
    response = jp_client.get_user(non_existent_user_id)
    assert response.status_code == 404


@pytest.mark.parametrize("expected_id", [1, 2, 3])
def test_get_user_by_id_parametrized(jp_client, user_id_factory, expected_id):
    user_id = user_id_factory(expected_id)
    assert_valid_user(jp_client, user_id)
