from components.base import BaseComponentPlaywright


class SolutionsMenu(BaseComponentPlaywright):
    CICD = 'a[href="https://github.com/solutions/use-case/ci-cd"]'

    def __init__(self, page):
        super().__init__(page)

    def select_cicd(self):
        cicd = self.page.locator(SolutionsMenu.CICD)

        cicd.click()
