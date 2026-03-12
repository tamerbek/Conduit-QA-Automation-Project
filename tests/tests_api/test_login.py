import pytest
import requests
from faker import Faker

#  test positive user login
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_positive_user_login_api(api_base_url):
    user_data = {"email": "conduit_test@test.com", "password": "conduit_test"}
    payload = {"user":user_data}
    response = requests.post(api_base_url + "/users/login", json = payload)

    assert response.status_code == 200
    assert response.json()["user"]["email"] == user_data["email"]
    assert response.json()["user"]["token"] is not None

