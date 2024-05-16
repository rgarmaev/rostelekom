import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_failed_login(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Ввести некорректный логин и некорректный пароль
    phone_input = browser.find_element(By.XPATH, "//input[@id='username']")
    phone_input.send_keys("rtkid_1715084000000")

    password_input = browser.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys("123456")

    # Нажать кнопку "Вход"
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Проверить проваленную авторизацию
    time.sleep(5)
    assert "Неверный логин или пароль" in browser.page_source

    # Проверить, что элемент "Забыл пароль" перекрашивается в оранжевый цвет
    forgot_password_link = browser.find_element(By.XPATH, "//a[contains(@class, 'rt-link--orange')]")
    assert "rgba(255, 79, 18, 1)" in forgot_password_link.value_of_css_property("color")