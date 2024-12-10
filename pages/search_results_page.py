from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[class="products-list"] [class="product-title__head"]')
    DISCOUNT_POPUP_CLOSE = (By.CSS_SELECTOR, '[class="popmechanic-close"]')

    def close_discount_popup(self):
        close_discount_popup = self.find_clickable_element(self.DISCOUNT_POPUP_CLOSE)
        close_discount_popup.click()

    def click_on_product(self):
        product_title = self.find_clickable_element(self.PRODUCT_TITLE)
        actions = ActionChains(self.browser)
        actions.move_to_element(product_title).perform()
        product_title.click()
