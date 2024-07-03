import pytest

from src.pages.article_page import ArticlePage
from src.pages.feed_page import FeedPage
from src.pages.search_page import SearchPage
from src.pages.welcome_page import WelcomePage
from src.utils.globals.appium_driver import AppiumDriverSingleton


@pytest.fixture(scope="module")
def appium_driver():
    driver = AppiumDriverSingleton().get_driver()
    yield driver
    driver.quit()


def test_show_article_page(appium_driver):
    welcome_page = WelcomePage(appium_driver)
    feed_page = FeedPage(appium_driver)
    search_page = SearchPage(appium_driver)
    article_page = ArticlePage(appium_driver)
    welcome_page.tap_on_skip_button()
    feed_page.tap_on_search_bar()
    search_page.enter_text()
    search_page.click_on_search_result()
    assert article_page.is_title_displayed() == True
