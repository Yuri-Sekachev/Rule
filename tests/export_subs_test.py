import time
import pytest


from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.V5_page import V5Page


class TestExportSubs:
    def test_export_subs(self, driver):
        login_page = LoginPage(driver, 'https://app.rule.io/v5/#/auth/login')
        home_page = HomePage(driver, 'https://app.rule.io')
        v5_page = V5Page(driver, 'https://app.rule.io')
        login_page.open()
        login_page.login()
        time.sleep(3)
        home_page.click_dashboard_button()
        home_page.click_new_rule_icon()
        v5_page.close_modal_1()
        v5_page.close_modal_2()
        v5_page.click_hor_expand_button()
        v5_page.click_for_ver_button()
        v5_page.click_segments_button()
        v5_page.click_smoke_segment_button()
        time.sleep(3)
        v5_page.click_sync_now_button()
        time.sleep(1)
        assert v5_page.success_snack_bar_is_visible()
        v5_page.click_actions_button()
        v5_page.click_xls_button()
        v5_page.click_order_group_button()
        v5_page.click_select_all_order_button()
        v5_page.click_user_group_button()
        v5_page.click_select_all_user_button()
        v5_page.click_export_segment_button()
        time.sleep(5)
        assert v5_page.test_file_download()
        driver.quit()
