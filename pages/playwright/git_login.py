import os

from playwright.sync_api import expect

from pages.base import BasePagePlaywright

print("DEBUG _LOGIN:", os.getenv("GH_LOGIN"))
print("DEBUG AVATAR:", f'button[data-login="{os.getenv("GH_LOGIN")}"]')


class GitLoginPage(BasePagePlaywright):
    _BASE_URL = os.getenv("BASE_URL")
    _LOGIN = os.getenv("GH_LOGIN")
    _PASSWORD = os.getenv("GH_PASSWORD")
    _USERNAME = os.getenv("GH_USERNAME")

    LOGIN_INPUT = "#login_field"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = 'input[name="commit"]'
    DASHBOARD_TEXT = '//span[text()="Dashboard"]'
    HOME_TEXT = '//h2[text()="Home"]'
    AVATAR = f'button[data-login="{_LOGIN}"]'
    LOGIN_TEXT = f'div[title="{_LOGIN}"]'
    NAME_TEXT = f'div[title="{_USERNAME}"]'
    USERNAME_PASSWORD_ERROR_TEXT = ".flash-error .js-flash-alert"

    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self._BASE_URL}/login"

    def open(self):
        self.page.goto(self.url)

    def fill_login_page(self, login, password):
        login_input = self.page.locator(GitLoginPage.LOGIN_INPUT)
        password_input = self.page.locator(GitLoginPage.PASSWORD_INPUT)

        login_input.fill(login)
        password_input.fill(password)

    def click_login_button(self):
        login_btn = self.page.locator(GitLoginPage.LOGIN_BUTTON)

        login_btn.click()

    def click_avatar_button(self):
        avatar = self.page.locator(GitLoginPage.AVATAR)

        avatar.hover()
        self.page.wait_for_timeout(500)
        avatar.click()

    def check_home_page(self):
        dashboard_element = self.page.locator(GitLoginPage.DASHBOARD_TEXT)
        home_element = self.page.locator(GitLoginPage.HOME_TEXT)

        expect(dashboard_element).to_be_visible()
        expect(dashboard_element).to_have_text("Dashboard")
        expect(home_element).to_be_visible()
        expect(home_element).to_have_text("Home")

    def check_user_info(self):
        login_element = self.page.locator(GitLoginPage.LOGIN_TEXT)
        name_element = self.page.locator(GitLoginPage.NAME_TEXT)

        expect(login_element).to_be_visible()
        expect(login_element).to_have_text(self._LOGIN)
        expect(name_element).to_be_visible()
        expect(name_element).to_have_text(self._USERNAME)

    def check_incorrect_username_or_password_text(self):
        error_message = self.page.locator(GitLoginPage.USERNAME_PASSWORD_ERROR_TEXT)

        expect(error_message).to_be_visible()
        expect(error_message).to_have_text("Incorrect username or password.")
