from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar_id = "org.wikipedia:id/search_container"

    def tap_on_search_bar(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, self.search_bar_id))
        )
        element.click()
