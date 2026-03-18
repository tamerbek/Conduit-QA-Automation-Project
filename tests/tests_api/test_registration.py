import pytest
from faker import Faker
import requests

fake = Faker("ru_RU")

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_user_positive_registration_api(api_base_url):
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "username": fake.name()
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    print(response.text)
    assert response.status_code == 201
    assert "token" in response.json()["user"]
    assert response.json()["user"]["token"] is not None
    assert response.json()["user"]["username"] == user_data["username"]
    assert response.json()["user"]["email"] == user_data["email"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_empty_password(api_base_url):
    user_data = {
        "email": fake.email(),
        "username": fake.name(),
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["password"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_empty_username(api_base_url):
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["username"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_empty_email(api_base_url):
    user_data = {
        "password": fake.password(),
        "username": fake.name()
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["email"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_all_fields_empty(api_base_url):
    user_data = {
        "username": "",
        "email": "",
        "password": ""
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["username"]
    assert "can't be blank" in response.json()["errors"]["email"]
    assert "can't be blank" in response.json()["errors"]["password"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_empty_body(api_base_url):
    payload = {}

    response = requests.post(api_base_url + "/users", json=payload)
    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["username"]
    assert "can't be blank" in response.json()["errors"]["email"]
    assert "can't be blank" in response.json()["errors"]["password"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_without_user_wrapper(api_base_url):
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "username": fake.name()
    }

    response = requests.post(api_base_url + "/users", json=user_data)

    assert response.status_code == 422
    assert "can't be blank" in response.json()["errors"]["username"]
    assert "can't be blank" in response.json()["errors"]["email"]
    assert "can't be blank" in response.json()["errors"]["password"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_email_100symbols(api_base_url):
    user_data = {
        "username": fake.name(),
        "email": "conduit_testconduit_testconduit_testconduit_testconduit_testconduit_testconduit_testconduit@test.com",
        "password": fake.password()
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 201
    assert response.json()["user"]["token"] is not None
    assert response.json()["user"]["username"] == user_data["username"]
    assert response.json()["user"]["email"] == "conduit_testconduit_testconduit_testconduit_testconduit_testconduit_testconduit_testconduit@test.com"


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_email_101symbol(api_base_url):
    user_data = {
        "username": fake.name(),
        "email": "conduit_testconduit_testconduit_testconduit_testconduit_testconduit_testconduit_testconduit1@test.com",
        "password": fake.password()
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 422
    print(response.text)
    assert "Email, username and password are expected as strings of length less than 100, 60, and 60, respectively" in response.json()["errors"]["body"]


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_username_60symbols(api_base_url):
    user_data = {
        "username": "usernameusernameusernameusernameusernameusernameusernameuser",
        "email": fake.email(),
        "password": fake.password()
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 201
    assert response.json()["user"]["username"] == "usernameusernameusernameusernameusernameusernameusernameuser"
    assert response.json()["user"]["email"] == user_data["email"]
    assert response.json()["user"]["token"] is not None


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_username_61symbol(api_base_url):
    user_data = {
        "username": "usernameusernameusernameusernameusernameusernameusernameuseru",
        "email": fake.email(),
        "password": fake.password()
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 422
    assert "Email, username and password are expected as strings of length less than 100, 60, and 60, respectively" in response.json()["errors"]["body"]
    print(response.text)


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_password_60symbols(api_base_url):
    user_data = {
        "username": fake.name(),
        "email": fake.email(),
        "password": "passwordpasswordpasswordpasswordpasswordpasswordpasswordpass"
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 201
    assert response.json()["user"]["username"] == user_data["username"]
    assert response.json()["user"]["email"] == user_data["email"]
    assert response.json()["user"]["token"] is not None


@pytest.mark.api
@pytest.mark.regression
def test_user_registration_password_61symbol(api_base_url):
    user_data = {
        "username": fake.name(),
        "email": fake.email(),
        "password": "passwordpasswordpasswordpasswordpasswordpasswordpasswordpassp"
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 422
    assert "Email, username and password are expected as strings of length less than 100, 60, and 60, respectively" in response.json()["errors"]["body"]
    print(response.text)