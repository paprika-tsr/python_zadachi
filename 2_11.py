import re


log_data = """
INFO User 123 logged in
ERROR User 456 authentication failed
WARNING User 123 changed password
ERROR User 789 authentication failed
INFO User 456 logged in
"""

all_users = re.findall(r"User (\d+)", log_data)
error_lines = re.findall(r"^ERROR.*", log_data, re.MULTILINE)
error_users = re.findall(r"^ERROR User (\d+)", log_data, re.MULTILINE)
print("Все идентификаторы пользователей:")
for user in all_users:
    print(f"  - {user}")
print("\nВсе строки с ERROR:")
for line in error_lines:
    print(f"  - {line}")
print("\nИдентификаторы пользователей с ошибкой:")
for user in error_users:
    print(f"  - {user}")
