from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, '[class="header-search__input"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[class="header-search__button"]')

    def search_for_product(self, product_name):
        search_input = self.find_visible_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(product_name)
        search_button = self.find_clickable_element(self.SEARCH_BUTTON)
        search_button.click()
