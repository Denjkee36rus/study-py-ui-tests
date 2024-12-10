from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[class="product-offer-button chg-app-button '
                                           'chg-app-button--primary chg-app-button--extra-large '
                                           'chg-app-button--brand-blue chg-app-button--block"]')

    def add_to_cart(self):
        add_to_cart_button = self.find_clickable_element(self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
