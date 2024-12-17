import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.page_load_strategy = 'eager'
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.chitai-gorod.ru/')
    yield browser
    browser.quit()
