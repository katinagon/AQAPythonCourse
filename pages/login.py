from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


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
