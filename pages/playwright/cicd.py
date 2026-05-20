from pages.base import BasePagePlaywright


class CICDPage(BasePagePlaywright):
    CONTACT_BUTTON = '(//span[text()="Contact sales"])[1]'

    def __init__(self, page):
        super().__init__(page)

    def click_contact_sales(self):
        contact_btn = self.page.locator(CICDPage.CONTACT_BUTTON)

        contact_btn.click()
