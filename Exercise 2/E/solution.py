# Python 3.12.1

n = int(input())
arr = list(map(int, input().split()))

winner = arr.index(max(arr))
result = 0

for num in range(1, len(arr) - 1):
        if num > winner and ((arr[num] + 5) % 10) == 0 and arr[num+1] < arr[num] and arr[num] > result:

            result = arr[num]

if result:
    arr.sort(reverse=True)
    result = arr.index(result) + 1

print(result)
