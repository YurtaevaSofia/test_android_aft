from time import sleep
from pages.p1_get_started_page import GetStartedPage
import allure


@allure.feature("tests of element presence on pages")
class TestPages:

    @allure.title("get_started_page_check")
    @allure.description("Test checks all elements presented on start_page")
    def test_get_started_page_check(self, common_steps, screenshot_maker):
        assert (common_steps.check_elements_presence(GetStartedPage.get_icon()))
        screenshot_maker.capture_screenshot("screenshot1.png")
        common_steps.check_image_similarity("bi1_one_wallet_to_do_it_all.png", "screenshot1.png")
        assert (common_steps.check_elements_presence(GetStartedPage.get_title()))
        assert (common_steps.check_elements_presence(GetStartedPage.get_button_get_started()))
        assert (common_steps.get_element_text(GetStartedPage.get_title()) == "One Wallet\nTo Do It All")
        assert (common_steps.get_element_text(GetStartedPage.get_subtitle()) == "Turn your phone into Web3 Mission Control with a wallet built for humans, not degens")
        sleep(8)
        screenshot_maker.capture_screenshot("screenshot2.png")
        common_steps.check_image_similarity("bi2_build_a_truly_multichain_portfolio.png", "screenshot2.png")
        assert (common_steps.get_element_text(GetStartedPage.get_title()) == "Build a Truly\nMultichain Portfolio")
        assert (common_steps.get_element_text(GetStartedPage.get_subtitle()) == "Track your complete portfolio across and manage all your private keys in one app")
        sleep(8)
        screenshot_maker.capture_screenshot("screenshot3.png")
        common_steps.check_image_similarity("bi3_explore_web3_with_people_you_trust.png", "screenshot3.png")
        assert (common_steps.get_element_text(GetStartedPage.get_title()) == "Explore Web3\nWith People You Trust")
        assert (common_steps.get_element_text(GetStartedPage.get_subtitle()) == "Create or import multiple wallets & sign transactions in-app")

