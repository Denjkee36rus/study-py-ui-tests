import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    FIRST_PRODUCT_TITLE = (By.CSS_SELECTOR, '[class="product-picture__img _loaded lazyloaded"]')
    SECOND_PRODUCT_TITLE = (By.CSS_SELECTOR, '[class="product-picture__img _loaded ls-is-cached lazyloaded"]')
    DISCOUNT_POPUP_CLOSE = (By.CSS_SELECTOR, '[class="popmechanic-close"]')

    def close_discount_popup(self):
        with allure.step('Закрываем попап скидок и выбираем искомый  первый продукт'):
            close_discount_popup = self.find_clickable_element(self.DISCOUNT_POPUP_CLOSE)
            close_discount_popup.click()

    def click_on_first_product(self):
        product_title = self.find_clickable_element(self.FIRST_PRODUCT_TITLE)
        actions = ActionChains(self.browser)
        actions.move_to_element(product_title).perform()
        product_title.click()

    def click_on_second_product(self):
        product_title = self.find_clickable_element(self.SECOND_PRODUCT_TITLE)
        actions = ActionChains(self.browser)
        actions.move_to_element(product_title).perform()
        product_title.click()

