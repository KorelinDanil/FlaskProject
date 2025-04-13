from flask import Flask, abort

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    # Разделяем строку по слешу и фильтруем пустые значения
    parts = numbers.split('/')
    num_list = []

    for part in parts:
        if not part:
            continue  # Пропускаем пустые части (например, из-за двойного слеша)

        # Проверяем, является ли часть числом (целым или дробным)
        if part.lstrip('-').replace('.', '', 1).isdigit():
            try:
                num = float(part)
                num_list.append(num)
            except ValueError:
                abort(400, description=f"Некорректное число: {part}")
        else:
            abort(400, description=f"Некорректные данные: '{part}' не является числом")

    if not num_list:
        abort(400, description="Не передано ни одного числа")

    max_num = max(num_list)

    # Проверяем, является ли число целым для красивого вывода
    if max_num.is_integer():
        max_num = int(max_num)

    return f"Максимальное число: <i>{max_num}</i>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    #curl http://localhost:5001/max_number/10/2/9/1
