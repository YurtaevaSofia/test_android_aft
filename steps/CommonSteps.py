import os
from time import sleep

import numpy as np
from PIL import Image
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from pages.p4_set_passcode_page import SetPasscodePage

words = []


def get_element_search_parameter(element):
    if element[0] == 'id':
        return AppiumBy.ID
    elif element[0] == 'accessibility_id':
        return AppiumBy.ACCESSIBILITY_ID
    elif element[0] == 'xpath':
        return AppiumBy.XPATH
    else:
        return AppiumBy.CUSTOM


def assert_images_equal(image_1: str, image_2: str):
    img1 = Image.open(image_1)
    img2 = Image.open(image_2)

    # Convert to same mode and size for comparison
    img2 = img2.convert(img1.mode)
    img2 = img2.resize(img1.size)

    sum_sq_diff = np.sum((np.asarray(img1).astype('float') - np.asarray(img2).astype('float')) ** 2)

    if sum_sq_diff == 0:
        # Images are exactly the same
        pass
    else:
        normalized_sum_sq_diff = np.sqrt(sum_sq_diff / np.asarray(img1).size)
        print(normalized_sum_sq_diff)
        assert normalized_sum_sq_diff < 7


class CommonSteps:

    def __init__(self, driver):
        self.driver = driver

    def check_elements_presence(self, element):
        return self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).is_displayed()

    def check_element_is_clickable(self, element):
        return self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).isEnabled()

    def click_on_element(self, element):
        try:
            self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).click()
        except NoSuchElementException:
            sleep(1)
            print('lol')
            self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).click()

    def get_element_text(self, element):
        return self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).get_attribute(
            "text")

    def enter_passcode(self, passcode):
        passcode_numerals = passcode.split()
        for numeral in passcode_numerals:
            self.click_on_element(SetPasscodePage.get_button_numeral(numeral))

    def wait_for_element_to_appear(self, seconds, element):
        self.driver.implicitly_wait(seconds)
        self.check_elements_presence(element)

    def tap_on_element(self, element):
        actions = TouchAction(self.driver)
        actions.tap(self.driver.find_element(by=get_element_search_parameter(element), value=element[1]))
        actions.perform()

    def check_image_similarity(self, baseline_filename, screenshot_filename):

        generated_file = os.path.join(str("/Users/sofia/PycharmProjects/zerion_android_aft/tests/screenshots"),
                                      "{}".format(screenshot_filename))

        assert_images_equal(
            "/Users/sofia/PycharmProjects/zerion_android_aft/resources/baseline_images/{}".format(baseline_filename),
            generated_file)

    def remember_the_seed_phrase(self):
        sleep(9)
        elements = self.driver.find_elements(by='id', value='io.zerion.android:id/recoveryWordTV')
        for element in elements:
            words.append(element.get_attribute('text'))
        print(words)

    def answer_the_question(self):
        sleep(0.5)
        number = self.driver.find_element(by='id', value='io.zerion.android:id/number').get_attribute('text')
        secret_word = words[int(number) - 1]
        for i in range(1, 5):
            element = self.driver.find_element(by='id', value='io.zerion.android:id/variantButton' + str(i))
            text = element.get_attribute('text')
            if text == secret_word:
                element.click()
                break
            else:
                i = i + 1

    def answer_the_question_wrong(self):
        sleep(0.5)
        number = self.driver.find_element(by='id', value='io.zerion.android:id/number').get_attribute('text')
        secret_word = words[int(number) - 1]
        print(number + " " + secret_word)
        for i in range(1, 5):
            element = self.driver.find_element(by='id', value='io.zerion.android:id/variantButton' + str(i))
            text = element.get_attribute('text')
            print(i)
            print(text)
            if text != secret_word:
                element.click()
                break
            else:
                i = i + 1

    def enter_text(self, element, phrase):
        found_element = self.driver.find_element(by=get_element_search_parameter(element), value=element[1])
        found_element.send_keys(phrase)

    def find_element_by_text_and_click(self, phrase):
        found_element = self.driver.find_element_by_xpath('//div[contains(text(), "Continue")]')
        found_element.click()


