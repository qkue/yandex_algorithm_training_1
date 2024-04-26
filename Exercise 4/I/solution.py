# Python 3.12.1

from sys import stdin

dict_set = {}
for _ in range(int(stdin.readline())):
    t = stdin.readline().rstrip()
    if t.lower() not in dict_set:
        dict_set[t.lower()] = list()
    dict_set[t.lower()] += [t]
#print(dict_set)


result = 0

for word in stdin.readline().split():
    if word.lower() in dict_set:
        if word not in dict_set[word.lower()]:
            result += 1
    else:
        temp = 0
        for char in word:
            temp += char.isupper()
        result += (temp == 0 or temp > 1) #(temp > 1) + (temp == 0)
print(result)
