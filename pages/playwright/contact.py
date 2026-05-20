from playwright.sync_api import expect

from pages.base import BasePagePlaywright


class ContactSalesPage(BasePagePlaywright):
    FIRST_NAME_INPUT = "#form-field-first_name"
    LAST_NAME_INPUT = "#form-field-last_name"

    def __init__(self, page):
        super().__init__(page)

    def fill_form(self, first_name: str, last_name: str):
        first_name_input = self.page.locator(ContactSalesPage.FIRST_NAME_INPUT)
        last_name_input = self.page.locator(ContactSalesPage.LAST_NAME_INPUT)

        first_name_input.fill(first_name)
        last_name_input.fill(last_name)

    def get_field_value(self, first_name: str, last_name: str):
        first_name_input = self.page.locator(ContactSalesPage.FIRST_NAME_INPUT)
        last_name_input = self.page.locator(ContactSalesPage.LAST_NAME_INPUT)

        expect(first_name_input).to_have_value(first_name)
        expect(last_name_input).to_have_value(last_name)
