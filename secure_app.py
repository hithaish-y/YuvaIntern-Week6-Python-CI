import hashlib
import re
import secrets
import sqlite3

DB_NAME = "users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def hash_password(password: str, salt: str | None = None) -> str:
    """Return a salted PBKDF2-HMAC-SHA256 password hash."""
    if salt is None:
        salt = secrets.token_hex(16)

    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100_000
    ).hex()

    return f"{salt}${digest}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        salt, expected = stored_hash.split("$", 1)
    except ValueError:
        return False

    actual = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100_000
    ).hex()

    return secrets.compare_digest(actual, expected)


def validate_username(username: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,30}", username))


def validate_email(email: str) -> bool:
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email))


def validate_password(password: str) -> bool:
    return len(password) >= 8


def setup_database():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """
        )


def add_user(username: str, password: str, email: str) -> bool:
    if not validate_username(username):
        raise ValueError("Invalid username")

    if not validate_email(email):
        raise ValueError("Invalid email")

    if not validate_password(password):
        raise ValueError("Password must contain at least 8 characters")

    password_hash = hash_password(password)

    with get_connection() as conn:
        try:
            conn.execute(
                "INSERT INTO users "
                "(username, password_hash, email) "
                "VALUES (?, ?, ?)",
                (username, password_hash, email),
            )
        except sqlite3.IntegrityError:
            return False

    return True


def find_user(username: str):
    with get_connection() as conn:
        return conn.execute(
            "SELECT id, username, email FROM users WHERE username = ?",
            (username,),
        ).fetchone()


if __name__ == "__main__":
    setup_database()

    print("Secure User Management Application")
    print("1. Add user")
    print("2. Find user")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        username = input("Username: ").strip()
        password = input("Password: ")
        email = input("Email: ").strip()

        try:
            if add_user(username, password, email):
                print("User added successfully.")
            else:
                print("Username already exists.")

        except ValueError as exc:
            print(f"Input error: {exc}")

    elif choice == "2":
        username = input("Username: ").strip()
        user = find_user(username)

        if user:
            print(f"User: {user}")
        else:
            print("User not found.")

    else:
        print("Invalid choice.")
