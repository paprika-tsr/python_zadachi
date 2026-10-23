import re


def is_valid_login(login):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{3,15}$"
    return bool(re.match(pattern, login))


test_logins = [
    "user_123",
    "admin",
    "123user",
    "ab",
    "user-name",
    "very_long_username",
]
for login in test_logins:
    print(f"{login:20} -> {is_valid_login(login)}")
