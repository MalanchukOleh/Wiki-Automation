from appium import webdriver

from src.utils.capabilities import get_capabilities
from src.utils.constants import APPIUM_SERVER_URL, CAPABILITIES_PATH


class AppiumDriverSingleton:
    _instance = None
    _driver = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppiumDriverSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._driver is None:
            self._driver = self._initialize_driver()

    @staticmethod
    def _initialize_driver():
        capabilities = get_capabilities(capabilities=CAPABILITIES_PATH)
        print(capabilities)
        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER_URL, options=capabilities
        )
        return driver

    def get_driver(self):
        return self._driver
