from flask import Flask
import os
from pathlib import Path

app = Flask(__name__)


# Создаём тестовые файлы при запуске
def create_test_files():
    test_dir = Path("test_files")
    test_dir.mkdir(exist_ok=True)

    # Простой текстовый файл
    (test_dir / "simple.txt").write_text("hello world!", encoding="utf-8")

    # Многострочный файл
    (test_dir / "multiline.txt").write_text(
        "Первая строка\nВторая строка\nТретья строка",
        encoding="utf-8"
    )

    # Большой файл (1000 символов)
    (test_dir / "large.txt").write_text("A" * 1000, encoding="utf-8")


@app.route('/preview/<int:size>/<path:relative_path>')
def file_preview(size, relative_path):
    try:
        abs_path = os.path.abspath(relative_path)

        if not os.path.exists(abs_path):
            return f"Файл {abs_path} не найден", 404

        if not os.path.isfile(abs_path):
            return f"{abs_path} не является файлом", 400

        with open(abs_path, 'r', encoding='utf-8') as file:
            preview_text = file.read(size)
            actual_size = len(preview_text)

        return (f"<b>{abs_path}</b> {actual_size}<br>"
                f"{preview_text}")

    except Exception as e:
        return f"Ошибка при обработке файла: {str(e)}", 500


if __name__ == '__main__':
    create_test_files()  # Создаём тестовые файлы
    print("Тестовые файлы созданы в папке 'test_files'")
    app.run(host='0.0.0.0', port=5002, debug=True)