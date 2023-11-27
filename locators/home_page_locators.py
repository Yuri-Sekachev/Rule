from selenium.webdriver.common.by import By


class HomePageLocators:
    bubble_button = (By.XPATH, '//span[@class="icon icon-bubble"]')
    dashboard_button = (By.CSS_SELECTOR, '.margin-right-10.line-icon.line-icon-grid')
    new_rule_icon = (By.CSS_SELECTOR, '.line-icon.line-icon-rocket.margin-right-5')
