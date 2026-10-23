from pathlib import Path


dir_input = input("Каталог: ").strip()
ext_input = input("Расширение: ").strip()
directory = Path(dir_input)
if not directory.exists():
    print(f"Ошибка: Каталог '{dir_input}' не существует.")
elif not directory.is_dir():
    print(f"Ошибка: Путь '{dir_input}' не является каталогом.")
else:
    if not ext_input.startswith("."):
        ext_input = f".{ext_input}"
    print(f"\nРезультаты поиска в '{directory.resolve()}':")
    found_any = False
    for file in directory.rglob(f"*{ext_input}"):
        if file.is_file():
            found_any = True
            file_size = file.stat().st_size
            print(f"  - {file} ({file_size} байт)")
    if not found_any:
        print(f"Файлы с расширением '{ext_input}' не найдены.")
