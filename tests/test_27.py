import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_name_field_validation(browser):
    # Открыть страницу авторизации
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(10)

    # Нажать кнопку "Зарегистрироваться"
    registration_link = browser.find_element(By.XPATH, "//a[@class='rt-link rt-link--orange' and @id='kc-register']")
    registration_link.click()
    time.sleep(5)

    # Ввести в поле имени менее 2 символов
    name_input = browser.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys("Ab")
    registration_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    registration_button.click()
    time.sleep(5)
    # Проверить сообщение об ошибке
    error_message = browser.find_element(By.XPATH, "//span[text()='Необходимо заполнить поле кириллицей. От 2 до 30 символов.']")
    assert error_message.is_displayed(), "Error message is not displayed for invalid name input"
    assert error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", "Incorrect error message for invalid name input"

    time.sleep(5)  # Для наглядности
