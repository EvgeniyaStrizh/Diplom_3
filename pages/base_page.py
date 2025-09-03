from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_visible(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False