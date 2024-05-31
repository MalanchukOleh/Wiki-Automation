from appium.webdriver.common.appiumby import AppiumBy


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.skip_button = "org.wikipedia:id/fragment_onboarding_skip_button"

    def tap_on_skip_button(self):
        self.driver.find_element(by=AppiumBy.ID, value=self.skip_button).click()
