from selenium.webdriver.common.by import By


class CampaignLocators:
    three_dots_button = (By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(6) button')
    copy_to_draft_button = (By.CSS_SELECTOR, 'button[type="button"]')
    success_snack_bar = (By.XPATH, '//h4[text()="Success!"]')
    snack_bar_link = (By.LINK_TEXT, 'Go to the copied campaign page')
    draft_campaign_link = (By.CSS_SELECTOR, 'rule-menu-action-list a')
    schedule_button = (By.CSS_SELECTOR, '.rule-icon-calendar-outline.rule-icon')
    radio_send_now_button = (By.CSS_SELECTOR, 'rule-radio-group > rule-radio-button:nth-child(2)')
    modal_submit_button = (By.CSS_SELECTOR, '[type="submit"]')
    rule_banner = (By.CSS_SELECTOR, '.rule-banner-message')
