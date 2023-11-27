from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators as Locators


class HomePage(BasePage):
    def bubble_button_is_displayed(self):
        return self.element_is_visible(Locators.bubble_button).is_displayed()

    def click_dashboard_button(self):
        self.element_is_visible(Locators.dashboard_button).click()

    def click_new_rule_icon(self):
        self.element_is_visible(Locators.new_rule_icon).click()
