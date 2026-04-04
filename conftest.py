import pytest
import requests
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
def api_base_url():
    return "https://api.realworld.show/api"

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)

@pytest.fixture()
def auth_token(api_base_url):
    requests.post(api_base_url + "/users", json={"user": {
        "email": "conduit_test@test.com",
        "password": "conduit_test",
        "username": "conduit_test"
    }})

    response = requests.post(api_base_url + "/users/login", json={"user": {
        "email": "conduit_test@test.com",
        "password": "conduit_test"
    }})
    return response.json()["user"]["token"]

@pytest.fixture()
def auth_headers(auth_token):
    return {"Authorization": f"Token {auth_token}"}