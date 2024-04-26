# Python 3.12.1

n, r = map(int, input().split())

arr = list(map(int, input().split()))

pair = 0
last = 0
for first in range(n):
    while last < n and arr[last] - arr[first] <= r:
        last += 1
    pair += n - last
print(pair)
