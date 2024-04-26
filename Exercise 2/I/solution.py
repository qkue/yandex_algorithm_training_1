# Python 3.12.1

n, m, k = list(map(int, input().split()))
mine = [tuple(map(int, input().split())) for _ in range(k)]

field = [[0 for _ in range(m)] for _ in range(n)]

for p, q in mine:
    field[p-1][q-1] = '*'
    for row in range(max(0, p - 2), min(p+1, n)):
        for col in range(max(0, q - 2), min(q+1, m)):
            if field[row][col] != '*':
                field[row][col] += 1



for row in field:
    print(*row)
