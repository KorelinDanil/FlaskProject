from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Оптимальное хранение дней недели (кортеж занимает меньше памяти)
WEEKDAYS = (
    "понедельника",
    "вторника",
    "среды",
    "четверга",
    "пятницы",
    "субботы",
    "воскресенья"
)

@app.route('/hello-world/<name>')
def hello_world(name):
    weekday_num = datetime.today().weekday()  # 0-6 (пн-вс)
    weekday_name = WEEKDAYS[weekday_num]
    return f"Привет, {name}. Хорошего {weekday_name}!"

if __name__ == '__main__':
    app.run(debug=True)
    # для проверки прописать в терминале: http://127.0.0.1:5000/hello-world/Маша