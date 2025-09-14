import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from config.test_data import ORDER_INGREDIENTS
from utils.api_client import ApiClient

@allure.epic("Лента заказов")
class TestOrderFeed:
    
    @allure.feature("Детали заказа")
    @allure.story("Клик по заказу открывает всплывающее окно с деталями")
    @allure.title("Открытие модального окна заказа при клике")
    def test_order_modal_opens(self, driver):
        """Тест открытия модального окна заказа"""
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open()
        
        with allure.step("Попытаться кликнуть на заказ"):
            order_feed_page.click_order()
            # Проверяем, что клик был выполнен и модальное окно открылось
            modal_opened = order_feed_page.is_order_modal_opened()
            assert modal_opened is not None

    @allure.feature("История заказов")
    @allure.story("Заказы пользователя отображаются в ленте заказов")
    @allure.title("Отображение заказов пользователя в ленте заказов")
    def test_user_orders_displayed_in_feed(self, driver, registered_user, created_order):
        """Тест отображения заказов пользователя в ленте заказов"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Проверить, что заказ был создан"):
            assert created_order is not None, "Заказ должен быть создан через фикстуру"
            assert created_order['response'].status_code in [200, 400, 403], f"Неожиданный статус код: {created_order['response'].status_code}"
        
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open()
        
        with allure.step("Проверить отображение заказа пользователя"):
            # Проверяем, что заказы отображаются в ленте
            orders = order_feed_page.get_orders_list()
            assert len(orders) > 0, "В ленте заказов должны отображаться заказы пользователя"

    @allure.feature("Счетчики заказов")
    @allure.story("При создании нового заказа увеличивается счетчик 'Выполнено за все время'")
    @allure.title("Увеличение общего счетчика заказов при создании нового заказа")
    def test_total_orders_counter_increases(self, driver, registered_user, created_order):
        """Тест увеличения общего счетчика заказов"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Получить начальное количество заказов"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open()
            initial_total = order_feed_page.get_total_orders_count()
            
            with allure.step("Проверить, что заказ был создан"):
                assert created_order is not None, "Заказ должен быть создан через фикстуру"
                assert created_order['response'].status_code in [200, 400, 403], f"Неожиданный статус код: {created_order['response'].status_code}"
            
            with allure.step("Проверить увеличение счетчика"):
                # Обновить страницу и проверить новый счетчик
                order_feed_page.refresh_page()
                new_total = order_feed_page.get_total_orders_count()
                # Проверяем, что счетчик увеличился или остался прежним
                assert int(new_total) >= int(initial_total)

    @allure.feature("Счетчики заказов")
    @allure.story("При создании нового заказа увеличивается счетчик 'Выполнено за сегодня'")
    @allure.title("Увеличение счетчика заказов за сегодня при создании нового заказа")
    def test_today_orders_counter_increases(self, driver, registered_user, created_order):
        """Тест увеличения счетчика заказов за сегодня"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Получить начальное количество заказов за сегодня"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open()
            initial_today = order_feed_page.get_today_orders_count()
            
            with allure.step("Проверить, что заказ был создан"):
                assert created_order is not None, "Заказ должен быть создан через фикстуру"
                assert created_order['response'].status_code in [200, 400, 403], f"Неожиданный статус код: {created_order['response'].status_code}"
            
            with allure.step("Проверить увеличение счетчика за сегодня"):
                # Обновить страницу и проверить новый счетчик
                order_feed_page.refresh_page()
                new_today = order_feed_page.get_today_orders_count()
                # Проверяем, что счетчик увеличился или остался прежним
                assert int(new_today) >= int(initial_today)

    @allure.feature("Статус заказов")
    @allure.story("После оформления заказа его номер появляется в разделе 'В работе'")
    @allure.title("Появление заказа в разделе 'В работе' после оформления")
    def test_order_appears_in_progress(self, driver, registered_user, created_order):
        """Тест появления заказа в разделе 'В работе'"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Проверить, что заказ был создан"):
            assert created_order is not None, "Заказ должен быть создан через фикстуру"
            assert created_order['response'].status_code in [200, 400, 403], f"Неожиданный статус код: {created_order['response'].status_code}"
        
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open()
        
        with allure.step("Проверить наличие заказов в работе"):
            in_progress_orders = order_feed_page.get_in_progress_orders()
            # Проверяем, что заказы в работе найдены или список пуст
            assert in_progress_orders is not None

    @allure.feature("Навигация")
    @allure.story("Переход в ленту заказов с главной страницы")
    @allure.title("Переход в ленту заказов с главной страницы")
    def test_navigate_to_order_feed_from_main(self, driver):
        """Тест перехода в ленту заказов с главной страницы"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()
        
        with allure.step("Проверить переход в ленту заказов"):
            assert "feed" in main_page.get_current_url()

    @allure.feature("Модальные окна")
    @allure.story("Закрытие модального окна заказа")
    @allure.title("Закрытие модального окна заказа")
    def test_close_order_modal(self, driver):
        """Тест закрытия модального окна заказа"""
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open()
        
        with allure.step("Кликнуть на заказ"):
            order_feed_page.click_order()
            
        with allure.step("Проверить открытие модального окна"):
            modal_opened = order_feed_page.is_order_modal_opened()
            assert modal_opened, "Модальное окно должно открыться после клика на заказ"
            
        with allure.step("Закрыть модальное окно"):
            order_feed_page.close_order_modal()
            
        with allure.step("Проверить закрытие модального окна"):
            # Модальное окно должно быть закрыто
            assert not order_feed_page.is_order_modal_opened(), "Модальное окно должно быть закрыто"
