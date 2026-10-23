def parse_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)


user_input = input("Введите число: ").strip()
try:
    result = parse_number(user_input)
    print(f"Успешное преобразование! Число: {result}")
except ValueError:
    print(f"Ошибка: Значение '{user_input}' не является корректным числом.")
