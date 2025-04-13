import pytest
from freezegun import freeze_time
from datetime import datetime


def get_weekday_greeting(name: str) -> str:
    """Возвращает приветствие с текущим днём недели"""
    weekdays = {
        0: "понедельника",
        1: "вторника",
        2: "среды",
        3: "четверга",
        4: "пятницы",
        5: "субботы",
        6: "воскресенья"
    }
    today = datetime.today().weekday()
    return f"Привет, {name}. Хорошего {weekdays[today]}!"


# Тесты
def test_greeting_contains_correct_weekday():
    """Проверяем, что функция возвращает корректный день недели"""
    test_cases = [
        ("2023-01-02", "понедельника"),  # Понедельник
        ("2023-01-03", "вторника"),  # Вторник
        ("2023-01-04", "среды"),  # Среда
        ("2023-01-05", "четверга"),  # Четверг
        ("2023-01-06", "пятницы"),  # Пятница
        ("2023-01-07", "субботы"),  # Суббота
        ("2023-01-08", "воскресенья"),  # Воскресенье
    ]

    for date, expected_day in test_cases:
        with freeze_time(date):
            result = get_weekday_greeting("Тест")
            assert expected_day in result, f"Ожидался {expected_day}, получено: {result}"


def test_greeting_with_custom_username():
    """Проверяем обработку разных имён"""
    with freeze_time("2023-01-02"):  # Фиксируем понедельник
        assert "Привет, Иван. Хорошего понедельника!" == get_weekday_greeting("Иван")
        assert "Привет, Мария. Хорошего понедельника!" == get_weekday_greeting("Мария")
        assert "Хорошего понедельника!" in get_weekday_greeting("Хорошей среды")


def test_all_days_covered():
    """Проверяем, что все дни недели обрабатываются"""
    weekdays = {"понедельника", "вторника", "среды", "четверга", "пятницы", "субботы", "воскресенья"}
    result_days = set()

    # Проверяем все дни в течение недели
    for day in range(7):
        with freeze_time(f"2023-01-0{day + 2}"):  # 2-8 января 2023 - полная неделя
            result = get_weekday_greeting("Тест")
            day_name = result.split()[-1].replace("!", "")
            result_days.add(day_name)

    assert weekdays == result_days, f"Не все дни недели обработаны: {weekdays - result_days}"