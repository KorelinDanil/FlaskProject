from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Хранение данных в формате: {год: {месяц: {день: сумма}}}
finance_data = {}


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    try:
        # Парсим дату
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])

        # Добавляем данные в хранилище
        finance_data.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
        finance_data[year][month][day] += number

        return f"Добавлена трата {number} руб. на дату {day}.{month}.{year}"

    except Exception as e:
        return f"Ошибка: {str(e)}", 400


@app.route('/calculate/<int:year>')
def calculate_year(year):
    try:
        total = 0
        # Суммируем все траты за год
        for month in finance_data.get(year, {}).values():
            for day_expense in month.values():
                total += day_expense

        return f"Суммарные траты за {year} год: {total} руб."

    except Exception as e:
        return f"Ошибка: {str(e)}", 400


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    try:
        total = 0
        # Суммируем траты за конкретный месяц
        for day_expense in finance_data.get(year, {}).get(month, {}).values():
            total += day_expense

        return f"Суммарные траты за {month}.{year}: {total} руб."

    except Exception as e:
        return f"Ошибка: {str(e)}", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
# Добавление траты
#curl "http://localhost:5001/add/20231015/500"

# Запрос за месяц
#curl "http://localhost:5001/calculate/2023/10"

# Запрос за год
#curl "http://localhost:5001/calculate/2023"