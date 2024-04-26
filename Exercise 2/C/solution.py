# Python 3.12.1

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

ans = arr[0]
delta = abs(x - ans)

for num in arr:
    if abs(x - num) < delta:
        delta = abs(x - num)
        ans = num

print(ans)
