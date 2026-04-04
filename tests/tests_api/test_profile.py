import pytest
import requests

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_get_profile_positive(api_base_url, auth_headers):
    user_data = {
        "email": "conduit_test@test.com",
        "password": "conduit_test",
        "username": "conduit_test"
    }
    payload = {"user": user_data}
    login_response = requests.post(api_base_url + "/users", json=payload)
    token = login_response.json()["user"]["token"]

    response = requests.get(api_base_url + "/profiles/conduit_test", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["profile"]["username"] == user_data["username"]

@pytest.mark.api
@pytest.mark.regression
def test_get_profile_unauthorized(api_base_url):
    response = requests.get(api_base_url + "/profiles/conduit_test")

    assert response.status_code == 404
    assert "not found" in response.json()["errors"]["profile"]

@pytest.mark.api
@pytest.mark.regression
def test_get_profile_wrong_token(api_base_url):
    headers = {"Authorization": f"Token token_f2259a88075638eb5c7aaa7a77c5ed60"}
    response = requests.get(api_base_url + "/profiles/conduit_test", headers=headers)

    assert response.status_code == 404
    assert "not found" in response.json()["errors"]["profile"]