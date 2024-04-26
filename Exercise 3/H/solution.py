# Python 3.12.1

n = int(input())
result = 0

birds = [tuple(map(int, input().split())) for _ in range(n)]
birds.sort(key = lambda x: (x[0], -x[1]))

shoot = set()
for x, y in birds:
    if x not in shoot:
        shoot.add(x)
        result += 1

print(result)
