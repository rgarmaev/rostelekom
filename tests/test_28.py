import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_default_region_selection(browser):
    # Открыть страницу авторизации
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(10)

    # Нажать кнопку "Зарегистрироваться"
    registration_link = browser.find_element(By.XPATH, "//a[@class='rt-link rt-link--orange' and @id='kc-register']")
    registration_link.click()
    time.sleep(5)

    # Проверить выбранный регион по умолчанию
    default_region = browser.find_element(By.XPATH,
                                          "//input[@class='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange' and @type='text']")
    assert default_region.get_attribute("value") == "Москва г", "Default region selection does not match Moscow"

    time.sleep(5)  # Для наглядности
