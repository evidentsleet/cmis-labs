def clear_text(text):
    new_text = ''
    for symbol in text:
        if 1072 <= ord(symbol) < 1104:
            new_text += symbol
    return new_text


def check_nearby(text):
    for i in range(1, len(text), 2):
        if text[i] in text[i-1]:
            return True


def remove_duplicates(key, new_key):
    for symbol in key:
        if symbol not in new_key:
            new_key += symbol
    return new_key


def isstring(string):
    try:
        for i in string:
            if i not in ABC:
                int(None)
        return string
    except TypeError:
        print('Введите строку, состоящую из букв русского алфавита')
        string = isstring(input().lower())
        return string


def allint(string):
    try:
        int(string)
        print('Введите строку, в которой есть буквы русского алфавита')
        string = allint(input().lower())
        return string
    except ValueError:
        return string


def encipher_pair(key, a, b):
    arow, acol = int(key.index(a) / 8), key.index(a) % 8
    brow, bcol = int(key.index(b) / 8), key.index(b) % 8
    if arow == brow:
        return (key[arow * 8 + (acol + 1) % 8] +
                key[brow * 8 + (bcol + 1) % 8])
    elif acol == bcol:
        return (key[(arow + 1) % 4 * 8 + acol] +
                key[(brow + 1) % 4 * 8 + bcol])
    else:
        return (key[arow * 8 + bcol] +
                key[brow * 8 + acol])


def decipher_pair(key, a, b):
    arow, acol = int(key.index(a) / 8), key.index(a) % 8
    brow, bcol = int(key.index(b) / 8), key.index(b) % 8
    if arow == brow:
        return (key[arow * 8 + (acol - 1) % 8] +
                key[brow * 8 + (bcol - 1) % 8])
    elif acol == bcol:
        return (key[(arow - 1) % 4 * 8 + acol] +
                key[(brow - 1) % 4 * 8 + bcol])
    else:
        return (key[arow * 8 + bcol] +
                key[brow * 8 + acol])


def encipher(key, string):
    ret = ''
    for c in range(0, len(string), 2):
        ret += encipher_pair(key, string[c], string[c + 1])
    return ret


def decipher(key, string):
    ret = ''
    for c in range(0, len(string), 2):
        ret += decipher_pair(key, string[c], string[c + 1])
    return ret


if __name__ == "__main__":
    while True:
        ABC = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        text = ''
        while True:
            print('Введите сообщение: ', end='')
            text = allint(input().lower())
            text = clear_text(text)
            if len(text) % 2 == 1:
                print('Текст должен иметь четное количество букв')
                continue
            if check_nearby(text):
                print('Введите текст без биграмм, ', end='')
                print('содержащих две одинаковые буквы.')
                continue
            break
        print('Введите ключевое слово: ', end='')
        key = isstring(input().lower())
        new_key = ''
        new_key = remove_duplicates(key, new_key)
        new_key = remove_duplicates(ABC, new_key)
        print('(1)Зашифровать или (2)расшифровать? ', end='')
        case = input()
        if case == '1':
            print('Зашифрованный текст:', encipher(new_key, text))
        elif case == '2':
            print('Расшифрованный текст:', decipher(new_key, text))
        print('Продолжить? да/нет')
        fail_condition = input()
        if fail_condition == 'нет':
            break
