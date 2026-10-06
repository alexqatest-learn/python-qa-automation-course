import pytest


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

