import pytest

from secure_app import (
    add_user,
    find_user,
    hash_password,
    setup_database,
    validate_email,
    validate_password,
    validate_username,
    verify_password,
)


@pytest.fixture
def test_database(tmp_path, monkeypatch):
    monkeypatch.setattr("secure_app.DB_NAME", str(tmp_path / "test_users.db"))
    setup_database()
    return tmp_path / "test_users.db"


def test_username_validation():
    assert validate_username("hithaish_1")
    assert not validate_username("ab")


def test_email_validation():
    assert validate_email("user@example.com")
    assert not validate_email("invalid-email")


def test_password_validation():
    assert validate_password("strongpass")
    assert not validate_password("123")


def test_password_hashing_and_verification():
    stored = hash_password("Secret123")
    assert stored != "Secret123"
    assert verify_password("Secret123", stored)
    assert not verify_password("Wrong123", stored)


def test_add_and_find_user(test_database):
    assert add_user("testuser", "Secret123", "test@example.com")
    user = find_user("testuser")
    assert user is not None
    assert user[1] == "testuser"
    assert user[2] == "test@example.com"


def test_duplicate_username(test_database):
    assert add_user("testuser", "Secret123", "test@example.com")
    assert not add_user("testuser", "Another123", "another@example.com")


def test_invalid_user_data(test_database):
    with pytest.raises(ValueError):
        add_user("ab", "Secret123", "test@example.com")
    with pytest.raises(ValueError):
        add_user("validuser", "short", "test@example.com")
    with pytest.raises(ValueError):
        add_user("validuser", "Secret123", "bad-email")
