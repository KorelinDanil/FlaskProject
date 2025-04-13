import sys


def get_mean_size():
    # Читаем все строки из stdin и пропускаем первую (заголовок)
    lines = sys.stdin.readlines()[1:]

    total_size = 0
    file_count = 0

    for line in lines:
        # Разбиваем строку по пробелам
        parts = line.split()

        # Проверяем, что строка содержит информацию о файле (обычно 9 частей)
        if len(parts) >= 9:
            try:
                size = int(parts[4])  # Размер файла в байтах (5-й столбец)
                total_size += size
                file_count += 1
            except (ValueError, IndexError):
                continue  # Пропускаем некорректные строки

    if file_count == 0:
        return "Нет файлов для подсчета среднего размера."

    mean_size = total_size / file_count
    return f"Средний размер файла: {mean_size:.2f} байт"


if __name__ == "__main__":
    print(get_mean_size())