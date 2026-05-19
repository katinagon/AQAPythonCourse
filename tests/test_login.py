from playwright.sync_api import expect
from selenium.webdriver.common.by import By

from pages.playwright.login import LoginPagePlaywright
from pages.selenium.login import LoginPageSelenium


def test_login_success_with_selenium(driver):
    login_page = LoginPageSelenium(driver)
    login_page.open()
    login_page.login(username="practice", password="SuperSecretPassword!")
    greeting = driver.find_element(By.ID, "username").text
    assert greeting == "Hi, practice!"


def test_login_success_with_playwright(page):
    login_page = LoginPagePlaywright(page)
    login_page.open()
    login_page.login(username="practice", password="SuperSecretPassword!")
    expect(page.locator("#username")).to_have_text("Hi, practice!")
