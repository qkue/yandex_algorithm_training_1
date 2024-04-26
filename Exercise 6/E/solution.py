# Python 3.12.1

a = int(input())
b = int(input())
c = int(input())

left = 0
right = 10 ** 18
grade_cnt = sum([a, b, c])
while left < right:
    m = (left + right) // 2
    if (35 * (grade_cnt + m)) <= (2 * a + 3 * b + 4 * c + 5 * m) * 10:
        right = m
    else:
        left = m + 1
print(left)
