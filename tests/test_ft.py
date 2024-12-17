import time
import pytest
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import allure



@pytest.mark.usefixtures("browser")
class TestFT:
    @allure.feature('add_one_product')
    def test_add_product_to_cart(self, browser):
        # Вбиваем в строку поиска, на главной страницы, искомый товар
        main_page = MainPage(browser)
        main_page.search_for_product('Гарри Поттер и философский камень')

        # Закрываем попап скидок и выбираем искомый продукт
        search_results_page = SearchResultsPage(browser)
        search_results_page.close_discount_popup()
        search_results_page.click_on_first_product()

        # Добавляем товар в карзину
        product_page = ProductPage(browser)
        product_page.add_to_cart()

        # Проверяем наличие товара в карзине
        cart_page = CartPage(browser)
        cart_page.go_to_cart()
        cart_page.check_product_in_cart('Гарри Поттер и философский камень')

