import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  postitive test for user registration
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_user_positive_registration(browser, ui_base_url, wait):
    browser.get(ui_base_url)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-signup"))).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='username']"))).send_keys("conduit_test")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']"))).send_keys("conduit_test@test.com")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='password']"))).send_keys("conduit_test")
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/profile/']")))
    profile_name = element.text.strip()
    assert profile_name == "conduit_test"


@pytest.mark.ui
@pytest.mark.regression
def test_user_registration_empty_password(browser, ui_base_url, wait):
    browser.get(ui_base_url + "/register")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='username']"))).send_keys("conduit_test")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']"))).send_keys("conduit_test@test.com")

    assert not wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).is_enabled()


@pytest.mark.ui
@pytest.mark.regression
def test_user_registration_empty_email(browser, ui_base_url, wait):
    browser.get(ui_base_url + "/register")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='username']"))).send_keys("conduit_test")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='password']"))).send_keys("conduit_test")

    assert not wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).is_enabled()


@pytest.mark.ui
@pytest.mark.regression
def test_user_registration_empty_username(browser, ui_base_url, wait):
    browser.get(ui_base_url + "/register")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']"))).send_keys("conduit_test@test.com")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='password']"))).send_keys("conduit_test")

    assert not wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).is_enabled()


@pytest.mark.ui
@pytest.mark.regression
def test_user_registration_haveaccount_button(browser, ui_base_url, wait):
    browser.get(ui_base_url + "/register")

    login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.text-xs-center a[href='/login']")))
    assert login_link.is_displayed()

    login_link.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']")))
    assert "/login" in browser.current_url
