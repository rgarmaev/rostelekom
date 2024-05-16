import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Ввести корректную почту и пароль
    phone_input = browser.find_element(By.XPATH, "//input[@id='username']")
    phone_input.send_keys("garmaev.rinchin@gmail.com")

    password_input = browser.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys("Test1234")

    # Нажать кнопку "Вход"
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Проверить успешную авторизацию
    time.sleep(5)
    assert browser.find_element(By.XPATH, "//a[@id='lk-btn']").is_displayed()