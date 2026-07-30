from playwright.sync_api import Page, expect


def test_successful_login(page: Page):

    page.goto("https://the-internet.herokuapp.com/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")

    page.locator("button[type='submit']").click()

    expect(page.locator("#flash")).to_be_visible()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")