# Python 3.12.1
# Задача действительно легкая, без каких-либо камней :)

n, x, y = map(int, input().split())

if x > y:
    x, y = y, x

left = 0
right = n * y

while left < right:
    m = (left + right) // 2
    if m // x + m // y >= n - 1:
        right = m
    else:
        left = m + 1

print(left + x)
