from time import sleep

import allure

from pages.p6_summary_page import SummaryPage
from pages.p7_settings_page import SettingsPage


@allure.feature("tests for importing wallet")
class TestWalletBackup:

    @allure.title("e2e test for importing wallet")
    @allure.description("Test checks happy case of importing wallet by seed phrase")
    def test_e2e_wallet_import_by_seed_phrase(self, common_steps, create_wallet):
        common_steps.click_on_element(SummaryPage.get_button_i_will_take_risk())
        common_steps.click_on_element(SummaryPage.get_popup_button_update_later())
        common_steps.click_on_element(SummaryPage.get_settings_button())
        common_steps.click_on_element(SettingsPage.get_manage_wallets_button())
        common_steps.click_on_element(SettingsPage.get_import_wallet_button())
        common_steps.enter_passcode("8 2 5 4 7 6")
        common_steps.enter_text(SettingsPage.get_enter_seed_phrase_or_private_key(),
                                 "Recycle Unlock Custom Museum Car Elbow Cigar Seat Dice Chimney Zero Know")
        sleep(1)
        common_steps.click_on_element(SettingsPage.get_import_button())
        common_steps.wait_for_element_to_appear(20, SettingsPage.get_wallet_for_import())
        wallet_number = common_steps.get_element_text(SettingsPage.get_wallet_for_import())
        assert common_steps.get_element_text(SettingsPage.get_wallets_ready_to_import()) == "Wallets ready to Import"
        common_steps.click_on_element(SettingsPage.get_wallet_for_import())
        sleep(3)
        common_steps.click_on_element(SettingsPage.get_continue_button())
        common_steps.wait_for_element_to_appear(20, SettingsPage.get_all_done())
        assert common_steps.get_element_text(SettingsPage.get_all_done()) == "All done! Your wallets have been imported 🚀"
        common_steps.click_on_element(SettingsPage.get_finish_button())
        sleep(2)
        common_steps.click_on_element(SummaryPage.get_summery())
        assert(common_steps.check_elements_presence(SummaryPage.get_imported_wallet()))
        assert common_steps.get_element_text(SummaryPage.get_imported_wallet()) == wallet_number



    @allure.title("e2e test for importing wallet by private key")
    @allure.description("Test checks happy case of importing wallet by private key")
    def test_e2e_wallet_import_by_private_key(self, common_steps, create_wallet):
        common_steps.click_on_element(SummaryPage.get_button_i_will_take_risk())
        common_steps.click_on_element(SummaryPage.get_popup_button_update_later())
        common_steps.click_on_element(SummaryPage.get_settings_button())
        common_steps.click_on_element(SettingsPage.get_manage_wallets_button())
        common_steps.click_on_element(SettingsPage.get_import_wallet_button())
        common_steps.enter_passcode("8 2 5 4 7 6")
        common_steps.enter_text(SettingsPage.get_enter_seed_phrase_or_private_key(),
                                 "634a14b604e0233c48e5be10432777492033966b407593f3e273b528547451d6")
        sleep(1)
        common_steps.click_on_element(SettingsPage.get_import_button())
        common_steps.wait_for_element_to_appear(20, SettingsPage.get_all_done())
        assert common_steps.get_element_text(SettingsPage.get_all_done()) == "All done! Your wallets have been imported 🚀"
        common_steps.click_on_element(SettingsPage.get_finish_button())
        sleep(2)
        common_steps.click_on_element(SummaryPage.get_summery())
        assert(common_steps.check_elements_presence(SummaryPage.get_imported_wallet()))
        assert common_steps.get_element_text(SummaryPage.get_imported_wallet()) == "0xcE1…EBE"

