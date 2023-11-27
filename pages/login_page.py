import time

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as Locators


class LoginPage(BasePage):
    def fill_email_field(self):
        self.element_is_visible(Locators.EMAIL_INPUT_FIELD).send_keys('yuri@rule.se')

    def fill_password_field(self):
        self.element_is_visible(Locators.PASSWORD_INPUT_FIELD).send_keys('Balagan1234')

    def click_sign_in_button(self):
        self.element_is_visible(Locators.SIGN_IN_BUTTON).click()

    def login(self):
        self.fill_email_field()
        self.fill_password_field()
        time.sleep(1)
        self.click_sign_in_button()
