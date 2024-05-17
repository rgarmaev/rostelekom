import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_password_length_validation(browser):
    # Открыть страницу авторизации
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)

    # Нажать кнопку "Регистрация"
    registration_link = browser.find_element(By.ID, "kc-register")
    registration_link.click()
    time.sleep(5)

    # Заполнить форму регистрации
    browser.find_element(By.NAME, "firstName").send_keys("Иван")
    browser.find_element(By.NAME, "lastName").send_keys("Иванов")
    browser.find_element(By.XPATH, "//input[@class='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange' and @type='text']").send_keys("Москва")
    browser.find_element(By.ID, "address").send_keys("example@example.com")
    browser.find_element(By.ID, "password").send_keys("passwor")  # Пароль длиной 7 символов
    browser.find_element(By.ID, "password-confirm").send_keys("passwor")
    browser.find_element(By.NAME, "register").click()
    time.sleep(5)

    # Проверить отображение сообщения об ошибке под полем "Пароль"
    error_message = browser.find_element(By.XPATH, "//span[text()='Длина пароля должна быть не менее 8 символов']").text
    assert error_message == "Длина пароля должна быть не менее 8 символов"

