from selenium.webdriver.common.by import By


class MainPageLocators:
    # Ингредиенты - более гибкие локаторы
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient') and not(contains(@class, 'menuContainer'))]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter') or contains(@class, 'num') or contains(@class, 'count')]")
    
    # Конструктор
    CONSTRUCTOR_TAB = (By.XPATH, "//span[text()='Булки']")
    CONSTRUCTOR_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'constructor-element')]")
    
    # Кнопка заказа - более гибкий локатор
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'заказ') or contains(text(), 'Оформить') or contains(text(), 'Оформить заказ') or contains(@class, 'order') or contains(@class, 'button')]")
    ORDER_BUTTON_ALT = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_BUTTON_ALT2 = (By.XPATH, "//button[contains(text(), 'заказ')]")
    ORDER_BUTTON_ALT3 = (By.XPATH, "//button[contains(@class, 'order')]")
    ORDER_BUTTON_ALT4 = (By.XPATH, "//button[contains(@class, 'Order')]")
    
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
    CONSTRUCTOR_AREA_ALT = (By.XPATH, "//div[contains(@class, 'constructor')]")
    CONSTRUCTOR_AREA_ALT2 = (By.XPATH, "//div[contains(@class, 'Constructor')]")
    CONSTRUCTOR_AREA_ALT3 = (By.XPATH, "//div[contains(@class, 'burger-constructor')]")
    CONSTRUCTOR_AREA_ALT4 = (By.XPATH, "//div[contains(@class, 'BurgerConstructor')]")
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'buns-section')]")
    SAUCE_SECTION = (By.XPATH, "//div[contains(@class, 'sauce-section')]")
    MAIN_SECTION = (By.XPATH, "//div[contains(@class, 'main-section')]")
    
    # Дополнительные локаторы для ингредиентов - более гибкие
    CLICKABLE_INGREDIENT = (By.XPATH, "//div[contains(@class, 'ingredient') and (@tabindex='0' or @role='button' or @onclick)]")
    MODAL_CLASS = (By.CLASS_NAME, "modal")
    COUNTER_CLASS = (By.XPATH, "//div[contains(@class, 'counter') or contains(@class, 'num') or contains(@class, 'count')]")
    MODAL_POPUP_OVERLAY = (By.XPATH, "//*[contains(@class, 'modal') or contains(@class, 'popup') or contains(@class, 'overlay') or contains(@class, 'Modal')]")
    
    # Альтернативные локаторы для ингредиентов
    INGREDIENT_ALTERNATIVE = (By.XPATH, "//div[contains(@class, 'BurgerIngredient') or contains(@class, 'ingredient')]")
    ANY_CLICKABLE_ELEMENT = (By.XPATH, "//div[@tabindex='0' or @role='button' or @onclick]")
    
    # Дополнительные локаторы для поиска модальных окон
    MODAL_CLASS_NAME = "modal"
    HIGH_Z_INDEX_ELEMENTS = (By.XPATH, "//*[@style[contains(., 'z-index') and number(substring-after(., 'z-index:')) > 1000]]")
    DIALOG_ELEMENTS = (By.XPATH, "//*[@role='dialog' or @aria-modal='true']")
    POSSIBLE_MODAL_ELEMENTS = (By.XPATH, "//*[contains(@class, 'modal') or contains(@class, 'Modal') or contains(@class, 'popup') or contains(@class, 'overlay') or contains(@class, 'dialog')]")