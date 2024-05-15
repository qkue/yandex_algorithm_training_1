# Python 3.12.1
# Начал через координаты делать, запутался и получалось огромное. Оказывается с площадью решение очень простое. 

n, w, L = map(int, input().split())
events = []

for i in range(1, n + 1):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    S = abs(y2 - y1) * abs(x2 - x1)
    events.append((z1, 1, S, i))
    events.append((z2, -1, S, i))
events.sort()

now_S = 0
full_S = w * L
best_cnt = n + 1
now_cnt = 0

#print(events)
for event in events:
    if event[1] == 1:
        now_cnt += 1
        now_S += event[2]
        
        if now_S == full_S and now_cnt < best_cnt:
            best_cnt = now_cnt
    elif event[1] == -1:
        now_cnt -= 1
        now_S -= event[2]

if best_cnt == n + 1:
    print('NO')
else:
    print('YES')
    print(best_cnt)
    blocks = set()
    for event in events:
        if event[1] == 1:
            now_cnt += 1
            blocks.add(event[3])
            now_S += event[2]
            
            if now_S == full_S and now_cnt == best_cnt:
                print(*blocks)
                break
        elif event[1] == -1:
            now_cnt -= 1
            blocks.remove(event[3])
            now_S -= event[2]
