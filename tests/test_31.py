import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_authentication(browser):
    # Открыть страницу восстановления пароля
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(10)
    assert "Личный кабинет" in browser.page_source