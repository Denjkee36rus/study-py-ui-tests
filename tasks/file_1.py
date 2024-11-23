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

with webdriver.Chrome() as browser:
        browser.get(url)

        # Ожидание, пока элемент станет кликабельным
        notification_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__input"]'))
            )

        # Вводим в поле значение
        notification_button.send_keys('гарри поттер')

        # Кликаем на кнопку поиска
        search_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__button"]'))
        )
        search_button.click()

        time.sleep(2)

        # Закрыть окно со скидками
        close_discount_popup = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="popmechanic-close"]')
                                       ))
        close_discount_popup.click()

        # Закрываем окно с согласием использования файлов cooke
        close_cooke_popup = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="button cookie-notice__button white"]')
                                       ))
        close_cooke_popup.click()

        # Ожидаем, пока  искомый элемент станет кликабельным
        add_product_to_cart = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="button action-button blue"]'))
            )

        # Используем JavaScript для клика
        browser.execute_script("arguments[0].click();", add_product_to_cart)
        time.sleep(3)

        # Переход в корзину
        check_product = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-cart sticky-header__controls-item"]'))
        )
        check_product.click()

        # Проверка товара в корзине
        product_in_cart = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="cart-item__title"]'))
        )

        # Проверяем, что товар с нужным названием присутствует в корзине
        assert product_in_cart.text == 'Гарри Поттер и философский камень', "Товар не найден в корзине"




        time.sleep(4)




