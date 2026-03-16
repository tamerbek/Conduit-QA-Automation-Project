import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_user_positive_post_new_article(browser, ui_base_url, wait):
    browser.get(ui_base_url + '/login')

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']"))).send_keys("conduit_test@test.com")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='password']"))).send_keys("conduit_test")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']"))).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[routerlink='/editor']"))).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='title']"))).send_keys("New test article")