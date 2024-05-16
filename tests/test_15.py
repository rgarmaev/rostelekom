import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_authorization_form_display(browser):
    # Открыть страницу
    browser.get("https://b2c.passport.rt.ru/")

    # Проверить отображение формы авторизации по коду
    phone_or_email_input = browser.find_element(By.ID, "phone-email")
    assert phone_or_email_input.is_displayed()

    get_code_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Получить код')]")
    assert get_code_button.is_displayed()