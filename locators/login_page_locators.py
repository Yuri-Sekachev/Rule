from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, 'input.rule-input-element[type="password"]')
    LOG_IN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
