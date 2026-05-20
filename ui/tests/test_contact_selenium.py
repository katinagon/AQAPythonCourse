import pytest

from components.selenium.solutions import SolutionsMenu
from pages.selenium.cicd import CICDPage
from pages.selenium.contact import ContactSalesPage
from pages.selenium.home import HomePage


@pytest.mark.selenium
@pytest.mark.ui
class TestGitContactSelenium:
    def test_filling_form(self, driver):
        home_page = HomePage(driver)
        solution_menu = SolutionsMenu(driver)
        cicd_page = CICDPage(driver)
        contact_sales_page = ContactSalesPage(driver)

        home_page.open()
        home_page.go_to_solutions()
        solution_menu.select_cicd()
        cicd_page.click_contact_sales()
        contact_sales_page.fill_form("John", "Pitt")
        contact_sales_page.get_field_value("John", "Pitt")
