from selenium.webdriver.common.by import By

from pages.base import BasePageSelenium


class HomePage(BasePageSelenium):
    SOLUTIONS = (By.XPATH, '//button[text()="Solutions"]')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BasePageSelenium._BASE_URL)

    def go_to_solutions(self):
        solutions = self.find(HomePage.SOLUTIONS)

        solutions.click()
