import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_password_recovery_form_display(browser):
    # Открыть страницу восстановления пароля
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)

    # Нажать кнопку "Забыл пароль"
    forgot_password_button = browser.find_element(By.XPATH, "//a[text()='Забыл пароль']")
    forgot_password_button.click()

    # Дополнительное ожидание для отображения формы восстановления пароля
    time.sleep(20)

    # Проверить, что на странице отображается форма восстановления пароля
    assert browser.find_element(By.XPATH, "//h1[text()='Восстановление пароля']").is_displayed()

    # Проверить, что присутствует форма для ввода контактных данных
    assert browser.find_element(By.XPATH,"//input[@id='username']").is_displayed()

    # Проверить, что по умолчанию выбрана форма восстановления пароля по телефону
    assert browser.find_element(By.XPATH, "//span[text()='Мобильный телефон']").is_displayed()

    # Проверить, что на форме присутствует форма ввода для капчи
    assert browser.find_element(By.XPATH,"//input[@id='captcha']").is_displayed()

    # Проверить, что на форме присутствуют кнопки "Далее" и "Вернуться"
    assert browser.find_element(By.XPATH, "//button[contains(., 'Продолжить')]").is_displayed()
    assert browser.find_element(By.XPATH, "//button[contains(., 'Вернуться назад')]").is_displayed()
