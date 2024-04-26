# Python 3.12.1

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a, b, c = sorted((a, b, c))
if d > e:
	d, e = e, d
    
if a <= d and b <= e:
	print('YES')
else:
	print('NO')
