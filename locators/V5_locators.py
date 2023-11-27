from selenium.webdriver.common.by import By


class V5Locators:
    close_modal_1_button = (By.CSS_SELECTOR,
                            '.new-feature-modal-control.-basic.-medium.rule-button-base.rule-button.-ghost')
    close_modal_2_button = (By.CSS_SELECTOR,
                            'rule-start-widget .rule-start-widget-header.ng-star-inserted .rule-start-widget-heading '
                            '.rule-start-widget-controls > button:nth-child(2)')
    panel_hor_expand_button = (By.XPATH, '//rule-icon[@key="right-arrow-outline"]')
    panel_ver_expand_button = (By.XPATH, '(//rule-icon[@key="arrow-down-outline"])[1]')
    segments_button = (By.CSS_SELECTOR, 'ul > li:nth-child(5) > a > span')
    smoke_segment_button = (By.CSS_SELECTOR, '[title="1smoke"]')
    sync_now_button = (By.CSS_SELECTOR, '.actions-container > .rule-button-base:nth-child(2) > .inner > .wrapper > span')
    success_snack_bar = (By.XPATH, '//h4[text()="Success!"]')
    actions_button = (By.CSS_SELECTOR, '.menu-trigger.-basic.rule-button-base.rule-button.-outlined.-large.rule-menu'
                                       '-trigger')
    xls_button = (By.CSS_SELECTOR, '.options-container.rule-scrollable>button:nth-child(2)')
    order_group_button = (By.XPATH, '(//rule-accordion-item-header[@class="rule-accordion-item-header"])[1]')
    select_all_order_button = (By.CSS_SELECTOR, 'rule-accordion > rule-accordion-item:nth-child(1) > '
                                                'rule-accordion-item-body rule-checkbox-group-grid div rule-checkbox '
                                                '> label > span input')
    user_group_button = (By.XPATH, '(//rule-accordion-item-header[@class="rule-accordion-item-header"])[2]')
    select_all_user_button = (By.CSS_SELECTOR, 'rule-accordion > rule-accordion-item:nth-child(2) > '
                                               'rule-accordion-item-body rule-checkbox-group-grid div rule-checkbox >'
                                               ' label > span input')
    export_segment_button = (By.CSS_SELECTOR, 'rule-modal-actions > button:nth-child(2)')
