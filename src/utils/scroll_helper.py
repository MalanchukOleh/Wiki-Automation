from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scroll_down_to_element(params: tuple, driver, max_attempts=10):
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]

    start_x = width / 2
    start_y = height * 0.8
    end_x = width / 2
    end_y = height * 0.2

    for attempt in range(max_attempts):
        try:
            element = WebDriverWait(driver, 1).until(
                EC.visibility_of_element_located(params)
            )
            return element
        except TimeoutException:
            # Perform the swipe action
            driver.swipe(start_x, start_y, end_x, end_y, 1000)

    raise Exception(
        f"Element with locator {params} not found after {max_attempts} attempts."
    )
