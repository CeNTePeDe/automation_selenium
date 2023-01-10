import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function') # по умолчанию всегда function
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install()) # если браузер установлен, то будет браться из кеша
    driver.maximize_window()
    yield driver
    driver.quit()





