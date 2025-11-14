from unittest.mock import MagicMock
from src.db_simple import create_user


def test_create_user_success():
    mock_db_client = MagicMock()
    mock_db_client.insert_user.return_value = True

    result = create_user(mock_db_client, 1, "Suraj")

    assert result is True