from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_text_id = "org.wikipedia:id/search_src_text"
        self.result_of_search_text_xpath = '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="GlobalLogic"]'

    def enter_text(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, self.search_text_id))
        )
        element.send_keys("GlobalLogic")

    def click_on_search_result(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.result_of_search_text_xpath))
        )
        element.click()
