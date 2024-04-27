# Python 3.9 (PyPy 7.3.11)
# Особенность в том, что здесь нужен не просто жадный алгоритм, перебирающий сначала в поисках первого максимального значения, а потом вновь перебирающий в поисках второго максимального ответа, а нужно искать максимальное значение на всей последовательности. Сперва сделал жадину и конечно же быстро попался тест, который её завалил.
# 

n = int(input())
duratation = 5

buyers = []
number = 0
for _ in range(n):
    start, end = map(int, input().split())
    if end - start < duratation:
        continue
    buyers.append((start, -1, number)) # IN
    buyers.append((end - duratation, 1, number)) # OUT
    number += 1

buyers.sort()
duratation = 5

watchers = 0
watchers_first_ad = set()
first_ad = 0
second_ad = 0

for customer in range(len(buyers)):
    if buyers[customer][1] == -1:
        watchers_first_ad.add(buyers[customer][2])

        if len(watchers_first_ad) > watchers:
            watchers = len(watchers_first_ad)
            first_ad = buyers[customer][0]
            second_ad = buyers[customer][0] + duratation
            
    cnt = 0
    for left in range(customer + 1, len(buyers)):
        if buyers[left][1] == -1:
            cnt += 1
        if buyers[left][0] - duratation >= buyers[customer][0] and len(watchers_first_ad) + cnt > watchers:
            watchers = len(watchers_first_ad) + cnt
            first_ad = buyers[customer][0]
            second_ad = buyers[left][0]
            
        if buyers[left][1] == 1 and buyers[left][2] not in watchers_first_ad:
            cnt -= 1
    if buyers[customer][1] == 1:
        watchers_first_ad.remove(buyers[customer][2])
if len(buyers) == 0:
    print(0, 10, 20)
else:
    print(watchers, first_ad, second_ad)
