def isstring(string):
    try:
        ABC = string_abc()
        for i in string:
            if not (i in ABC or i in ['–', ',', '.', ' ']):
                int(None)
        return string
    except TypeError:
        print('Введите строку, состоящую из букв русского алфавита, без цифр')
        string = isstring(input().upper())
        return string


def string_abc():
    abc = ''
    for i in range(1040, 1072):
        abc += chr(i)
    return abc


def clear_text(text):
    new_text = ''
    for symbol in text:
        if 1040 <= ord(symbol) < 1072:
            new_text += symbol
    return new_text


def encipher(key, string):
    ABC = string_abc()
    string = clear_text(string)
    ret = ''
    for (i, c) in enumerate(string):
        i = i % len(key)
        ret += ABC[(ABC.index(c) + ABC.index(key[i])) % 32]
    return ret


def decipher(key, string):
    ABC = string_abc()
    string = clear_text(string)
    ret = ''
    for (i, c) in enumerate(string):
        i = i % len(key)
        ret += ABC[(ABC.index(c) - ABC.index(key[i])) % 32]
    return ret

# Шифр Вижинера


if __name__ == "__main__":
    while True:
        print('Введите сообщение: ', end='')
        text = isstring(input().upper())
        print('Введите ключевое слово: ', end='')
        key = isstring(input().upper())
        print('(1)Зашифровать или (2)расшифровать? ', end='')
        case = input()
        if case == '1':
            print('Зашифрованный текст:', encipher(key, text))
        elif case == '2':
            print('Расшифрованный текст:', decipher(key, text))
        print('Продолжить? да/нет')
        fail_condition = input()
        if fail_condition == 'нет':
            break
