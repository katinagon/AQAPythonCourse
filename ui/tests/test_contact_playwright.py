import pytest

from components.playwright.solutions import SolutionsMenu
from pages.playwright.cicd import CICDPage
from pages.playwright.contact import ContactSalesPage
from pages.playwright.home import HomePage


@pytest.mark.playwright
@pytest.mark.ui
class TestGitContactPlaywright:
    def test_filling_form(self, page):
        home_page = HomePage(page)
        solution_menu = SolutionsMenu(page)
        cicd_page = CICDPage(page)
        contact_sales_page = ContactSalesPage(page)

        home_page.open()
        home_page.go_to_solutions()
        solution_menu.select_cicd()
        cicd_page.click_contact_sales()
        contact_sales_page.fill_form("John", "Pitt")
        contact_sales_page.get_field_value("John", "Pitt")
