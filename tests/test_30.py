import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_valid_password_input(browser):
    # Открыть страницу авторизации
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(10)

    # Нажать кнопку "Зарегистрироваться"
    registration_link = browser.find_element(By.XPATH, "//a[@class='rt-link rt-link--orange' and @id='kc-register']")
    registration_link.click()
    time.sleep(5)

    # Ввести корректный пароль
    valid_password = "validPassword123"
    password_field = browser.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys(valid_password)

    # Проверить, что система принимает введенный пароль
    assert password_field.get_attribute("value") == valid_password, "The entered password is not accepted by the system"

    time.sleep(5)  # Для наглядности
