from time import sleep

from pages.p3_create_or_import_page import CreateOrImportPage
from pages.p5_generating_wallet_page import GeneratingWalletPage
from pages.p1_get_started_page import GetStartedPage
import allure
from pages.p2_introducing_zerion_wallet_page import IntroducingZerionWalletPage
from pages.p6_summary_page import SummaryPage


@allure.feature("tests for wallet creation")
class TestWalletCreation:

    @allure.title("e2e test for wallet creation")
    @allure.description("Test checks happy case of wallet creation by new user")
    def test_e2e_wallet_creation(self, common_steps, screenshot_maker):
        common_steps.click_on_element(GetStartedPage.get_button_get_started())
        common_steps.click_on_element(IntroducingZerionWalletPage.get_button())
        common_steps.click_on_element(CreateOrImportPage.get_button_create_new_wallet())
        common_steps.enter_passcode("8 2 5 4 7 6")
        common_steps.enter_passcode("8 2 5 4 7 6")
        common_steps.wait_for_element_to_appear(12, GeneratingWalletPage.get_ok_lets_go_button())
        sleep(5)
        common_steps.tap_on_element(GeneratingWalletPage.get_ok_lets_go_button())
        common_steps.wait_for_element_to_appear(20, GeneratingWalletPage.get_subtitle_owner_of())
        created_wallet_number = common_steps.get_element_text(GeneratingWalletPage.get_created_wallet_number())
        shortened_number = (created_wallet_number[:5] + '…' + created_wallet_number[-3:]).lower()
        assert common_steps.get_element_text(GeneratingWalletPage.get_button_generating()) == "Finish", \
            screenshot_maker.capture_screenshot("error_in_button_text.png")
        common_steps.click_on_element(GeneratingWalletPage.get_button_generating())
        common_steps.click_on_element(SummaryPage.get_button_i_will_take_risk())
        common_steps.click_on_element(SummaryPage.get_popup_button_update_later())
        sleep(3)
        assert common_steps.get_element_text(SummaryPage.get_first_created_wallet()).lower() == shortened_number, \
            screenshot_maker.capture_screenshot("error_in_created_wallet_number.png")


    @allure.title("e2e test for creation additional wallet")
    @allure.description("Test checks happy case of aaditional wallet")
    def test_e2e_create_additional_wallet(self, common_steps2):
        common_steps2.enter_passcode("8 2 5 4 7 6")
        common_steps2.click_on_element(SummaryPage.get_popup_button_update_later())
        common_steps2.click_on_element(SummaryPage.get_add_wallet())
        common_steps2.click_on_element(IntroducingZerionWalletPage.get_button())
        common_steps2.click_on_element(CreateOrImportPage.get_button_create_new_wallet())
        common_steps2.enter_passcode("8 2 5 4 7 6")
        common_steps2.wait_for_element_to_appear(12, GeneratingWalletPage.get_ok_lets_go_button())
        sleep(5)
        common_steps2.tap_on_element(GeneratingWalletPage.get_ok_lets_go_button())
        common_steps2.wait_for_element_to_appear(20, GeneratingWalletPage.get_subtitle_owner_of())
        created_wallet_number = common_steps2.get_element_text(GeneratingWalletPage.get_created_wallet_number())
        shortened_number = (created_wallet_number[:5] + '…' + created_wallet_number[-3:]).lower()
        assert common_steps2.get_element_text(GeneratingWalletPage.get_button_generating()) == "Finish"
        common_steps2.click_on_element(GeneratingWalletPage.get_button_generating())
        sleep(3)
        assert common_steps2.get_element_text(SummaryPage.get_imported_wallet()).lower() == shortened_number









