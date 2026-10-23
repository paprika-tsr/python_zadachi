from pathlib import Path


def read_file(path):
    file_path = Path(path)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл по пути '{path}' не найден.")
        return None
    except PermissionError:
        print(f"Ошибка: Нет прав доступа для чтения файла '{path}'.")
        return None
    except UnicodeDecodeError:
        print(f"Ошибка: Невозможно прочитать файл '{path}' (ошибка кодировки).")
        return None
    except OSError as e:
        print(f"Системная ошибка при работе с файлом '{path}': {e}")
        return None


file_content = read_file("example.txt")
if file_content is not None:
    print("\nСодержимое файла:")
    print(file_content)
