from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ArticlePage:
    def __init__(self, driver):
        self.driver = driver
        self.title_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("SoftServe").instance(0)',
        )

    def is_title_displayed(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.title_locator)
        )
        return element.is_displayed()
