import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{self.base_url}feed"

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        self.navigate_to_url(self.url)

    @allure.step("Кликнуть на заказ")
    def click_order(self, index=0):
        orders = self.find_elements(OrderFeedLocators.ORDER_ITEM)
        if orders and index < len(orders):
            orders[index].click()

    @allure.step("Проверить открытие модального окна заказа")
    def is_order_modal_opened(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_MODAL)

    @allure.step("Получить детали заказа")
    def get_order_details(self):
        return self.get_text(OrderFeedLocators.ORDER_DETAILS)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_element(OrderFeedLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        # Пробуем найти счетчик с fallback локаторами
        fallback_locators = [
            (By.XPATH, "//p[contains(text(), 'всего') or contains(text(), 'все') or contains(text(), 'total')]"),
            (By.XPATH, "//span[contains(text(), 'всего') or contains(text(), 'все') or contains(text(), 'total')]"),
            (By.XPATH, "//div[contains(text(), 'всего') or contains(text(), 'все') or contains(text(), 'total')]")
        ]
        
        element = self.find_element_with_fallback(OrderFeedLocators.TOTAL_ORDERS_COUNTER, fallback_locators)
        if element:
            text = element.text
            # Извлекаем число из текста
            import re
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else "0"
        return "0"

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        # Пробуем найти счетчик с fallback локаторами
        fallback_locators = [
            (By.XPATH, "//p[contains(text(), 'сегодня') or contains(text(), 'today')]"),
            (By.XPATH, "//span[contains(text(), 'сегодня') or contains(text(), 'today')]"),
            (By.XPATH, "//div[contains(text(), 'сегодня') or contains(text(), 'today')]")
        ]
        
        element = self.find_element_with_fallback(OrderFeedLocators.TODAY_ORDERS_COUNTER, fallback_locators)
        if element:
            text = element.text
            # Извлекаем число из текста
            import re
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else "0"
        return "0"

    @allure.step("Проверить наличие заказов в работе")
    def get_in_progress_orders(self):
        # Пробуем найти заказы в работе с fallback локаторами
        fallback_locators = [
            (By.XPATH, "//div[contains(@class, 'in-progress') or contains(@class, 'progress') or contains(@class, 'работа')]"),
            (By.XPATH, "//div[contains(text(), 'в работе') or contains(text(), 'готовится') or contains(text(), 'готовится')]"),
            (By.XPATH, "//div[contains(@class, 'order') and contains(@class, 'active')]")
        ]
        
        elements = self.find_elements_with_fallback(OrderFeedLocators.IN_PROGRESS_ORDERS, fallback_locators)
        return elements if elements else []

    @allure.step("Проверить наличие выполненных заказов")
    def get_done_orders(self):
        return self.find_elements(OrderFeedLocators.DONE_ORDERS)

    @allure.step("Проверить отображение заказа пользователя")
    def is_user_order_displayed(self, order_number):
        orders = self.find_elements(OrderFeedLocators.ORDER_NUMBER)
        for order in orders:
            if order.text == order_number:
                return True
        return False
