import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_enter_phone_and_request_code(browser):
    # Открыть страницу
    browser.get("https://lk.rt.ru/")
    time.sleep(5)
    # Ввести корректный номер телефона/почту
    phone_or_email_input = browser.find_element(By.XPATH, "//input[@id='address']")
    phone_or_email_input.send_keys("+79836361806")

    # Нажать кнопку "Получить код"
    get_code_button = browser.find_element(By.XPATH, "//button[contains(., 'Получить код')]")
    get_code_button.click()

    # Запросить у пользователя, пришло ли сообщение
    time.sleep(10)
    message_received = input("Пришло ли сообщение? (yes/no): ")

    # Проверить, что система отправила код на введенный номер телефона/почту
    if message_received.lower() == "yes":
        print("Сообщение успешно получено!")
        assert True
    elif message_received.lower() == "no":
        print("Сообщение не получено!")
        assert False
    else:
        print("Некорректный ввод!")
        assert False