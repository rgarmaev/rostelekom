import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_password_change_via_email_and_phone(browser):
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
    email_input.send_keys("example@example.com")

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
    time.sleep(20)

    # Переход на форму ввода нового пароля
    time.sleep(5)

    # Ввод нового пароля и его подтверждение
    new_password_input = browser.find_element(By.XPATH, "//input[@id='password-new']")
    confirm_password_input = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    new_password_input.send_keys("Test_1234")
    confirm_password_input.send_keys("Test_1234")

    # Нажать кнопку "Сохранить"
    save_button = browser.find_element(By.XPATH, "//button[@id='t-btn-reset-pass']")
    save_button.click()
    time.sleep(5)

    # Проверить переход на страницу авторизации
    expected_url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/required-action?execution=UPDATE_PASSWORD&client_id=account_b2c&tab_id=S2JD2kGUxR4"
    assert expected_url in browser.current_url

    # Вводим номер телефона (или email) и пароль
    username_input = browser.find_element(By.XPATH, "//input[@id='username']")
    username_input.send_keys("garmaev.rinchin@gmail.com")

    password_input = browser.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys(str(new_password_input))

    # Нажимаем кнопку "Войти"
    login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
    login_button.click()

    # Проверяем, что авторизация удалась c новым паролем
    time.sleep(15)
    assert "Личный кабинет" in browser.page_source