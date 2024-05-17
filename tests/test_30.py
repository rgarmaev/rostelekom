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

    # Ввести данные для регистрации
    firstname = browser.find_element(By.XPATH, "//input[@name='firstName']")  # Поле ввода имени
    firstname.send_keys('Тест')
    lastname = browser.find_element(By.XPATH, "//input[@name='lastName']") # Поле ввода фамилии
    lastname.send_keys('Тестовый')
    region = browser.find_element(By.XPATH,
                                "//input[@class='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange' and @type='text']")  # Поле выбора региона
    region.send_keys('Москва г')
    email = browser.find_element(By.XPATH,
                                "//input[@id='address']")  # Поле ввода email или мобильного телефона
    email.send_keys('rinchin92@ya.ru')

    # Ввести корректный пароль
    valid_password = "validPassword123"
    password_field = browser.find_element(By.ID, "password")
    password_confirm = browser.find_element(By.ID, "password-confirm")
    password_field.clear()
    password_confirm.clear()
    password_field.send_keys(valid_password)
    password_confirm.send_keys(valid_password)
    registration_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    registration_button.click()
    time.sleep(5)

    # Проверить, что система принимает введенный пароль
    assert "Подтверждение email" in browser.page_source

    time.sleep(5)  # Для наглядности
