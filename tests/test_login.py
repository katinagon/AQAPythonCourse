from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login import LoginPage


def test_login_success():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="practice", password="SuperSecretPassword!")
    greeting = driver.find_element(By.ID, "username").text
    assert greeting == "Hi, practice!"
