import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_change_password_and_authentication(browser):
    # Открыть страницу восстановления пароля
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)

    # Нажать кнопку "Забыл пароль"
    forgot_password_button = browser.find_element(By.XPATH, "//a[text()='Забыл пароль']")
    forgot_password_button.click()

    # Дополнительное ожидание для отображения формы восстановления пароля
    time.sleep(20)

    # Ввести корректный номер телефона
    phone_input = browser.find_element(By.XPATH, "//input[@id='username']")
    phone_input.send_keys("+79836361806")

    # Ввести капчу
    time.sleep(20)

    # Нажать кнопку "Продолжить"
    continue_button = browser.find_element(By.XPATH, "//button[contains(., 'Продолжить')]")
    continue_button.click()

    # Нажать чек-бокс восстановления пароля по номеру телефона
    time.sleep(5)
    recovery_by_phone_checkbox = browser.find_element(By.XPATH, "//span[@class='rt-radio__label' and text()='По номеру телефона']")
    recovery_by_phone_checkbox.click()

    # Нажать кнопку "Продолжить"
    time.sleep(5)
    continue_button_secondary = browser.find_element(By.XPATH, "//button[@id='reset-form-submit']")
    continue_button_secondary.click()

    # Вводим в форму ввода код полученный из SMS
    time.sleep(25)

    # Вводим в форму ввода новый пароль
    new_password_input = browser.find_element(By.XPATH, "//input[@id='password-new']")
    new_password_input.send_keys("Test_1234")

    # Вводим в форму ввода подтверждение нового пароля
    confirm_password_input = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    confirm_password_input.send_keys("Test_1234")

    # Нажать кнопку "Сохранить"
    save_button = browser.find_element(By.XPATH, "//button[@id='t-btn-reset-pass']")
    save_button.click()

    # Проверяем, что переход на страницу авторизации прошел успешно
    time.sleep(15)
    expected_url_part = "https://b2c.passport.rt.ru/"
    assert expected_url_part in browser.current_url
    time.sleep(5)

    # Вводим номер телефона (или email) и пароль
    username_input = browser.find_element(By.XPATH, "//input[@id='username']")
    username_input.send_keys("+79836361806")

    password_input = browser.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys(str(new_password_input))

    # Нажимаем кнопку "Войти"
    login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
    login_button.click()

    # Проверяем, что авторизация удалась c новым паролем
    time.sleep(25)
    assert "Личный кабинет" in browser.page_source
