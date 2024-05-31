import unittest

from appium import webdriver
from capabilities_options import get_capabilities_options

from url import APPIUM_SERVER_URL

capabilities_options = get_capabilities_options(capabilities="capabilities.json")


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor=APPIUM_SERVER_URL, options=capabilities_options
        )

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
