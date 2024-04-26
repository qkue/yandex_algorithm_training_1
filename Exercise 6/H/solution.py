# Python 3.12.1

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left = 0
right = 10 ** 7

def check(k, m, arr):
    if k <= sum([line // m for line in arr]):
        return True
    else:
        return False

while left < right:
    mid = (left + right + 1) // 2
    
    if check(k, mid, arr):
        left = mid
    else:
        right = mid - 1

print(left)
