# Python 3.12.1

n = int(input())
result = {}

for _ in range(n):
    left, right = input().split()
    result[left] = right
    result[right] = left

print(result[input()])
