from playwright.sync_api import Page, expect

def test_automation_camp_homepage_loads(page: Page):
    page.goto("https://play1.automationcamp.ir/index.html")
    expect(page.get_by_role("heading", name="Forms")).to_be_visible()

def test_navigate_to_forms_page(page: Page):
    page.goto("https://play1.automationcamp.ir/index.html")
    page.locator('a[href="forms.html"]').click()
    expect(page).to_have_url("https://play1.automationcamp.ir/forms.html")

def test_fill_text_field_on_forms_page(page: Page):
    page.goto("https://play1.automationcamp.ir/forms.html")
    page.locator('#notes').fill("Test User")
    expect(page.locator('#notes')).to_have_value("Test User")

def test_select_dropdown_option(page: Page):
    page.goto("https://play1.automationcamp.ir/forms.html")
    page.locator('#select_tool').select_option("sel")
    expect(page.locator('#select_tool')).to_have_value("sel")

def test_form_validation_shows_error(page: Page):
    page.goto("https://play1.automationcamp.ir/forms.html")
    page.get_by_role("button", name="Submit Form").click()
    expect(page.locator('#invalid_city')).to_be_visible()
    expect(page.locator('#invalid_city')).to_contain_text("Please provide a valid city.")