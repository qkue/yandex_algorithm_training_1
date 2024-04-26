# Python 3.12.1

arr = list(map(int, input().split()))

arr.sort()

x1 = arr[-1]
x2 = arr[-2]
x3 = arr[-3]

y1 = arr[0]
y2 = arr[1]
y3 = arr[2]

ans1 = x1 * x2 * x3
ans2 = x1 * y2 * y1


if ans1 > ans2:
	print(x1, x2, x3)
else:
	print(x1, y2, y1)
