from collections import Counter
import re

log_pattern = re.compile(
    r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ([A-Z]+) User (\d+)"
)
log_stats = Counter()
error_users = set()

with open("app.log", "r", encoding="utf-8") as file:
    for line in file:
        match = log_pattern.match(line)
        if match:
            log_type = match.group(1)
            user_id = match.group(2)
            log_stats[log_type] += 1
            if log_type == "ERROR":
                error_users.add(user_id)
print(f"INFO: {log_stats['INFO']}")
print(f"WARNING: {log_stats['WARNING']}")
print(f"ERROR: {log_stats['ERROR']}")
print("\nПользователи, для которых встречались ошибки:")
if error_users:
    for user in sorted(error_users, key=int):
        print(f"  - User {user}")
else:
    print("  - Ошибок не обнаружено")
