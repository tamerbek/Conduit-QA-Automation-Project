import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

#  positive test for user login
@allure.epic("Пользователи")
@allure.feature("Логин пользователя")
@allure.title("Успешный логин пользователя")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_user_positive_login(browser, ui_base_url, wait):
    browser.get(ui_base_url + '/login')

    with allure.step("Шаг 1: Ожидаем появления полей email, password и кнопки submit"):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']"))).send_keys("conduit_test@test.com")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='password']"))).send_keys("conduit_test")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']"))).click()

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/profile/']")))
    profile_name = element.text.strip()
    assert profile_name == "conduit_test"

@pytest.mark.ui
@pytest.mark.regression
def test_user_login_needaccount_button(browser, ui_base_url, wait):
    browser.get(ui_base_url + "/login")

    register_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.text-xs-center a[href='/register']")))
    assert register_link.is_displayed()

    register_link.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']")))
    assert "/register" in browser.current_url