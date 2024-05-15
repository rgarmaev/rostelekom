import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_phone_authentication_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Нажать на таб выбора аутентификации по номеру
    browser.find_element(By.XPATH,"//div[@id='t-btn-tab-phone']").click()
    # Проверить, что форма ввода изменяется соответственно
    time.sleep(5)
    assert browser.find_element(By.XPATH,"//span[contains(text(), 'Мобильный телефон')]").is_displayed()

def test_email_authentication_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Нажать на таб выбора аутентификации по почте
    browser.find_element(By.XPATH,"//div[@id='t-btn-tab-mail']").click()
    # Проверить, что форма ввода изменяется соответственно
    time.sleep(5)
    assert browser.find_element(By.XPATH,"//span[contains(text(), 'Электронная почта')]").is_displayed()

def test_login_authentication_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Нажать на таб выбора аутентификации по логину
    browser.find_element(By.XPATH,"//div[@id='t-btn-tab-login']").click()
    # Проверить, что форма ввода изменяется соответственно
    time.sleep(5)
    assert browser.find_element(By.XPATH,"//span[contains(text(), 'Логин')]").is_displayed()

def test_account_authentication_tab(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")
    time.sleep(5)
    # Нажать на таб выбора аутентификации по лицевому счету
    browser.find_element(By.XPATH,"//div[@id='t-btn-tab-ls']").click()
    # Проверить, что форма ввода изменяется соответственно
    time.sleep(5)
    assert browser.find_element(By.XPATH,"//span[contains(text(), 'Лицевой счёт')]").is_displayed()
