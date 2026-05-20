import os

import pytest

from pages.playwright.git_login import GitLoginPage

has_credentials = bool(os.getenv("GH_LOGIN") and os.getenv("GH_PASSWORD"))


@pytest.mark.playwright
@pytest.mark.ui
class TestGitLoginPlaywright:
    @pytest.mark.skipif(
        not has_credentials,
        reason="Тест пропущен: отсутствуют GH_LOGIN или GH_PASSWORD в .env",
    )
    def test_successful_authorization(self, page):
        login_page = GitLoginPage(page)
        login_page.open()
        login_page.fill_login_page(os.getenv("GH_LOGIN"), os.getenv("GH_PASSWORD"))
        login_page.click_login_button()
        login_page.check_home_page()
        login_page.click_avatar_button()
        login_page.check_user_info()

    @pytest.mark.parametrize(
        "login, password",
        [
            ("login", os.getenv("GH_PASSWORD")),
            ("логин", "пароль"),
            ("12345", os.getenv("GH_PASSWORD")),
            ("№*%(?", "№*%(?"),
        ],
    )
    def test_authorization_with_incorrect_login_password(self, page, login, password):
        login_page = GitLoginPage(page)
        login_page.open()
        login_page.fill_login_page(login, password)
        login_page.click_login_button()
        login_page.check_incorrect_username_or_password_text()
