
import sqlite3
import hashlib
import hmac
import os
import getpass

DB_NAME = "users.db"


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    password_hash = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=16384,
        r=8,
        p=1
    )

    return salt, password_hash


def initialize_database():
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                salt BLOB NOT NULL,
                password_hash BLOB NOT NULL
            )
        """)


def register_user(username, password):
    salt, password_hash = hash_password(password)

    try:
        with sqlite3.connect(DB_NAME) as connection:
            connection.execute(
                "INSERT INTO users (username, salt, password_hash) "
                "VALUES (?, ?, ?)",
                (username, salt, password_hash)
            )
        print("Registration successful.")

    except sqlite3.IntegrityError:
        print("Username already exists.")


def login(username, password):
    with sqlite3.connect(DB_NAME) as connection:
        user = connection.execute(
            "SELECT salt, password_hash FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    if user is None:
        print("Invalid username or password.")
        return

    salt, stored_hash = user
    _, entered_hash = hash_password(password, salt)

    if hmac.compare_digest(entered_hash, stored_hash):
        print("Login successful.")
    else:
        print("Invalid username or password.")


def main():
    initialize_database()

    print("SECURE LOGIN DEMO")
    print("1. Register")
    print("2. Login")

    choice = input("Choose an option: ").strip()
    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    password = getpass.getpass("Enter password: ")

    if not password:
        print("Password cannot be empty.")
        return

    if choice == "1":
        register_user(username, password)
    elif choice == "2":
        login(username, password)
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
