import unittest

from src.pages.welcome import WelcomePage
from src.tests.base import BaseTest


class SearchTest(BaseTest):

    def search_test(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.tap_on_skip_button()
        # TODO: COMPLETE TEST


if __name__ == "__main__":
    unittest.main()
