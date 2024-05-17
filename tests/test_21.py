import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_display_password_recovery_form(browser):
    # 1. Перейти на страницу восстановления пароля
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # 2. Нажать на кнопку "Забыл пароль"
    forgot_password_button = browser.find_element(By.XPATH, "//a[text()='Забыл пароль']")
    forgot_password_button.click()

    # 3. Ввести корректный номер телефона
    phone_input = browser.find_element(By.XPATH, "//input[@id='username']")
    phone_input.send_keys("+79836361806")

    # 4. Ввести капчу (если требуется)
    time.sleep(20)

    # 5. Нажать кнопку "Продолжить"
    continue_button = browser.find_element(By.XPATH, "//button[contains(., 'Продолжить')]")
    continue_button.click()

    # Ожидаемые результаты:
    # - Отображается чек-бокс "По номеру телефона"
    assert browser.find_element(By.XPATH, "//span[@class='rt-radio__label' and text()='По номеру телефона']").is_displayed()

    # - Отображается чек-бокс "По e-mail"
    assert browser.find_element(By.XPATH, "//span[@class='rt-radio__label' and text()='По e-mail']").is_displayed()

    # - Присутствует кнопка "Продолжить"
    assert browser.find_element(By.XPATH, "//button[contains(., 'Продолжить')]").is_displayed()

    # - Присутствует кнопка "Вернуться назад"
    assert browser.find_element(By.XPATH, "//button[contains(., 'Вернуться назад')]").is_displayed()
