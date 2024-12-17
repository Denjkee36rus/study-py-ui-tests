import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON = (By.CSS_SELECTOR, '[class="header-cart sticky-header__controls-item"]')
    PRODUCT_IN_CART = (By.CSS_SELECTOR, '[class="product-title__head"]')
    COUNT_PRODUCT = (By.CSS_SELECTOR, '[class="app-title__append"]')

    def go_to_cart(self):
        with allure.step('Переходим в карзину'):
            cart_icon = self.find_clickable_element(self.CART_ICON)
            cart_icon.click()

    def check_product_in_cart(self, product_name):
        with allure.step('Прверяем, что в карзине 1 товара'):
            product_in_cart = self.find_visible_element(self.PRODUCT_IN_CART)
            assert product_in_cart.text == product_name, "Товар не найден в корзине"

    def check_count_product_in_cart(self, expected_quantity):
        with allure.step('Прверяем, что в карзине 2 товара'):
            count_product = self.find_visible_element(self.COUNT_PRODUCT)
            assert count_product.text == expected_quantity, (f'Ожидалось {expected_quantity} товаров, но найдено '
                                                             f'{count_product}')

