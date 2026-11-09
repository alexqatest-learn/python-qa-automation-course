from playwright.sync_api import Page

BASE_URL = "https://play1.automationcamp.ir"
MAIN_PAGE_URL = f"{BASE_URL}/index.html"
FORMS_PAGE_URL = f"{BASE_URL}/forms.html"


class AutomationCampPage:
    def __init__(self, page: Page):
        self.page = page

    def open_main_page(self) -> None:
        self.page.goto(MAIN_PAGE_URL)

    def open_forms_page(self) -> None:
        self.page.goto(FORMS_PAGE_URL)

    def go_to_forms_via_link(self) -> None:
        self.page.locator('a[href="forms.html"]').click()

    def fill_notes(self, text: str) -> None:
        self.page.locator("#notes").fill(text)

    def select_tool(self, value: str) -> None:
        self.page.locator("#select_tool").select_option(value)

    def click_submit_form(self) -> None:
        self.page.get_by_role("button", name="Submit Form").click()

    @property
    def forms_heading(self):
        return self.page.get_by_role("heading", name="Forms")

    @property
    def notes(self):
        return self.page.locator("#notes")

    @property
    def select_tool_locator(self):
        return self.page.locator("#select_tool")

    @property
    def invalid_city(self):
        return self.page.locator("#invalid_city")