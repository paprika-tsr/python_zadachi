import re


text_data = """
Мои контакты: +7 999 123-45-67 и 8 999 123-45-67.
Также можно звонить на +7 (999) 123-45-67 или 8 (999) 123-45-67.
Рабочий телефон: 123-45-67.
"""
phone_pattern = r"(?:\+7|8)\s?(?:\d{3}|\(\d{3}\))\s?\d{3}-\d{2}-\d{2}"
found_phones = re.findall(phone_pattern, text_data)
print("Найденные номера:")
for phone in found_phones:
    print(f"  - {phone}")
