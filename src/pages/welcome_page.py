import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.skip_button_id = "org.wikipedia:id/fragment_onboarding_skip_button"

    def tap_on_skip_button(self):
        self.driver.find_element(by=AppiumBy.ID, value=self.skip_button_id).click()
