import csv


def filtration_csv(file, result_file='expensive.csv'):
    try:
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            #reader.fieldnames = [name.strip() for name in reader.fieldnames]
            with open(result_file, 'w') as res_f:
                writer = csv.DictWriter(res_f, fieldnames=reader.fieldnames)
                writer.writeheader()
                for i in reader:
                    price = int(i['price'].strip())
                    if price > 100:
                        writer.writerow(i)

        print(f"фильтрация CSV завершена. данные сохранены в '{result_file}'.")

    except FileNotFoundError:
        print(f"ошибка: файл '{file}' не найден.")


filtration_csv('products.csv')
