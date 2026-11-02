import pytest
from clients.json_placeholder import JsonPlaceholderClient, LoggingJsonPlaceholderClient


@pytest.fixture
def api_headers():
    print("\n[Setup] Preparing headers and token for API test...")
    api_key = "free_user_3HDWdmc5qUH7NWShCtfUtjvSZ8p"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Content-Type": "application/json",
        "x-api-key": api_key,
    }

    yield headers

    print("\n[Teardown] API test execution finished. Cleaning up.")


@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def jp_client():
    return JsonPlaceholderClient("https://jsonplaceholder.typicode.com")

@pytest.fixture
def jp_logging_client():
    return LoggingJsonPlaceholderClient("https://jsonplaceholder.typicode.com")

@pytest.fixture
def user_id_factory():
    used_ids = []

    def factory(user_id=1):
        used_ids.append(user_id)
        return user_id

    yield factory

    print(f"\n[Teardown] Released user ids: {used_ids}")
    used_ids.clear()