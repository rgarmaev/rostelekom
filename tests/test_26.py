import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_registration_form_display(browser):
    # Открыть страницу авторизации
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(10)

    # Нажать кнопку "Зарегистрироваться"
    registration_link = browser.find_element(By.XPATH, "//a[@class='rt-link rt-link--orange' and @id='kc-register']")
    registration_link.click()
    time.sleep(5)

    # Проверить переход на страницу регистрации
    expected_url_part = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration"
    actual_url = browser.current_url
    assert expected_url_part in actual_url, f"Expected URL part: {expected_url_part}, Actual URL: {actual_url}"

    # Проверить отображение формы регистрации
    assert browser.find_element(By.XPATH, "//h1[text()='Регистрация']").is_displayed()

    # Проверить поля формы регистрации
    assert browser.find_element(By.XPATH, "//input[@name='firstName']").is_displayed()  # Поле ввода имени
    assert browser.find_element(By.XPATH, "//input[@name='lastName']").is_displayed()  # Поле ввода фамилии
    assert browser.find_element(By.XPATH, "//input[@class='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange' and @type='text']").is_displayed()  # Поле выбора региона
    assert browser.find_element(By.XPATH, "//input[@id='address']").is_displayed()  # Поле ввода email или мобильного телефона
    assert browser.find_element(By.XPATH, "//input[@id='password']").is_displayed()  # Поле ввода пароля
    assert browser.find_element(By.XPATH, "//input[@id='password-confirm']").is_displayed()  # Поле подтверждения пароля
    assert browser.find_element(By.XPATH, "//button[@type='submit']").is_displayed()  # Кнопка "Продолжить"


