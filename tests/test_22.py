import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_password_recovery_by_sms(browser):
    # Открыть страницу восстановления пароля
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)

    # Нажать кнопку "Забыл пароль"
    forgot_password_button = browser.find_element(By.XPATH, "//a[text()='Забыл пароль']")
    forgot_password_button.click()

    # Дополнительное ожидание для отображения формы восстановления пароля
    time.sleep(10)

    # Ввести корректный номер телефона
    phone_input = browser.find_element(By.XPATH, "//input[@id='username']")
    phone_input.send_keys("+79836361806")

    # Ввести капчу
    time.sleep(20)

    # Нажать кнопку "Продолжить"
    continue_button = browser.find_element(By.XPATH, "//button[contains(., 'Продолжить')]")
    continue_button.click()
    time.sleep(5)
    # Нажать чек-бокс восстановления пароля по номеру телефона
    recovery_by_phone_checkbox = browser.find_element(By.XPATH, "//span[@class='rt-radio__label' and text()='По номеру телефона']")
    recovery_by_phone_checkbox.click()

    # Нажать кнопку "Продолжить"
    time.sleep(5)
    continue_button_secondary = browser.find_element(By.XPATH, "//button[@id='reset-form-submit']")
    continue_button_secondary.click()

    # Вводим в форму ввода код полученный из SMS
    time.sleep(25)

    # Проверить, что отображается поле для ввода нового пароля
    assert browser.find_element(By.XPATH, "//input[@id='password-new']").is_displayed()

    # Проверить, что отображается поле для ввода подтверждения пароля
    assert browser.find_element(By.XPATH, "//input[@id='password-confirm']").is_displayed()

    # Проверить, что отображается кнопка "Сохранить"
    assert browser.find_element(By.XPATH, "//button[@id='t-btn-reset-pass']").is_displayed()
