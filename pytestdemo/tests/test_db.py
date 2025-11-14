def test_insert(db):
    db.insert("user2", {"name": "John"})
    assert db.get("user2")["name"] == "John"

def test_preloaded_value(db):
    assert db.get("user1")["name"] == "Suraj"