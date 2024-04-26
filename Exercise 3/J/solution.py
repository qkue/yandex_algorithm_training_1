# Python 3.12.1

def extend(rect, d):
    min_plus, max_plus, min_minus, max_minus = rect
    return [min_plus - d, max_plus + d, min_minus - d, max_minus + d]

def intersect(rect1, rect2):
    ans = [max(rect1[0], rect2[0]), min(rect1[1], rect2[1]), max(rect1[2], rect2[2]), min(rect1[3], rect2[3])]
    return ans

t, d, n = map(int, input().split())
pos_rect = (0, 0, 0, 0)

for _ in range(n):
    pos_rect = extend(pos_rect, t)
    nav_x, nav_y = map(int, input().split())
    nav_rect = extend((nav_x + nav_y, nav_x + nav_y, nav_x - nav_y, nav_x - nav_y), d)
    pos_rect = intersect(pos_rect, nav_rect)

points = []

for x_plus_y in range(pos_rect[0], pos_rect[1] + 1):
    for x_minus_y in range(pos_rect[2], pos_rect[3] + 1):
        if (x_plus_y + x_minus_y) % 2 == 0:
            x = (x_plus_y + x_minus_y) // 2
            y = x_plus_y - x
            points.append((x, y))

print(len(points))
for point in points:
    print(*point)
