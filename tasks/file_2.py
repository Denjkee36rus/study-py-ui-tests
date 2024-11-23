import os
import time

import allure
from assertpy import assert_that
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Загрузка переменных окружения
load_dotenv()

url = 'https://www.chitai-gorod.ru/'

class Test:
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)

    def search_product(self, product_name):
        # Ожидание, пока элемент станет кликабельным
        notification_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__input"]'))
        )

        # Вводим в поле значение
        notification_button.send_keys(product_name)

        # Кликаем на кнопку поиска
        search_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__button"]'))
        )
        search_button.click()



    def close_popups(self):
        # Закрыть окно со скидками
        close_discount_popup = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="popmechanic-close"]'))
        )
        close_discount_popup.click()

        # Закрываем окно с согласием использования файлов cooke
        close_cooke_popup = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="button cookie-notice__button white"]'))
        )
        close_cooke_popup.click()

    def add_product_to_cart(self):
        # Ожидаем, пока искомый элемент станет кликабельным
        add_product_to_cart = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="button action-button blue"]'))
        )

        # Используем JavaScript для клика
        self.browser.execute_script("arguments[0].click();", add_product_to_cart)


    def check_cart(self, product_name):
        # Переход в корзину
        check_product = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-cart sticky-header__controls-item"]'))
        )
        check_product.click()

        # Проверка товара в корзине
        product_in_cart = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="cart-item__title"]'))
        )

        # Проверяем, что товар с нужным названием присутствует в корзине
        assert product_in_cart.text == product_name, "Товар не найден в корзине"


# Создаем экземпляр класса и выполняем тест
test = ChitaiGorodTest(url)
test.search_product('Гарри Поттер и философский камень')
test.close_popups()
test.add_product_to_cart()
test.check_cart('Гарри Поттер и философский камень')