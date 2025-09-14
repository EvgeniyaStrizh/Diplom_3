from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        element.click()

    def input_text(self, locator, text, timeout=15):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_visible(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        return element.is_displayed()

    @allure.step("Перейти на URL")
    def navigate_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Найти элементы по локатору")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_elements(*locator)
        )

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        """Прокрутить страницу к указанному элементу"""
        self.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Нажать клавишу Escape")
    def press_escape(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()

    @allure.step("Получить атрибут элемента")
    def get_element_attribute(self, locator, attribute, timeout=10):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    @allure.step("Проверить отображение элемента")
    def is_element_displayed(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.is_displayed()


    @allure.step("Кликнуть на элемент с ожиданием")
    def click_element_with_wait(self, locator, timeout=10):
        """Кликнуть на элемент с ожиданием его кликабельности"""
        # Ждем, пока элемент станет кликабельным
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Ожидать исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ожидать, пока элемент исчезнет со страницы"""
        WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать появления элемента")
    def wait_for_element_to_appear(self, locator, timeout=10):
        """Ожидать появления элемента на странице"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Ожидать, пока элемент станет кликабельным"""
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ожидать полной загрузки страницы"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    @allure.step("Ожидать после прокрутки")
    def wait_after_scroll(self, element, timeout=2):
        """Ожидать стабилизации после прокрутки к элементу"""
        # Ждем, пока элемент станет видимым после прокрутки
        WebDriverWait(self.driver, timeout).until(
            lambda driver: element.is_displayed() and element.is_enabled()
        )

    @allure.step("Найти элементы по классу")
    def find_elements_by_class(self, class_name, timeout=10):
        """Найти элементы по классу"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.find_elements(By.CLASS_NAME, class_name)) > 0
        )
        return self.driver.find_elements(By.CLASS_NAME, class_name)

    @allure.step("Найти элементы по XPath")
    def find_elements_by_xpath(self, xpath, timeout=10):
        """Найти элементы по XPath"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.find_elements(By.XPATH, xpath)) > 0
        )
        return self.driver.find_elements(By.XPATH, xpath)

    @allure.step("Получить видимые элементы")
    def get_visible_elements(self, elements):
        """Получить только видимые элементы из списка"""
        return [elem for elem in elements if elem.is_displayed()]