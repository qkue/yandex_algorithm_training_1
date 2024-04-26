# Python 3.12.1

n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

for target in arr_k:
    left = 0
    right = n - 1
    while left < right:
        m = (left + right) // 2
        if arr_n[m] >= target:
            right = m
        else:
            left = m + 1
    if arr_n[left] != target:
        print('NO')
    else:
        print('YES')
