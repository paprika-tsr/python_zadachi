import re


text = "Это   строка    с       большим      количеством   пробелов.  "
cleaned_text = re.sub(r"\s+", " ", text)
result = cleaned_text.strip()
print(f'"{result}"')
