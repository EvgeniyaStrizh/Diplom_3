from selenium.webdriver.common.by import By


class MainPageLocators:
    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'ingredient-item')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter')]")
    
    # Конструктор
    CONSTRUCTOR_TAB = (By.XPATH, "//span[text()='Булки']")
    CONSTRUCTOR_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'constructor-element')]")
    
    # Кнопка заказа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.CLASS_NAME, "modal")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'order-number')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'close-button')]")
    
    # Модальное окно ингредиента - обновленные локаторы
    INGREDIENT_MODAL = (By.CLASS_NAME, "modal")
    INGREDIENT_NAME = (By.XPATH, "//h3[contains(@class, 'ingredient-name')]")
    INGREDIENT_CALORIES = (By.XPATH, "//p[contains(@class, 'calories')]")
    INGREDIENT_PROTEINS = (By.XPATH, "//p[contains(@class, 'proteins')]")
    INGREDIENT_FAT = (By.XPATH, "//p[contains(@class, 'fat')]")
    INGREDIENT_CARBOHYDRATES = (By.XPATH, "//p[contains(@class, 'carbohydrates')]")
    
    # Альтернативные локаторы для модального окна
    MODAL_OVERLAY = (By.CLASS_NAME, "modal-overlay")
    MODAL_CONTENT = (By.CLASS_NAME, "modal-content")
    
    # Локаторы для конструктора
    CONSTRUCTOR_AREA = (By.CLASS_NAME, "constructor-area")
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'buns-section')]")
    SAUCE_SECTION = (By.XPATH, "//div[contains(@class, 'sauce-section')]")
    MAIN_SECTION = (By.XPATH, "//div[contains(@class, 'main-section')]")
