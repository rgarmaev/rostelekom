import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_successful_login_with_correct_phone_and_temporary_code(browser):
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

    # Ввести полученный временный код
    # В данном тесте предполагается, что код будет автоматически введен и далее происходит переход по URL,
    # который будет представлять личный кабинет. Так что в данном тесте нет явного ввода кода.

    # Подождать некоторое время для загрузки страницы после успешной авторизации
    time.sleep(30)

    # Проверить, что авторизация прошла успешно и URL содержит путь к личному кабинету
    expected_url = "https://start.rt.ru/?tab=main"
    assert browser.current_url == expected_url