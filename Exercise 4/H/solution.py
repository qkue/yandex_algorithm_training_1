# Python 3.9 (PyPy 7.3.11

from sys import stdin

g, s = map(int, stdin.readline().strip().split())
w = stdin.readline().rstrip()
seq = stdin.readline().rstrip()

result = 0

#создаём словарь из искомого слова
main_key = {}
for char in w:
    if char not in main_key:
        main_key[char] = 0
    main_key[char] += 1

#создаём словарь из первого слова в последовательности
window_dict = {}
for char in seq[:g]:
    if char not in window_dict:
        window_dict[char] = 0
    window_dict[char] += 1

#сверяем сходства обоих словарей
matches = 0
for k in main_key:
    if k in window_dict and main_key[k] == window_dict[k]:
        matches += 1

#если совпадения выявили в первом слове искомое слово
if matches == len(main_key):
    result += 1

# основной цикл по установлению слов
ind = 0
for char in seq[g:]:
    # удаление символа из начала строки
    temp = seq[ind]
    if temp in main_key and main_key[temp] == window_dict[temp]:
        matches -= 1
    window_dict[temp] -= 1
    if temp in main_key and main_key[temp] == window_dict[temp]:
        matches += 1

    # прибавление символа к концу строки
    if char not in window_dict:
        window_dict[char] = 0
    if char in main_key and main_key[char] == window_dict[char]:
        matches -= 1
    window_dict[char] += 1
    if char in main_key and main_key[char] == window_dict[char]:
        matches += 1


    if matches == len(main_key):
        result += 1
    ind += 1


print(result)
