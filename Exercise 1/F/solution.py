# Python 3.12.1

f1, f2, s1, s2 = map(int, input().split())
notebook_1 = [f1, f2]
notebook_2 = [s1, s2]
best = []
best_s = 10 ** 9

for first in range(len(notebook_1)):
    for second in range(len(notebook_2)):
        length = (notebook_1[first-1] + notebook_2[second - 1])
        heigth = max(notebook_1[first], notebook_2[second])
        t = length * heigth
        if t < best_s:
            best_s = t
            best = [length, heigth]

print(*best)
