from playwright.sync_api import Page

LOGIN_URL = "https://the-internet.herokuapp.com/login"
SECURE_URL = "https://the-internet.herokuapp.com/secure"


class TheInternetLoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(LOGIN_URL)

    def login(self, username, password):
        self.page.locator("#username").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("button[type='submit']").click()