import unittest

from src.pages.article_page import ArticlePage
from src.pages.feed_page import FeedPage
from src.pages.search_page import SearchPage
from src.pages.welcome_page import WelcomePage
from src.tests.base import BaseTest


class SearchTest(BaseTest):
    def test_search_test(self):
        welcome_page = WelcomePage(self.driver)
        feed_page = FeedPage(self.driver)
        search_page = SearchPage(self.driver)
        article_page = ArticlePage(self.driver)
        welcome_page.tap_on_skip_button()
        feed_page.tap_on_search_bar()
        search_page.enter_text()
        search_page.click_on_search_result()
        assert article_page.is_title_displayed() == True


if __name__ == "__main__":
    unittest.main()
