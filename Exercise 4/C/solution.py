# Python 3.12.1

with open('input.txt', 'rt', encoding='utf-8') as file:
    text = file.read().split()

word_dict = {}

for word in text:
    if word not in word_dict:
        word_dict[word] = 0
    #print(word_dict[word], end=' ')
    word_dict[word] += 1

word_list = []
count = 0

for key, val in word_dict.items():
    if val > count:
        word_list = [key]
        count = val
    elif val == count:
        word_list.append(key)

word_list.sort()
print(word_list[0])
