import pytest
from faker import Faker
import requests

fake = Faker("ru_RU")

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_user_positive_registration_api(api_base_url):
    user_data = {
        "email": fake.name(),
        "password": fake.email(),
        "username": fake.password()
    }
    payload = {"user": user_data}

    response = requests.post(api_base_url + "/users", json=payload)

    assert response.status_code == 201
    assert "token" in response.json()["user"]
    assert response.json()["user"]["token"] is not None
    assert response.json()["user"]["username"] == user_data["username"]
    assert response.json()["user"]["email"] == user_data["email"]

    #  print(response.status_code)
    #  print(response.json())
    #  print(response.text)
    #  print(response.headers)
    #  print(response.url)