from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, 'input.field[type="email"]')
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, 'input.field[type="password"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[ng-click="loginForm.doLogin()"]')
