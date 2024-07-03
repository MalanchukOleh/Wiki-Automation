from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.utils.scroll_helper import scroll_down_to_element


class FeedPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar_id = "org.wikipedia:id/search_container"
        self.top_read_container_title_id = "org.wikipedia:id/view_card_header_title"
        self.top_read_container_id = "org.wikipedia:id/view_list_card_list"

    def tap_on_search_bar(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, self.search_bar_id))
        )
        element.click()

    def is_top_read_title_displayed(self):
        element = scroll_down_to_element(
            params=(By.ID, self.top_read_container_title_id), driver=self.driver
        )
        return element.is_displayed()

    def is_top_read_container_displayed(self):
        element = scroll_down_to_element(
            params=(By.ID, self.top_read_container_id), driver=self.driver
        )
        return element.is_displayed()
