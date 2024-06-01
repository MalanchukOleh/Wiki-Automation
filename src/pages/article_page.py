from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ArticlePage:
    def __init__(self, driver):
        self.driver = driver
        self.title_xpath = '//android.view.View[@text="GlobalLogic"]'

    def is_title_displayed(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.title_xpath))
        )
        return element.is_displayed()
