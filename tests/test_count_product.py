import time

import allure
import pytest
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("browser")
class TestCheckSumProduct:
    @allure.feature('Добавление товаров в корзину')
    @allure.story('Добавление двух разных товаров в корзину')
    def test_add_product_to_cart(self, browser):
        main_page = MainPage(browser)
        main_page.search_for_product('Колобок')

        search_results_page = SearchResultsPage(browser)
        search_results_page.close_discount_popup()
        search_results_page.click_on_first_product()

        product_page = ProductPage(browser)
        product_page.add_to_cart()

        main_page.return_main_page()

        main_page.search_for_product('Гарри Поттер и Тайная комната')

        search_results_page.close_discount_popup()
        search_results_page.click_on_second_product()

        product_page.add_to_cart()

        cart_page = CartPage(browser)
        cart_page.go_to_cart()

        cart_page.check_count_product_in_cart('2 товара')
