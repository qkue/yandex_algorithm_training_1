# Python 3.12.1

with open('input.txt', 'rt', encoding='utf-8') as file:
    text = file.read().split()

word_dict = {}

for word in text:
    if word not in word_dict:
        word_dict[word] = 0
    print(word_dict[word], end=' ')
    word_dict[word] += 1
