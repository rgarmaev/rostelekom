import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_invalid_email_or_phone_input(browser):
    # Открыть страницу авторизации
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(10)

    # Нажать кнопку "Зарегистрироваться"
    registration_link = browser.find_element(By.XPATH, "//a[@class='rt-link rt-link--orange' and @id='kc-register']")
    registration_link.click()
    time.sleep(5)

    # Ввести некорректный email или телефон
    invalid_input = "8962304"
    input_field = browser.find_element(By.ID, "address")
    input_field.clear()
    input_field.send_keys(invalid_input)
    registration_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    registration_button.click()

    # Проверить сообщение об ошибке
    error_message = browser.find_element(By.XPATH, "//span[text()='Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru']")
    assert error_message.is_displayed(), "Error message for invalid email or phone input is not displayed"

    time.sleep(5)  # Для наглядности
