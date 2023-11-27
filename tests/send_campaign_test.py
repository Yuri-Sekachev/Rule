import time


from pages.login_page import LoginPage
from pages.V5_page import V5Page
from pages.campaign_page import CampaignPage, DraftPage


class TestSendCampaign:
    def test_send_campaign(self, driver):
        login_page = LoginPage(driver, 'https://app.rule.io')
        v5_page = V5Page(driver, 'https://app.rule.io/v5/#/app/dashboard')
        campaign_page = CampaignPage(driver, 'https://app.rule.io/v5/#/app/campaigns/list')
        draft_page = DraftPage(driver, 'https://app.rule.io/v5/#/app/campaigns/list/draft?search=&page=1&limit=20')
        login_page.open()
        login_page.login()
        time.sleep(2)
        v5_page.open()
        v5_page.close_modal_1()
        v5_page.close_modal_2()
        campaign_page.open()
        campaign_page.click_three_dots_button()
        campaign_page.click_copy_to_draft_button()
        assert campaign_page.success_snack_bar_is_visible()
        campaign_page.click_snack_bar_link()
        time.sleep(1)
        draft_page.click_schedule_button()
        draft_page.click_radio_send_now_button()
        draft_page.click_modal_submit_button()
        time.sleep(1)
        assert draft_page.rule_banner_message_is_visible()
        time.sleep(2)
