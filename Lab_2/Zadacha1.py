import os
home_dir = os.path.expanduser('~')  # Получаем путь к домашней папке (~)
file_path = os.path.join(home_dir, 'output_file.txt')  # Собираем полный путь
def get_summary_rss(fp: str) -> str:
    total_rss_kb = 0

    with open(fp, 'r') as file:
        lines = file.readlines()[1:]  # Пропускаем заголовок

        for line in lines:
            columns = line.split()
            rss_kb = int(columns[5])  # RSS находится в 6-м столбце (индекс 5)
            total_rss_kb += rss_kb

    # Переводим килобайты в байты (1 KB = 1024 B)
    total_rss_bytes = total_rss_kb * 1024

    # Определяем подходящую единицу измерения
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0

    while total_rss_bytes >= 1024 and unit_index < len(units) - 1:
        total_rss_bytes /= 1024
        unit_index += 1

    return f"{total_rss_bytes:.2f} {units[unit_index]}"

summary = get_summary_rss(file_path)
print(f"Total RSS: {summary}")