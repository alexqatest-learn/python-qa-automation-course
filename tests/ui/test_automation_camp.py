from playwright.sync_api import Page, expect

from tests.ui.page_object.automation_camp_page import (
    AutomationCampPage,
    FORMS_PAGE_URL,
)

import pytest

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_automation_camp_homepage_loads(page: Page):
    camp = AutomationCampPage(page)
    camp.open_main_page()
    expect(camp.forms_heading).to_be_visible()


def test_navigate_to_forms_page(page: Page):
    camp = AutomationCampPage(page)
    camp.open_main_page()
    camp.go_to_forms_via_link()
    expect(page).to_have_url(FORMS_PAGE_URL)


def test_fill_text_field_on_forms_page(page: Page):
    camp = AutomationCampPage(page)
    camp.open_forms_page()
    camp.fill_notes("Test User")
    expect(camp.notes).to_have_value("Test User")


def test_select_dropdown_option(page: Page):
    camp = AutomationCampPage(page)
    camp.open_forms_page()
    camp.select_tool("sel")
    expect(camp.select_tool_locator).to_have_value("sel")


def test_form_validation_shows_error(page: Page):
    camp = AutomationCampPage(page)
    camp.open_forms_page()
    camp.click_submit_form()
    expect(camp.invalid_city).to_be_visible()
    expect(camp.invalid_city).to_contain_text("Please provide a valid city.")