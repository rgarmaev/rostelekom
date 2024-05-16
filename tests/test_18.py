import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_failed_login_with_correct_phone_and_incorrect_temporary_code(browser):
    # Открыть страницу авторизации
    browser.get("https://lk.rt.ru/")
    time.sleep(5)

    # Ввести корректный номер телефона
    phone_input = browser.find_element(By.XPATH, "//input[@id='address']")
    phone_input.send_keys("+79836361806")

    # Нажать кнопку "Получить код"
    get_code_button = browser.find_element(By.XPATH, "//button[contains(., 'Получить код')]")
    get_code_button.click()

    # Дополнительное ожидание для получения кода (может потребоваться)
    time.sleep(5)

    # Ввести некорректный временный код

    # Дополнительное ожидание для отображения сообщения об ошибке
    time.sleep(30)

    # Проверить, что авторизация провалилась и отображается сообщение об ошибке "Неверный код"
    assert "Неверный код. Повторите попытку" in browser.page_source

    # Проверить, что отображается ссылка на изменение данных
    assert browser.find_element(By.XPATH, "//button[text()='Изменить номер']").is_displayed()

    # Проверить, что отображается текст обратного отсчета для повторной отправки кода
    assert browser.find_element(By.XPATH, "//span[@id='otp-code-timeout']").is_displayed()
