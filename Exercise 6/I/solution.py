# Python 3.12.1

n, r, c = map(int, input().split())
height = [int(input()) for _ in range(n)]
height.sort()

left = 0
right = height[-1]

def check(m, arr, n, c):
    count = 0
    teams = 0
    while count < n - c + 1:
        if arr[count + c - 1] - arr[count] <= m:
            teams += 1
            count += c
        else:
            count += 1
    return teams

while left < right:
    mid = (left + right) // 2
    if check(mid, height, n, c) >= r:
        right = mid
    else:
        left = mid + 1

print(left)
