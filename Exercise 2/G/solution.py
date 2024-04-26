# Python 3.12.1

arr = list(map(int, input().split()))

arr.sort()

x1 = arr[0]
x2 = arr[1]
y1 = arr[-1]
y2 = arr[-2]

if x1 * x2 > y1 * y2:
	print(x1, x2)
else:
	print(y2, y1)
