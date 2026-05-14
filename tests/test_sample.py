import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def scope_module():
    print("Выполнится один раз на файл")


@pytest.fixture(autouse=True)
def autouse_fix():
    print("Выполняется для каждого теста")


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://practice.expandtesting.com/login"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "submit-login")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

        btn = self.driver.find_element(*self.login_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn).perform()

        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()


def test_login_success():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="practice", password="SuperSecretPassword!")
    greeting = driver.find_element(By.ID, "username").text
    assert greeting == "Hi, practice!"


def test1(scope_module, fixture_for_all_tests):
    print("Тест 1")


@pytest.mark.xfail
def test2(scope_module, fixture_for_all_tests):
    print("Тест 2")


@pytest.mark.skip
def test3(scope_module, fixture_for_all_tests):
    print("Тест 3")


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (2, 2, 4),
        (5, 5, 10),
        (-1, 1, 0),
    ],
)
@pytest.mark.smoke
def test_sum(num1, num2, expected):
    assert num1 + num2 == expected
