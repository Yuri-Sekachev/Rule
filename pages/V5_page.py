import os

from pages.base_page import BasePage
from locators.V5_locators import V5Locators as Locators


class V5Page(BasePage):
    def close_modal_1(self):
        self.element_is_visible(Locators.close_modal_1_button).click()

    def close_modal_2(self):
        self.element_is_visible(Locators.close_modal_2_button).click()
        self.driver.execute_script("document.getElementsByTagName('rule-tutorial-hint-tooltip')[0].remove();")

    def click_hor_expand_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.panel_hor_expand_button))

    def click_for_ver_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.panel_ver_expand_button))

    def click_segments_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.segments_button))

    def click_smoke_segment_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.smoke_segment_button))

    def click_sync_now_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.sync_now_button))

    def success_snack_bar_is_visible(self):
        return self.element_is_visible(Locators.success_snack_bar)

    def click_actions_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.actions_button))

    def click_xls_button(self):
        self.driver.execute_script("arguments[0].click();", self.elements_is_clickable(Locators.xls_button))

    def click_order_group_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.order_group_button))

    def click_select_all_order_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.select_all_order_button))

    def click_user_group_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.user_group_button))

    def click_select_all_user_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.select_all_user_button))

    def click_export_segment_button(self):
        self.driver.execute_script("arguments[0].click();", self.element_is_visible(Locators.export_segment_button))

    @staticmethod
    def test_file_download():
        download_path = "/home/Downloads/file.xls"
        return os.path.exists(download_path), f"File '{download_path}' was not downloaded"
