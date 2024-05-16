import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_authorization_form_display(browser):
    # Открыть страницу
    browser.get("https://lk.rt.ru/")
    time.sleep(5)
    # Проверить отображение формы авторизации по коду
    phone_or_email_input = browser.find_element(By.XPATH, "//input[@id='address']")
    assert phone_or_email_input.is_displayed()

    get_code_button = browser.find_element(By.XPATH, "//button[contains(., 'Получить код')]")
    assert get_code_button.is_displayed()