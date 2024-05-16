import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_no_temporary_code_with_incorrect_phone_number(browser):
    # Открыть страницу авторизации
    browser.get("https://lk.rt.ru/")
    time.sleep(5)

    # Ввести некорректный номер телефона
    phone_input = browser.find_element(By.XPATH, "//input[@id='address']")
    phone_input.send_keys("1234567890")  # Некорректный номер телефона

    # Нажать кнопку "Получить код"
    get_code_button = browser.find_element(By.XPATH, "//button[contains(., 'Получить код')]")
    get_code_button.click()

    # Дополнительное ожидание для отображения сообщения об ошибке
    time.sleep(5)

    # Проверить, что отображается сообщение об ошибке, указывающее на некорректность введенного номера телефона
    assert "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" in browser.page_source

    # Проверить, что код не отправляется на введенный номер телефона
    # (В этом тесте не предполагается проверка отправки кода, так как номер некорректный)

    # Проверить, что форма остается на экране
    assert browser.find_element(By.XPATH, "//input[@id='address']").is_displayed()