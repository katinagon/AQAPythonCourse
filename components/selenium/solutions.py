from selenium.webdriver.common.by import By

from components.base import BaseComponentSelenium


class SolutionsMenu(BaseComponentSelenium):
    CICD = (By.CSS_SELECTOR, 'a[href="https://github.com/solutions/use-case/ci-cd"]')

    def __init__(self, driver):
        super().__init__(driver)

    def select_cicd(self):
        cicd = self.find(SolutionsMenu.CICD)

        cicd.click()
