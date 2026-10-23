import re


text_data = """
Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru
"""
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
all_emails = re.findall(email_pattern, text_data)
unique_emails = sorted(set(all_emails))
print("Результат:")
for email in unique_emails:
    print(email)
