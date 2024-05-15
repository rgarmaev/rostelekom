import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Тест для проверки автоматической смены таба на "Телефон" при вводе номера телефона
def test_automatic_phone_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Ввести корректный номер телефона
    phone_input = browser.find_element(By.XPATH, "//input[@id='username']")
    phone_input.send_keys("1234567890")
    phone_input.send_keys(Keys.TAB)
    # Проверить, что таб выбора авторизации автоматически сменился на "Телефон"
    time.sleep(5)
    assert browser.find_element(By.XPATH, "//span[contains(text(), 'Мобильный телефон')]").is_displayed()


# Тест для проверки автоматической смены таба на "Почта" при вводе почты
def test_automatic_email_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Ввести корректную почту
    email_input = browser.find_element(By.XPATH, "//input[@id='username']")
    email_input.send_keys("example@example.com")
    email_input.send_keys(Keys.TAB)
    # Проверить, что таб выбора авторизации автоматически сменился на "Почта"
    time.sleep(5)
    assert browser.find_element(By.XPATH, "//span[contains(text(), 'Электронная почта')]").is_displayed()


# Тест для проверки автоматической смены таба на "Логин" при вводе логина
def test_automatic_login_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)

    # Ввести корректный логин
    login_input = browser.find_element(By.XPATH, "//input[@id='username']")
    login_input.send_keys("my_login")
    login_input.send_keys(Keys.TAB)
    # Проверить, что таб выбора авторизации автоматически сменился на "Логин"
    time.sleep(5)
    assert browser.find_element(By.XPATH, "//span[contains(text(), 'Логин')]").is_displayed()


# Тест для проверки автоматической смены таба на "Лицевой счет" при вводе лицевого счета
def test_automatic_account_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)

    # Ввести корректный лицевой счет
    account_input = browser.find_element(By.XPATH, "//input[@id='username']")
    account_input.send_keys("423456789101")
    account_input.send_keys(Keys.TAB)
    # Проверить, что таб выбора авторизации автоматически сменился на "Лицевой счет"
    time.sleep(5)
    assert browser.find_element(By.XPATH, "//span[contains(text(), 'Лицевой счёт')]").is_displayed()
