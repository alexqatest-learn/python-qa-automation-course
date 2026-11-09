from tests.ui.page_object.the_internet_login_page import TheInternetLoginPage, SECURE_URL
from playwright.sync_api import Page, expect

import pytest

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_successful_login(page: Page):
    login_page = TheInternetLoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(page.locator("#flash")).to_be_visible()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page).to_have_url(SECURE_URL)