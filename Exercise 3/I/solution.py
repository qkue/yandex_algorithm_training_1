# Python 3.12.1

n = int(input())
all_set = {input() for _ in range(1) for _ in range(int(input()))}
all_know = all_set.copy()

for _ in range(n-1):
    temp = set()
    for _ in range(int(input())):
        lang = input()
        temp.add(lang)
        all_set.add(lang)
    all_know &= temp

print(len(all_know))
if all_know:
    print(*all_know, sep = '\n')
print(len(all_set))
print(*all_set, sep = '\n')
