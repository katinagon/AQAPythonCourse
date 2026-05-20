from selenium.webdriver.common.by import By

from pages.base import BasePageSelenium


class CICDPage(BasePageSelenium):
    CONTACT_BUTTON = (By.XPATH, '(//span[text()="Contact sales"])[1]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_contact_sales(self):
        contact_btn = self.find(CICDPage.CONTACT_BUTTON)

        contact_btn.click()
