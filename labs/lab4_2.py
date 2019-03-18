def check_alphabet(string, key):
    try:
        for i in string:
            if i not in key:
                int(None)
        return string
    except TypeError:
        print('Введите строку, состоящую из букв русского ', end='')
        print('алфавита, или символов ":", ",", "."')
        string = check_alphabet(input().lower(), key)
        return string


def cipher_pair(key1, key2, a, b):
    arow, acol = key1.index(a) // 5, key1.index(a) % 5
    brow, bcol = key2.index(b) // 5, key2.index(b) % 5
    if arow == brow:
        return (key2[arow * 5 + acol] +
                key1[brow * 5 + bcol])
    else:
        return (key2[arow * 5 + bcol] +
                key1[brow * 5 + acol])


def cipher(key1, key2, string):
    ret = ''
    for c in range(0, len(string), 2):
        ret += cipher_pair(key1, key2, string[c], string[c + 1])
    return ret

# Шифр «двойной квадрат» Уитстона


if __name__ == "__main__":
    while True:
        key1 = 'жщнюритьцбяме.свыпч :дуокзэфгшха,лъ'
        key2 = 'ичгят,жьмозюрвщц:пелъан.хэксшдбфуы '
        print('Введите сообщение: ', end='')
        text = input().lower().replace('й', 'и')
        text = check_alphabet(text, key1)
        if len(text) % 2 == 1:
            text += ' '
        print('(1)Зашифровать или (2)расшифровать? ', end='')
        case = input()
        if case == '1':
            print('Зашифрованный текст:', cipher(key1, key2, text))
        elif case == '2':
            print('Расшифрованный текст:', cipher(key2, key1, text))
        print('Продолжить? да/нет')
        fail_condition = input()
        if fail_condition == 'нет':
            break
