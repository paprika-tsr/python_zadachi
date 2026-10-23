from pathlib import Path


def analyze_directory(path):
    directory = Path(path)
    files_count = 0
    subdirs_count = 0
    for i in directory.iterdir():
        if i.is_file():
            files_count += 1
        elif i.is_dir():
            subdirs_count += 1
    py_files = [str(file) for file in directory.rglob("*.py")]
    total_size = sum(f.stat().st_size for f in directory.rglob("*") if f.is_file())
    print(f"количество файлов: {files_count}")
    print(f"количество подкаталогов: {subdirs_count}")
    print("\nсписок всех `.py` файлов:")
    if py_files:
        for py_file in py_files:
            print(f"  - {py_file}")
    else:
        print("файлы .py не найдены")

    print(f"\nсуммарный размер всех файлов: {total_size} байт")


folder_path = "/Users/aitanatserenova/Downloads"
analyze_directory(folder_path)
