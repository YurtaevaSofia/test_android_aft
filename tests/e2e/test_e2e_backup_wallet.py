from time import sleep

import pytest

from pages.p3_create_or_import_page import CreateOrImportPage
from pages.p5_generating_wallet_page import GeneratingWalletPage
from pages.p1_get_started_page import GetStartedPage
import allure
from pages.p2_introducing_zerion_wallet_page import IntroducingZerionWalletPage
from pages.p6_summary_page import SummaryPage


@allure.feature("tests for wallet backup")
class TestWalletBackup:

    @allure.title("e2e test for wallet backup - successful case")
    @allure.description("Test checks happy case of wallet backup by new user")
    def test_e2e_wallet_backup(self, common_steps2):
        sleep(1)
        common_steps2.enter_passcode("8 2 5 4 7 6")
        common_steps2.click_on_element(SummaryPage.get_button_backup_1min())
        sleep(1)
        common_steps2.click_on_element(SummaryPage.get_popup_button_update_later())
        sleep(3)
        common_steps2.click_on_element(SummaryPage.get_button_got_it())
        common_steps2.wait_for_element_to_appear(10, SummaryPage.get_button_show_seed_phrase())
        common_steps2.click_on_element(SummaryPage.get_button_show_seed_phrase())
        common_steps2.enter_passcode("8 2 5 4 7 6")
        common_steps2.remember_the_seed_phrase()
        common_steps2.click_on_element(SummaryPage.get_button_confirm_phrase())
        common_steps2.answer_the_question()
        common_steps2.answer_the_question()
        common_steps2.answer_the_question()
        common_steps2.answer_the_question()
        common_steps2.answer_the_question()
        common_steps2.wait_for_element_to_appear(3, SummaryPage.get_nicely_done())
        assert common_steps2.get_element_text(SummaryPage.get_nicely_done()) == "Nicely done!"
        common_steps2.click_on_element(SummaryPage.get_finish_button())


    @allure.title("e2e test for wallet backup - successful case")
    @allure.description("Test checks happy case of wallet backup by new user")
    def test_e2e_wallet_backup(self, common_steps, screenshot_maker, create_wallet):
        sleep(2)
        common_steps.click_on_element(SummaryPage.get_button_backup_1min())
        sleep(1)
        common_steps.click_on_element(SummaryPage.get_popup_button_update_later())
        sleep(3)
        common_steps.click_on_element(SummaryPage.get_button_got_it())
        common_steps.wait_for_element_to_appear(10, SummaryPage.get_button_show_seed_phrase())
        common_steps.click_on_element(SummaryPage.get_button_show_seed_phrase())
        common_steps.enter_passcode("8 2 5 4 7 6")
        common_steps.remember_the_seed_phrase()
        common_steps.click_on_element(SummaryPage.get_button_confirm_phrase())
        common_steps.answer_the_question()
        common_steps.answer_the_question()
        common_steps.answer_the_question()
        common_steps.answer_the_question()
        common_steps.answer_the_question()
        common_steps.wait_for_element_to_appear(3, SummaryPage.get_nicely_done())
        assert common_steps.get_element_text(SummaryPage.get_nicely_done()) == "Nicely done!", \
            screenshot_maker.capture_screenshot("error_in_button_text.png")
        common_steps.click_on_element(SummaryPage.get_finish_button())

    @allure.title("e2e test for wallet backup - user mistake in the survey")
    @allure.description("Test checks user mistake in the survey case of wallet backup")
    def test_e2e_wallet_backup_user_mistake_in_survey(self, common_steps, screenshot_maker, create_wallet):
        sleep(1)
        common_steps.click_on_element(SummaryPage.get_button_backup_1min())
        sleep(1)
        common_steps.click_on_element(SummaryPage.get_popup_button_update_later())
        sleep(3)
        common_steps.click_on_element(SummaryPage.get_button_got_it())
        common_steps.wait_for_element_to_appear(10, SummaryPage.get_button_show_seed_phrase())
        common_steps.click_on_element(SummaryPage.get_button_show_seed_phrase())
        common_steps.enter_passcode("8 2 5 4 7 6")
        common_steps.remember_the_seed_phrase()
        common_steps.click_on_element(SummaryPage.get_button_confirm_phrase())
        common_steps.answer_the_question()
        common_steps.answer_the_question()
        common_steps.answer_the_question_wrong()
        common_steps.answer_the_question_wrong()
        common_steps.wait_for_element_to_appear(3, SummaryPage.get_warning_notification())
        assert common_steps.get_element_text(SummaryPage.get_warning_notification()) == "Don't try to guess the word", \
            screenshot_maker.capture_screenshot("error_in_warning_text.png")
        sleep(5)
