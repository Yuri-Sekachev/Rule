import time

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestSuccessfulLogin:
    def test_successful_login(self, driver):
        login_page = LoginPage(driver, 'https://app.rule.io/v5/#/auth/login')
        home_page = HomePage(driver, 'https://app.rule.io')
        login_page.open()
        login_page.fill_email_field()
        login_page.fill_password_field()
        time.sleep(1)
        login_page.click_sign_in_button()
        assert home_page.bubble_button_is_displayed()
