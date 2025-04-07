from flask import Flask
from datetime import datetime, timedelta
import random
import os
import re

app = Flask(__name__)

# ------------------------- Глобальные переменные -------------------------
cars_list = ["Chevrolet", "Renault", "Ford", "Lada"]
cats_breeds = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
counter_visits = 0  # Для /counter

# Для /get_random_word
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

# Загружаем слова из файла один раз при старте сервера
with open(BOOK_FILE, 'r', encoding='utf-8') as file:
    text = file.read()
    words = re.findall(r'\b[а-яА-ЯёЁ]+\b', text)  # Только русские слова без пунктуации

# ------------------------- Эндпоинты -------------------------

# 1. /hello_world
@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"

# 2. /cars
@app.route('/cars')
def cars():
    return ", ".join(cars_list)

# 3. /cats
@app.route('/cats')
def cats():
    return random.choice(cats_breeds)

# 4. /get_time/now
@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Точное время: {current_time}"

# 5. /get_time/future
@app.route('/get_time/future')
def get_time_future():
    future_time = (datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")
    return f"Точное время через час будет {future_time}"

# 6. /get_random_word
@app.route('/get_random_word')
def get_random_word():
    return random.choice(words)

# 7. /counter
@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return f"Страница открыта {counter_visits} раз(а)"

# ------------------------- Запуск сервера -------------------------
if __name__ == '__main__':
    app.run(debug=True)