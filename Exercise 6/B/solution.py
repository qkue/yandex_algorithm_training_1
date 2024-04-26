# Python 3.12.1

n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

for target in arr_k:
    left = 0
    right = n - 1
    while left < right:
        m = (left + right + 1) // 2
        #if target - arr_n[m] 
        if arr_n[m] <= target:
            left = m
        else:
            right = m - 1
    if abs(target - arr_n[left]) <= abs(target - arr_n[min(left + 1, n - 1)]):
        print(arr_n[left])
    else:
        print(arr_n[left + 1])
