from time import sleep

import allure
from pages.p6_summary_page import SummaryPage
from pages.p7_settings_page import SettingsPage


@allure.feature("tests for exporting wallet")
class TestWalletBackup:

    @allure.title("e2e test for export wallet")
    @allure.description("Test checks happy case of exporting wallet by QR-code")
    def test_e2e_wallet_export_QR_code(self, common_steps2):
        common_steps2.enter_passcode("8 2 5 4 7 6")
        common_steps2.click_on_element(SummaryPage.get_popup_button_update_later())
        common_steps2.click_on_element(SummaryPage.get_settings_button())
        common_steps2.click_on_element(SettingsPage.get_manage_wallets_button())
        common_steps2.click_on_element(SettingsPage.get_zerion_wallets())
        common_steps2.click_on_element(SettingsPage.get_first_wallet())
        common_steps2.click_on_element(SettingsPage.get_private_key())
        common_steps2.click_on_element(SettingsPage.get_show_button())
        common_steps2.enter_passcode("8 2 5 4 7 6")
        common_steps2.click_on_element(SettingsPage.get_display_private_key_button())
        assert(common_steps2.check_elements_presence(SettingsPage.get_QR_code()))
        assert(common_steps2.check_elements_presence(SettingsPage.get_copy_to_clipboard()))
        common_steps2.click_on_element(SettingsPage.get_copy_to_clipboard())

