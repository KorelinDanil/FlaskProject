import sys
def decrypt(encrypted: str) -> str:
    result = []
    i = 0
    n = len(encrypted)

    while i < n:
        if encrypted[i] == '.':
            if i + 1 < n and encrypted[i + 1] == '.':
                # Две точки: удаляем предыдущий символ (если есть)
                if result:
                    result.pop()
                i += 2  # Пропускаем обе точки
            else:
                # Одна точка: оставляем предыдущий символ (точку удаляем)
                i += 1  # Пропускаем точку
        else:
            # Обычный символ (буква, пробел и т.д.)
            result.append(encrypted[i])
            i += 1

    return ''.join(result)


if __name__ == "__main__":
    # Чтение ввода из stdin (для работы в конвейере)
    input_data = sys.stdin.read().strip()
    print(decrypt(input_data))