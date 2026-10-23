import re


products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321",
]
pattern = r"^PRD-\d{5}$"
correct_products = [prod for prod in products if re.match(pattern, prod)]
print(correct_products)
