from selenium.webdriver.common.by import By

from pages.base import BasePageSelenium


class ContactSalesPage(BasePageSelenium):
    FIRST_NAME_INPUT = (By.ID, "form-field-first_name")
    LAST_NAME_INPUT = (By.ID, "form-field-last_name")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, first_name: str, last_name: str):
        first_name_input = self.find(ContactSalesPage.FIRST_NAME_INPUT)
        last_name_input = self.find(ContactSalesPage.LAST_NAME_INPUT)

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)

    def get_field_value(self, first_name: str, last_name: str):
        first_name_input_text = self.find(
            ContactSalesPage.FIRST_NAME_INPUT
        ).get_attribute("value")
        last_name_input_text = self.find(
            ContactSalesPage.LAST_NAME_INPUT
        ).get_attribute("value")

        assert first_name_input_text == first_name
        assert last_name_input_text == last_name
