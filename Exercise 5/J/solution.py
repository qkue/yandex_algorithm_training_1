# Python 3.9 (PyPy 7.3.11)

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
result = 0

for ind in range(n):
    used_points = set()
    neig = []

    for j in range(n):
        x = points[ind][0] - points[j][0]
        y = points[ind][1] - points[j][1]
        length = x ** 2 + y ** 2
        neig.append(length)
        if (x, y) in used_points:
            result -= 1
        used_points.add((-x, -y))

    neig.sort()
    
    last = 0
    for first in range(len(neig)):
        while last < len(neig) and neig[last] == neig[first]:
            last += 1
        result += last - first - 1

print(result)
