# Python 3.12.1

n, m = map(int, input().split())

events = []

for _ in range(n):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    events.append((start, -1)) #IN
    events.append((end, 1)) #OUT

points = list(map(int, input().split()))
for point in range(len(points)):
    events.append((points[point], 0, point)) # point, priority, place in start input

events.sort()
include_points = []
cnt_section = 0

for i in range(len(events)):
    if events[i][1] == -1:
        cnt_section += 1
    elif events[i][1] == 1:
        cnt_section -= 1
    elif events[i][1] == 0:
        include_points.append((cnt_section, events[i][2]))
include_points.sort(key=lambda x: x[1])
for ans in include_points:
    print(ans[0], end=' ')
