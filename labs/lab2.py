def ca(a, b, text, abc):
    """Цезарь, аффинный"""
    list_abc = []
    length = len(abc)
    for i in range(length):
        list_abc.append([ABC[i], abc[(i * a + b) % length]])
    # print(list_abc)  # output table
    print('Зашифрованный текст: ', end='')
    for symbol in text:
        if 1072 <= ord(symbol) < 1104 or symbol == 'ё':
            for row in list_abc:
                if symbol in row[0]:
                    print(row[1], end="")
        else:
            print(symbol, end="")
    print()


def t(b, text, abc):
    """Трисемус"""
    list_abc = []
    length = len(abc)
    for i in range(length):
        list_abc.append([abc[i], abc[(i + b) % length]])
    # print(list_abc)  # output table
    print('Зашифрованный текст: ', end='')
    for symbol in text:
        if 1072 <= ord(symbol) < 1104 or symbol == 'ё':
            for row in list_abc:
                if symbol in row[0]:
                    print(row[1], end="")
        else:
            print(symbol, end="")
    print()


def remove_duplicates(key, new_key):
    for symbol in key:
        if symbol not in new_key:
            new_key += symbol
    return new_key


def isint(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        print('Введите числовое значение')
        s = isint(input())
        return int(s)


def isstring(string):
    try:
        for i in string:
            if i not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
                int(None)
        return string
    except TypeError:
        print('Введите строку, состоящую из букв русского алфавита')
        string = isstring(input().lower())
        return string


if __name__ == "__main__":
    while True:
        ABC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        print('Режим работы:')
        print('(1)Система шифрования Цезаря')
        print('(2)Аффинная система подстановок Цезаря')
        print('(3)Система шифрования Цезаря с ключевым словом')
        print('(4)Система шифрования Трисемуса')
        case = input()
        if case == '1':
            print('Введите сообщение: ', end='')
            text = input().lower()
            print('Введите ключ: ', end='')
            b = isint(input())
            ca(1, b, text, ABC)
        elif case == '2':
            print('Введите сообщение: ', end='')
            text = input().lower()
            print('Введите a: ', end='')
            a = isint(input())
            print('Введите b: ', end='')
            b = isint(input())
            ca(a, b, text, ABC)
        elif case == '3':
            print('Введите сообщение: ', end='')
            text = input().lower()
            print('Введите ключевое слово: ', end='')
            key = isstring(input().lower())
            print('Введите ключ: ', end='')
            b = isint(input())
            new_key = ''
            new_key = remove_duplicates(key, new_key)
            new_key = remove_duplicates(ABC, new_key)
            print(new_key)
            ca(1, - b, text, new_key)
        elif case == '4':
            print('Введите сообщение: ', end='')
            text = input().lower()
            print('Введите ключевое слово: ', end='')
            key = isstring(input().lower())
            print('Введите количество столбцов: ', end='')
            b = isint(input())
            new_key = ''
            new_key = remove_duplicates(key, new_key)
            new_key = remove_duplicates(ABC, new_key).replace('ё', '')
            t(b, text, new_key)
        print('Продолжить? да/нет')
        fail_condition = input()
        if fail_condition == 'нет':
            break
