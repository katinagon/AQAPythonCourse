from playwright.sync_api import Page

from pages.base import BasePagePlaywright


class HomePage(BasePagePlaywright):
    SOLUTIONS = "Solutions"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.page.goto(BasePagePlaywright._BASE_URL)

    def go_to_solutions(self):
        solutions = self.page.get_by_text(HomePage.SOLUTIONS, exact=True)

        solutions.click()
