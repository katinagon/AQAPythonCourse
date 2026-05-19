from playwright.sync_api import Page


class BasePageSelenium:
    def __init__(self, driver):
        self.driver = driver


class BasePagePlaywright:
    def __init__(self, page: Page):
        self.page = page
