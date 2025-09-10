import allure
import re
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
        element = self.find_element_with_fallback(OrderFeedLocators.TOTAL_ORDERS_COUNTER, OrderFeedLocators.TOTAL_ORDERS_FALLBACK)
        if element:
            text = element.text
            # Извлекаем число из текста
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else "0"
        return "0"

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        element = self.find_element_with_fallback(OrderFeedLocators.TODAY_ORDERS_COUNTER, OrderFeedLocators.TODAY_ORDERS_FALLBACK)
        if element:
            text = element.text
            # Извлекаем число из текста
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else "0"
        return "0"

    @allure.step("Проверить наличие заказов в работе")
    def get_in_progress_orders(self):
        elements = self.find_elements_with_fallback(OrderFeedLocators.IN_PROGRESS_ORDERS, OrderFeedLocators.IN_PROGRESS_ORDERS_FALLBACK)
        return elements if elements else []

    @allure.step("Проверить наличие выполненных заказов")
    def get_done_orders(self):
        return self.find_elements(OrderFeedLocators.DONE_ORDERS)

    @allure.step("Получить список заказов")
    def get_orders_list(self):
        """Получить список всех заказов на странице"""
        return self.find_elements(OrderFeedLocators.ORDER_ITEM)

    @allure.step("Проверить отображение заказа пользователя")
    def is_user_order_displayed(self, order_number):
        orders = self.find_elements(OrderFeedLocators.ORDER_NUMBER)
        for order in orders:
            if order.text == order_number:
                return True
        return False
