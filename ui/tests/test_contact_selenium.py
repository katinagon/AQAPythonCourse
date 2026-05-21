import pytest

from components.selenium.solutions import SolutionsMenu
from pages.selenium.cicd import CICDPage
from pages.selenium.contact import ContactSalesPage
from pages.selenium.home import HomePage


@pytest.mark.selenium
@pytest.mark.ui
class TestGitContactSelenium:
    @pytest.mark.parametrize(
        "first_name, last_name",
        [
            ("John", "Pitt"),
            ("Mary", "Sue"),
        ],
    )
    def test_filling_form(self, driver, first_name, last_name):
        home_page = HomePage(driver)
        solution_menu = SolutionsMenu(driver)
        cicd_page = CICDPage(driver)
        contact_sales_page = ContactSalesPage(driver)

        home_page.open()
        home_page.go_to_solutions()
        solution_menu.select_cicd()
        cicd_page.click_contact_sales()
        contact_sales_page.fill_form(first_name, last_name)
        contact_sales_page.get_field_value(first_name, last_name)
