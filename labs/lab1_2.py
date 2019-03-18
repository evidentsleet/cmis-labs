def Is_magic(m):
    n = len(m)
    s = (n ** 2 + 1) * n // 2
    return (
        set(range(1, n ** 2 + 1)) == set(i for r in m for i in r) and
        all(sum(r) == s for r in (*m, *zip(*m))) and
        sum(m[i][i] for i in range(n)) == sum(m[i][-i - 1] for i in range(n)) == s)


def Encrypt(arr, key):
    text = ''
    new_arr = []
    for i in range(len(arr)):
        new_line = []
        for column in range(len(arr)):
            index = arr[i][column]
            new_line.append(key[index-1])
        new_arr.append(new_line)

    for row in range(len(arr)):
        temp_text = "".join(new_arr[row])
        text += temp_text
    print('Зашифрованное сообщение: ' + text)


def Decrypt(arr, key):
    j = 0
    new_arr = []
    for row in arr:
        for i in range(len(arr)):
            new_arr.append([row[i], key[j]])
            j += 1
    new_arr.sort(key=lambda row: row[0])
    print('Расшифрованное сообщение: ', end='')
    for row in new_arr:
        print(row[1], end='')
    print()


if __name__ == "__main__":
    while True:
        print('Введите сообщение')
        key = input()
        print('Введите разметрность')
        n = int(input())
        print('Введите матрицу построчно')
        arr = []
        for i in range(n):
            arr.append([int(j) for j in input().split()])
        # arr = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        # print(arr)
        print('Магия?', Is_magic(arr))
        print('(1)Зашифровать или (2)расшифровать?')
        if int(input()) == 1:
            Encrypt(arr, key)
        else:
            Decrypt(arr, key)
        print('Продолжить? да/нет')
        fail_condition = input()
        if fail_condition == 'нет':
            break
