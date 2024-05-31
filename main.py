from appium.webdriver.common.appiumby import AppiumBy
from base import BaseTest


class SearchGlobalLogicTest(BaseTest):
    def test_find_battery(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.ID, value="org.wikipedia:id/fragment_onboarding_skip_button"
        )
        el.click()
