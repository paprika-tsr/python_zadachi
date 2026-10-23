from collections import Counter
import json
import logging
import re


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log_pattern = re.compile(
    r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "  
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) "
    r"([A-Z]+) " 
    r"(\S+) " 
    r"(\d{3})"
)
method_stats = Counter()
url_stats = Counter()
errors_4xx_count = 0
filename = "access.log"
output_json = "stats.json"
logging.info(f"Начало обработки файла '{filename}'...")
try:
    with open(filename, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            clean_line = line.strip()
            if not clean_line:
                continue
            match = log_pattern.match(clean_line)
            if match:
                ip, method, url, status_code = match.groups()
                method_stats[method] += 1
                url_stats[url] += 1
                if status_code.startswith("4"):
                    errors_4xx_count += 1
            else:
                logging.warning(f"Строка {line_num} не соответствует формату лога")
    most_frequent_url = (url_stats.most_common(1)[0][0] if url_stats else "Нет данных")
    result_data = {
        "requests_by_method": dict(method_stats),
        "errors_4xx_total": errors_4xx_count,
        "most_frequent_url": most_frequent_url,
    }
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(result_data, json_file, indent=4, ensure_ascii=False)
    logging.info(f"Обработка успешно завершена. Статистика сохранена в '{output_json}'")

except FileNotFoundError:
    logging.error(f"Файл '{filename}' не найден для чтения.")
except PermissionError:
    logging.error(f"Недостаточно прав для чтения файла '{filename}' или записи результатов.")
except OSError as e:
    logging.error(f"Системная ошибка ввода-вывода при обработке: {e}")
