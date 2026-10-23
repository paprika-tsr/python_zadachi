filename = "large_numbers.txt"
total_sum = 0
count = 0
min_value = None
max_value = None
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        if not clean_line:
            continue
        number = int(clean_line)
        total_sum += number
        count += 1
        if min_value is None or number < min_value:
            min_value = number
        if max_value is None or number > max_value:
            max_value = number
average = total_sum / count if count > 0 else 0
print(f"Количество чисел: {count}")
if count > 0:
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {min_value}")
    print(f"Максимум: {max_value}")
    print(f"Среднее: {average:.2f}")
else:
    print("Файл пуст.")
