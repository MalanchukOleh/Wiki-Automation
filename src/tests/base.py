import unittest

from src.utils.globals.appium_driver import AppiumDriverSingleton


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumDriverSingleton().get_driver()

    def tearDown(self):
        if self.driver:
            self.driver.quit()
