import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.page_load_strategy = 'eager'
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.chitai-gorod.ru/')
    yield browser
    browser.quit()


@pytest.mark.usefixtures("browser")
class TestFT:
    def test_search_product(self, browser):
        # Ожидание, пока элемент станет кликабельным
        search_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__input"]'))
        )

        # Вводим в поле значение
        search_input.send_keys('Гарри Поттер и философский камень')

        # Кликаем на кнопку поиска
        search_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__button"]'))
        )
        search_button.click()

    def test_close_popups(self, browser):
        # Закрыть окно со скидками
        close_discount_popup = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="popmechanic-close"]'))
        )
        close_discount_popup.click()

        # Закрываем окно с согласием использования файлов cooke
        close_cooke_popup = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="button cookie-notice__button white"]'))
        )
        close_cooke_popup.click()

    def test_add_product_to_cart(self, browser):

        # Ожидание, пока элемент станет кликабельным
        search_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="header-search__input"]'))
        )
        search_input.clear()

        # Вводим в поле значение
        search_input.send_keys('Гарри Поттер и философский камень')

        # Кликаем на кнопку поиска
        search_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__button"]'))
        )
        search_button.click()

        # Закрыть окно со скидками
        close_discount_popup = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="popmechanic-close"]'))
        )
        close_discount_popup.click()

        # Ожидаем, пока искомый элемент станет кликабельным
        add_product_to_cart = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="products-list"] [class="button action-button blue"]'))
        )
        actions = ActionChains(browser)

        # Выполняем скролл до элемента
        actions.move_to_element(add_product_to_cart).perform()
        add_product_to_cart.click()

    def test_check_cart(self, browser):
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
