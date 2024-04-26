# Python 3.12.1

n, k = map(int, input().split())

arr = list(map(int, input().split()))

result = 0
delta = 0
last = 0

for first in range(n):
	while last < n and (last == first or delta + arr[last] <= k):
		if delta + arr[last] == k:
			result += 1
			break
		delta += arr[last]
		last += 1
	delta -= arr[first]
        
print(result)
