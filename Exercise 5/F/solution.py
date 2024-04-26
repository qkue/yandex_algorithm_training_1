# Python 3.12.1

n = int(input())
classes = list(map(int, input().split()))
m = int(input())
arr_m = [tuple(map(int, input().split())) for _ in range(m)]
arr_m.sort(key = lambda x: (x[1], x[0]))
classes.sort()
result = 0
last = 0
for first in range(n):
    cnt = 0
    while last < m and arr_m[last][0] < classes[first]:
        last += 1
        
    result += arr_m[last][1]

print(result)
