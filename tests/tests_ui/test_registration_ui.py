from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration(browser, ui_base_url, wait):

    browser.get(ui_base_url + "/register")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='username']"))).send_keys("conduit_test")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']"))).send_keys("conduit_test@test.com")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='password']"))).send_keys("conduit_test")
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/profile/']")))
    profile_name = element.text.strip()
    assert profile_name == "conduit_test"