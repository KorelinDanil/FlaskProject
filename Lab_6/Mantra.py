import random
import time


def generate_excuse():
    excuses = [
        "У меня сломался интернет в самый ответственный момент!",
        "Моя кошка села на клавиатуру и удалила весь код...",
        "Я думал, что дедлайн — завтра...",
        "Компилятор взбунтовался и отказался работать!",
        "Мой хомяк бежал в колесе и отключил электричество!",
        "Мой ноутбук решил, что сегодня день обновлений...",
    ]
    return random.choice(excuses)


def dramatic_typing(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def main():
    print("\033[36m")
    dramatic_typing("Уважаемый преподаватель...")
    time.sleep(1)
    dramatic_typing("Я искренне пытался сделать эту лабу, но...")
    time.sleep(1.5)

    excuse = generate_excuse()
    dramatic_typing(f"ВСЁ ИСПОРТИЛО ТО, ЧТО {excuse.upper()}")
    time.sleep(2)

    dramatic_typing("Поэтому умоляю...")
    time.sleep(1)
    dramatic_typing("Пожалуйста, не снижайте балл слишком сильно! 😭")
    print("\033[0m")

    import sys
    if "--please" in sys.argv:
        print("\n(Преподаватель смягчился и снизил балл всего на 10%! 🎉)")


if __name__ == "__main__":
    main()