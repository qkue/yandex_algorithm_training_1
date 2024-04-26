# Python 3.12.1

n = int(input())
m = int(input())
t = int(input())

left = 0
right = n + m

while left < right:
    mid = (left + right + 1) // 2
    if m - 2 * mid < 0:
        right = mid - 1
        continue
    #print(f'sum {(2 * (n * mid)) + (2 * ((m - 2 * mid) * mid))}')
    if t >= 2 * (n * mid) + 2 * ((m - 2 * mid) * mid):
        left = mid
    else:
        right = mid - 1

print(left)
