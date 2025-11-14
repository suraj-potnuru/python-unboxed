import pytest
from src.db import FakeDB

@pytest.fixture
def db():
    db = FakeDB()
    db.insert("user1", {"name": "Suraj"})
    return db