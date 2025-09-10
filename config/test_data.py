"""
Тестовые данные для автотестов
"""

# ID ингредиентов для тестирования
TEST_INGREDIENT_IDS = {
    "bun": "643d69a5c3f7b9001cfa093c",
    "main": "643d69a5c3f7b9001cfa0941"
}

# Базовый список ингредиентов для заказа (булочка + основной ингредиент + булочка)
ORDER_INGREDIENTS = [
    TEST_INGREDIENT_IDS["bun"],
    TEST_INGREDIENT_IDS["main"], 
    TEST_INGREDIENT_IDS["bun"]
]
