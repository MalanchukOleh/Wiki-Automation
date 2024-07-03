import pytest

from src.pages.feed_page import FeedPage
from src.pages.welcome_page import WelcomePage
from src.utils.globals.appium_driver import AppiumDriverSingleton


@pytest.fixture(scope="function")
def appium_driver():
    driver = AppiumDriverSingleton().get_driver()
    yield driver
    driver.quit()


def test_show_top_read_container(appium_driver):
    welcome_page = WelcomePage(appium_driver)
    feed_page = FeedPage(appium_driver)
    welcome_page.tap_on_skip_button()

    assert feed_page.is_top_read_title_displayed() == True
    assert feed_page.is_top_read_container_displayed() == True
