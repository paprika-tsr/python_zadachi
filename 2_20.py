import re


text_data = """
Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026.
Следующая встреча запланирована на 1.11.2026.
"""
date_pattern = r"\b\d{1,2}\.\d{1,2}\.\d{4}\b"
found_dates = re.findall(date_pattern, text_data)
print("Найденные даты:")
for date in found_dates:
    print(date)
