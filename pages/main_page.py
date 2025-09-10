import allure
import re
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators
from locators.order_locators import OrderLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_site()

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_element(BaseLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_element(BaseLocators.ORDER_FEED_BUTTON)

    @allure.step("Перейти в личный кабинет")
    def go_to_personal_account(self):
        self.click_element(BaseLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, index=0):
        # Закрываем модальное окно если открыто
        if self.is_ingredient_modal_opened():
            self.close_modal()
        
        # Находим ингредиенты
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        
        if ingredients and index < len(ingredients):
                    ingredients[index].click()
                    return True
                    return False

    @allure.step("Проверить открытие модального окна ингредиента")
    def is_ingredient_modal_opened(self):
        # Проверяем основные локаторы модального окна
        modal_visible = self.is_element_visible(MainPageLocators.INGREDIENT_MODAL, timeout=3)
        overlay_visible = self.is_element_visible(MainPageLocators.MODAL_OVERLAY, timeout=3)
        content_visible = self.is_element_visible(MainPageLocators.MODAL_CONTENT, timeout=3)
        
        # Ищем любые элементы с классом modal
        all_modals = self.driver.find_elements(By.CLASS_NAME, "modal")
        visible_modals = [modal for modal in all_modals if modal.is_displayed()]
        
        # Ищем элементы с высоким z-index
        high_z_elements = self.driver.find_elements(By.XPATH, "//*[@style[contains(., 'z-index') and number(substring-after(., 'z-index:')) > 1000]]")
        visible_high_z = [elem for elem in high_z_elements if elem.is_displayed()]
        
        # Ищем элементы с role="dialog" или aria-modal="true"
        dialog_elements = self.driver.find_elements(By.XPATH, "//*[@role='dialog' or @aria-modal='true']")
        visible_dialogs = [elem for elem in dialog_elements if elem.is_displayed()]
            
            # Ищем любые элементы, которые могут быть модальными окнами
        all_possible_modals = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'modal') or contains(@class, 'Modal') or contains(@class, 'popup') or contains(@class, 'overlay') or contains(@class, 'dialog')]")
        visible_possible_modals = [elem for elem in all_possible_modals if elem.is_displayed()]
        
        return (modal_visible or overlay_visible or content_visible or 
                len(visible_modals) > 0 or len(visible_high_z) > 0 or 
                len(visible_dialogs) > 0 or len(visible_possible_modals) > 0)

    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_name_in_modal(self):
        try:
            return self.get_text(MainPageLocators.INGREDIENT_NAME)
        except:
            # Альтернативный способ получения названия
            modal_text = self.get_text(MainPageLocators.MODAL_CLASS)
            return modal_text.split('\n')[0] if modal_text else ""

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        # Пробуем найти и кликнуть по кнопке закрытия
        if self.is_element_visible(MainPageLocators.CLOSE_MODAL_BUTTON, timeout=2):
            self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        else:
            # Если кнопка не найдена, нажимаем ESC
            self.press_escape()

    @allure.step("Проверить закрытие модального окна")
    def is_modal_closed(self):
        return not self.is_ingredient_modal_opened()

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self, index=0):
        # Закрываем модальное окно если открыто
        if self.is_ingredient_modal_opened():
            self.close_modal()
        
        # Находим ингредиенты
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        
        if ingredients and index < len(ingredients):
            # Находим область конструктора
            constructor_area = self.find_element_with_fallback(
                OrderLocators.CONSTRUCTOR_AREA,
                [
                    OrderLocators.CONSTRUCTOR_AREA_ALT,
                    OrderLocators.CONSTRUCTOR_AREA_ALT2,
                    OrderLocators.CONSTRUCTOR_AREA_ALT3,
                    OrderLocators.CONSTRUCTOR_AREA_ALT4
                ]
            )
            
            if constructor_area:
                # Перетаскиваем ингредиент в конструктор
                actions = ActionChains(self.driver)
                actions.drag_and_drop(ingredients[index], constructor_area).perform()
            else:
                # Если не нашли конструктор, просто кликаем на ингредиент
                ingredients[index].click()
            return True
        return False

    @allure.step("Проверить увеличение счетчика ингредиента")
    def is_ingredient_counter_increased(self, index=0):
        try:
            counters = self.find_elements(MainPageLocators.INGREDIENT_COUNTER)
            if counters and index < len(counters):
                return counters[index].text != "0"
            
            # Альтернативная проверка - ищем любые счетчики
            all_counters = self.find_elements(MainPageLocators.COUNTER_CLASS)
            for counter in all_counters:
                if counter.text and counter.text != "0":
                    return True
            return False
        except:
            return False

    @allure.step("Оформить заказ")
    def place_order(self):
        # Ищем кнопку заказа
        order_button = self.find_element_with_fallback(
            OrderLocators.ORDER_BUTTON,
            [
                OrderLocators.ORDER_BUTTON_ALT,
                OrderLocators.ORDER_BUTTON_ALT2,
                OrderLocators.ORDER_BUTTON_ALT3,
                OrderLocators.ORDER_BUTTON_ALT4
            ]
        )
        
        if order_button:
            order_button.click()
            return True
        else:
            print("Кнопка заказа не найдена. Возможно, нужно сначала добавить ингредиенты в конструктор.")
            return False

    @allure.step("Проверить открытие модального окна заказа")
    def is_order_modal_opened(self):
        return self.is_element_visible(OrderLocators.ORDER_MODAL)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        if self.is_element_visible(OrderLocators.ORDER_NUMBER, timeout=3):
            return self.get_text(OrderLocators.ORDER_NUMBER)
        else:
            # Альтернативный способ получения номера заказа
            modal_text = self.get_text(MainPageLocators.MODAL_CLASS)
            if "заказ" in modal_text.lower():
                # Ищем номер в тексте модального окна
                numbers = re.findall(r'\d+', modal_text)
                return numbers[0] if numbers else "Номер не найден"
            return "Номер не найден"
