# Python 3.12.1

n, a, b, w, h = map(int, input().split())

left = 0
right = 10 ** 18
while left < right:
    m = (left + right + 1) // 2
    #print(f'm = {m} w * h - {((w // (a + 2 * m)) * (h // (b + 2 * m)))} or {((w // (b + 2 * m)) * (h // (a + 2 * m)))}')
    if (((w // (a + 2 * m)) * (h // (b + 2 * m))) >= n or ((w // (b + 2 * m)) * (h // (a + 2 * m))) >= n):
        left = m
    else:
        right = m - 1

print(left)
