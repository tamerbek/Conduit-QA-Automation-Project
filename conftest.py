import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from faker import Faker
import time

fake = Faker()

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()

@pytest.fixture
def ui_base_url():
    return "https://demo.realworld.show"

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)