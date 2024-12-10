from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON = (By.CSS_SELECTOR, '[class="header-cart sticky-header__controls-item"]')
    PRODUCT_IN_CART = (By.CSS_SELECTOR, '[class="product-title__head"]')

    def go_to_cart(self):
        cart_icon = self.find_clickable_element(self.CART_ICON)
        cart_icon.click()

    def check_product_in_cart(self, product_name):
        product_in_cart = self.find_visible_element(self.PRODUCT_IN_CART)
        assert product_in_cart.text == product_name, "Товар не найден в корзине"