from pages.base_page import BasePage
from locators.campaign_locators import CampaignLocators as Locators


class CampaignPage(BasePage):
    pass

    def click_three_dots_button(self):
        self.element_is_visible(Locators.three_dots_button).click()

    def click_copy_to_draft_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.copy_to_draft_button))

    def success_snack_bar_is_visible(self):
        return self.element_is_visible(Locators.success_snack_bar)

    def click_snack_bar_link(self):
        self.elements_is_clickable(Locators.snack_bar_link).click()


class DraftPage(BasePage):
    def click_schedule_button(self):
        self.element_is_visible(Locators.schedule_button).click()

    def click_radio_send_now_button(self):
        self.elements_is_clickable(Locators.radio_send_now_button).click()

    def click_modal_submit_button(self):
        self.elements_is_clickable(Locators.modal_submit_button).click()

    def rule_banner_message_is_visible(self):
        return self.element_is_present(Locators.rule_banner)
