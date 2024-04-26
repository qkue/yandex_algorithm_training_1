# Python 3.12.1

w, h, n = map(int, input().split())

left = 0
right = 10 ** 14

while left < right:
    m = (left + right) // 2
    if ((m // w) * (m // h)) >= n:
        right = m
    else:
        left = m + 1

print(left)
