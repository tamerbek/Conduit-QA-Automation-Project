import pytest
import requests
from faker import Faker
import allure

fake = Faker("ru_RU")

#  test positive user login
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_user_positive_login_api(api_base_url):
    user_data = {
        "email": "conduit_test@test.com",
        "password": "conduit_test",
        "username": "conduit_test"
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    user_data = {"email": "conduit_test@test.com", "password": "conduit_test"}
    payload = {"user": user_data}
    response = requests.post(api_base_url + "/users/login", json = payload)

    assert response.status_code == 200
    assert response.json()["user"]["email"] == user_data["email"]
    assert response.json()["user"]["token"] is not None


@pytest.mark.api
@pytest.mark.regression
def test_user_negative_login_wrong_password(api_base_url):
    user_data = {"email": "conduit_test@test.com",
                 "password": "123"}
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users/login", json=payload)

    assert response.status_code == 401
    assert "invalid" in response.json()["errors"]["credentials"]


@pytest.mark.api
@pytest.mark.regression
def test_user_negative_login_empty_email(api_base_url):
    user_data = {"email": "", "password": fake.password()}
    payload = {"user":user_data}

    response = requests.post(api_base_url + "/users/login", json = payload)
    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["email"]


@pytest.mark.api
@pytest.mark.regression
def test_user_negative_login_empty_password(api_base_url):
    user_data = {"email": fake.email(), "password": ""}
    payload = {"user":user_data}

    response = requests.post(api_base_url + "/users/login", json = payload)
    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["password"]


@pytest.mark.api
@pytest.mark.regression
def test_user_negative_login_empty_login_and_password(api_base_url):
    user_data = {
        "email": "",
        "password": ""
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users/login", json=payload)

    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["email"]
    assert "can't be blank" in response.json()["errors"]["password"]


@pytest.mark.api
@pytest.mark.regression
def test_user_negative_login_without_body(api_base_url):
    payload = ""

    response = requests.post(api_base_url + "/users/login", json = payload)

    assert response.status_code == 422
    assert "Invalid request body" in response.json()["errors"]["body"]


@pytest.mark.api
@pytest.mark.regression
def test_user_negative_login_without_wrapper(api_base_url):
    user_data = {"email": "conduit_test@test.com",
                 "password": "conduit_test"}

    response = requests.post(api_base_url + "/users/login", json=user_data)

    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["email"]
    assert "can't be blank" in response.json()["errors"]["password"]


@pytest.mark.api
@pytest.mark.regression
def test_user_login_sql_injection_password(api_base_url):
    user_data = {"email": "conduit_test@test.com",
                 "password": "' OR '1'='1"}

    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users/login", json=payload)

    assert response.status_code == 401
    assert "invalid" in response.json()["errors"]["credentials"]

