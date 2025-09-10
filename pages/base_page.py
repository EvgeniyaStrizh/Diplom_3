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
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False

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
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()
        except:
            return False

    @allure.step("Проверить отображение элемента с несколькими попытками")
    def is_element_visible_with_fallback(self, primary_locator, fallback_locators, timeout=10):
        """Проверить отображение элемента, пробуя несколько локаторов по очереди"""
        locators_to_try = [primary_locator] + fallback_locators
        
        for locator in locators_to_try:
            try:
                if self.is_element_visible(locator, timeout=5):
                    return True
            except:
                continue
        return False

    @allure.step("Найти элемент с несколькими попытками")
    def find_element_with_fallback(self, primary_locator, fallback_locators, timeout=10):
        """Найти элемент, пробуя несколько локаторов по очереди"""
        locators_to_try = [primary_locator] + fallback_locators
        
        for locator in locators_to_try:
            try:
                element = self.find_element(locator, timeout=5)
                if element and element.is_displayed():
                    return element
            except:
                continue
        return None

    @allure.step("Найти элементы с несколькими попытками")
    def find_elements_with_fallback(self, primary_locator, fallback_locators, timeout=10):
        """Найти элементы, пробуя несколько локаторов по очереди"""
        locators_to_try = [primary_locator] + fallback_locators
        
        for locator in locators_to_try:
            try:
                elements = self.find_elements(locator, timeout=5)
                if elements and len(elements) > 0:
                    return elements
            except:
                continue
        return []

    @allure.step("Кликнуть на элемент с несколькими попытками")
    def click_element_with_fallback(self, primary_locator, fallback_locators, timeout=10):
        """Кликнуть на элемент, пробуя несколько локаторов по очереди"""
        element = self.find_element_with_fallback(primary_locator, fallback_locators, timeout)
        if element:
            try:
                element.click()
                return True
            except Exception as e:
                print(f"Ошибка при клике: {e}")
                # Пробуем кликнуть через JavaScript
                try:
                    self.execute_script("arguments[0].click();", element)
                    return True
                except Exception as e2:
                    print(f"JavaScript клик не удался: {e2}")
                    return False
        return False

    @allure.step("Кликнуть на элемент с ожиданием")
    def click_element_with_wait(self, locator, timeout=10):
        """Кликнуть на элемент с ожиданием его кликабельности"""
        try:
            # Ждем, пока элемент станет кликабельным
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return True
        except Exception as e:
            print(f"Обычный клик не удался: {e}")
            try:
                # Пробуем кликнуть через ActionChains
                element = self.find_element(locator, timeout)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                return True
            except Exception as e2:
                print(f"ActionChains клик не удался: {e2}")
                try:
                    # Пробуем кликнуть через JavaScript
                    element = self.find_element(locator, timeout)
                    self.execute_script("arguments[0].click();", element)
                    return True
                except Exception as e3:
                    print(f"JavaScript клик не удался: {e3}")
                    return False

    @allure.step("Ожидать исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ожидать, пока элемент исчезнет со страницы"""
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception as e:
            print(f"Элемент не исчез в течение {timeout} секунд: {e}")
            return False

    @allure.step("Ожидать появления элемента")
    def wait_for_element_to_appear(self, locator, timeout=10):
        """Ожидать появления элемента на странице"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception as e:
            print(f"Элемент не появился в течение {timeout} секунд: {e}")
            return False

    @allure.step("Ожидать кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Ожидать, пока элемент станет кликабельным"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except Exception as e:
            print(f"Элемент не стал кликабельным в течение {timeout} секунд: {e}")
            return False

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ожидать полной загрузки страницы"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            return True
        except Exception as e:
            print(f"Страница не загрузилась в течение {timeout} секунд: {e}")
            return False

    @allure.step("Ожидать после прокрутки")
    def wait_after_scroll(self, element, timeout=2):
        """Ожидать стабилизации после прокрутки к элементу"""
        try:
            # Ждем, пока элемент станет видимым после прокрутки
            WebDriverWait(self.driver, timeout).until(
                lambda driver: element.is_displayed() and element.is_enabled()
            )
            return True
        except Exception as e:
            print(f"Элемент не стабилизировался после прокрутки: {e}")
            return False