import os
from time import sleep

import pytest
from appium import webdriver

from core.ConfigurationLoader import ConfigurationLoader
from core.ScreenshotMaker import ScreenshotMaker
from pages.p1_get_started_page import GetStartedPage
from pages.p2_introducing_zerion_wallet_page import IntroducingZerionWalletPage
from pages.p3_create_or_import_page import CreateOrImportPage
from pages.p5_generating_wallet_page import GeneratingWalletPage
from steps.CommonSteps import CommonSteps


@pytest.fixture(scope="session")
def configuration():
    return ConfigurationLoader("/Users/sofia/PycharmProjects/zerion_android_aft/resources/configuration.txt")


@pytest.yield_fixture(scope="function")
def driver(configuration):
    desired_caps = {
        "app": os.path.expanduser(configuration.get_app()),
        "platformName": configuration.get_platform_name(),
        "deviceName": configuration.get_device_name()
    }
    driver = webdriver.Remote(configuration.get_url(), desired_caps)
    driver.implicitly_wait(10)
    print("Driver started!")
    yield driver
    driver.quit()


@pytest.yield_fixture(scope="function")
def driver_with_no_reset(configuration):
    desired_caps = {
        "app": os.path.expanduser(configuration.get_app()),
        "platformName": configuration.get_platform_name(),
        "deviceName": configuration.get_device_name(),
        "noReset": "true",
        "appActivity": ".ui.launch.LaunchActivity",
        "appPackage": "io.zerion.android"
    }
    driver = webdriver.Remote(configuration.get_url(), desired_caps)
    driver.implicitly_wait(10)
    print("Driver started!")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def screenshot_maker(driver):
    return ScreenshotMaker(driver)


# is used when there is a need to restart session, we need to continue work in a new session
@pytest.fixture(scope="function")
def common_steps(driver):
    return CommonSteps(driver)


# is used when there is no need in a session restart, we need to continue work in same session
@pytest.fixture(scope="function")
def common_steps2(driver_with_no_reset):
    return CommonSteps(driver_with_no_reset)


@pytest.fixture(scope="function")
def create_wallet(common_steps):
    common_steps.click_on_element(GetStartedPage.get_button_get_started())
    common_steps.click_on_element(IntroducingZerionWalletPage.get_button())
    common_steps.click_on_element(CreateOrImportPage.get_button_create_new_wallet())
    common_steps.enter_passcode("8 2 5 4 7 6")
    common_steps.enter_passcode("8 2 5 4 7 6")
    common_steps.wait_for_element_to_appear(12, GeneratingWalletPage.get_ok_lets_go_button())
    sleep(5)
    common_steps.tap_on_element(GeneratingWalletPage.get_ok_lets_go_button())
    common_steps.wait_for_element_to_appear(20, GeneratingWalletPage.get_subtitle_owner_of())
    common_steps.click_on_element(GeneratingWalletPage.get_button_generating())
