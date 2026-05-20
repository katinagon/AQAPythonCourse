import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePageSelenium


class GitLoginPage(BasePageSelenium):
    _BASE_URL = os.getenv("BASE_URL")
    _LOGIN = os.getenv("GH_LOGIN")
    _PASSWORD = os.getenv("GH_PASSWORD")
    _USERNAME = os.getenv("GH_USERNAME")

    LOGIN_INPUT = (By.ID, "login_field")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[name="commit"]')
    DASHBOARD_TEXT = (By.XPATH, '//span[text()="Dashboard"]')
    HOME_TEXT = (By.XPATH, '//h2[text()="Home"]')
    AVATAR = (By.CSS_SELECTOR, 'img[data-testid="github-avatar"]')
    LOGIN_TEXT = (By.CSS_SELECTOR, f'div[title="{_LOGIN}"]')
    NAME_TEXT = (By.CSS_SELECTOR, f'div[title="{_USERNAME}"]')
    USERNAME_PASSWORD_ERROR_TEXT = (By.CSS_SELECTOR, ".flash-error .js-flash-alert")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{self._BASE_URL}/login"
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def open(self):
        self.driver.get(self.url)

    def fill_login_page(self, login, password):
        login_input = self.find(self.LOGIN_INPUT)
        password_input = self.find(self.PASSWORD_INPUT)

        login_input.send_keys(login)
        password_input.send_keys(password)

    def click_login_button(self):
        login_btn = self.find(self.LOGIN_BUTTON)
        login_btn.click()

    def click_avatar_button(self):
        avatar = self.find(self.AVATAR)

        avatar.click()

    def check_home_page(self):
        dashboard_element = self.find(self.DASHBOARD_TEXT)
        home_element = self.find(self.HOME_TEXT)

        assert dashboard_element.is_displayed()
        assert home_element.is_displayed()
        assert dashboard_element.text == "Dashboard", "Некорректный текст Dashboard"
        assert home_element.text == "Home", "Некорректный текст Home"

    def check_user_info(self):
        login_element = self.find(self.LOGIN_TEXT)
        name_element = self.find(self.NAME_TEXT)

        assert login_element.is_displayed()
        assert name_element.is_displayed()
        assert (
            login_element.text == self._LOGIN
        ), "Некорректный логин в всплывающем меню"
        assert (
            name_element.text == self._USERNAME
        ), "Некорректное имя в всплывающем меню"

    def check_incorrect_username_or_password_text(self):
        error_message = self.find(self.USERNAME_PASSWORD_ERROR_TEXT)

        assert error_message.is_displayed()
        assert (
            error_message.text == "Incorrect username or password."
        ), "Некорректное сообщение об ошибке"
