# Python 3.12.1
# Кажется, задача должна решаться так(потому что первоначальное решение подходит под следующую задачу :-)), хотя и для понимания функция search_second_max гораздо сложнее и пока писал десятки раз путался в количестве индексов

binary = []

#добавление корня дерева
def root(binary, x):
    binary = [x, [None, None]]
    return binary

#добавление нового элемента дерева
def ad_in_binary(binary, x):
    key=binary[0]
    if x < key:
        if binary[1][0] == None:
            binary[1][0] = [x, [None, None]]
        else:
            ad_in_binary(binary[1][0], x)
    if x > key:
        if binary[1][1] == None:
            binary[1][1] = [x, [None, None]]
        else:
            ad_in_binary(binary[1][1], x)               
    return binary
s = list(map(int, input().split()))

binary = root(binary, s[0])
i = 1

while s[i] != 0:
    binary = ad_in_binary(binary, s[i])
    i = i + 1
pre_ans = []
def search_second_max(binary):
    root = binary[0]
    if binary[1][1] is not None: # если есть правая ветвь, идём по ней
        while binary[1][1][1][1]:
            root = binary[1][1][0]
            binary = binary[1][1]
        if binary[1][1][1][0]: # если последнее звено имеет левую ветвь
            root = binary[1][1][1][0][0]
            binary = binary[1][1][1][0]
            while binary[1][1]:
                root = binary[1][1][0]
                binary = binary[1][1]
            return root
        else: # в противном случае выводим корень
            return root

    elif binary[1][0][1][1] is None: # если у левой ветки нет правых веток
        return binary[1][0][0]
    else: # по левой ветке и проходим по правой до упора
        root = binary[1][0][0]
        binary = binary[1][0]
        while binary[1][1][1][1]:
            root = binary[1][1][0]
            binary = binary[1][1]
        return binary[1][1][0]

print(search_second_max(binary))
