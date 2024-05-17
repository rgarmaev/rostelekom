import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_password_recovery_via_email(browser):
    # Открыть страницу восстановления пароля
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)

    # Нажать кнопку "Забыл пароль"
    forgot_password_button = browser.find_element(By.XPATH, "//a[text()='Забыл пароль']")
    forgot_password_button.click()

    # Дополнительное ожидание для отображения формы восстановления пароля
    time.sleep(5)

    # Ввести корректную почту
    email_input = browser.find_element(By.XPATH, "//input[@id='username']")
    email_input.send_keys("garmaev.rinchin@gmail.com")

    # Ввести капчу
    time.sleep(20)

    # Нажать кнопку "Продолжить"
    continue_button = browser.find_element(By.XPATH, "//button[contains(., 'Продолжить')]")
    continue_button.click()
    time.sleep(5)

    # Нажать чек-бокс восстановления пароля по e-mail
    recovery_by_email_checkbox = browser.find_element(By.XPATH, "//span[@class='rt-radio__label' and text()='По e-mail']/ancestor::span[@class='rt-radio__container']")
    recovery_by_email_checkbox.click()

    # Нажать кнопку "Продолжить"
    time.sleep(5)
    continue_button_secondary = browser.find_element(By.XPATH, "//button[@id='reset-form-submit']")
    continue_button_secondary.click()


    # Вводим в форму ввода код полученный из e-mail
    time.sleep(30)

    # Переход на форму восстановления пароля
    time.sleep(5)

    # Отображается поле для ввода нового пароля
    assert browser.find_element(By.XPATH, "//input[@id='password-new']").is_displayed()

    # Отображается поле для ввода подтверждения пароля
    assert browser.find_element(By.XPATH, "//input[@id='password-confirm']").is_displayed()

    # Отображается кнопка "Сохранить"
    assert browser.find_element(By.XPATH, "//button[@id='t-btn-reset-pass']").is_displayed()
