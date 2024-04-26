a = int(input())
b = int(input())
c = int(input())

print('YES' if all([a < b + c, b < a + c, c < b + a]) else 'NO')
