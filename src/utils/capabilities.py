from appium.options.android import UiAutomator2Options
import json

from appium.options.common import AppiumOptions


def get_capabilities(capabilities: str) -> AppiumOptions:
    return UiAutomator2Options().load_capabilities(json.load(open(capabilities)))
