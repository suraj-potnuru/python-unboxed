import pytest

@pytest.fixture
def user():
    return {"id": 1, "name": "Suraj"}

@pytest.fixture
def enriched_user(user):
    user["role"] = "admin"
    return user

def test_user_role(enriched_user):
    assert enriched_user["role"] == "admin"