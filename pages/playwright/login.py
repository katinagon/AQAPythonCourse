from pages.base import BasePagePlaywright


class LoginPagePlaywright(BasePagePlaywright):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://practice.expandtesting.com/login"
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#submit-login"

    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
