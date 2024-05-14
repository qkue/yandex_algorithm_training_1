# Python 3.12.1
# Проверочных тестов мало и они явно маленькие

m, n = map(int, input().split())
volunteers = []
time_dict = {}
count_ballons = [0] * n
ballons = 0
time = 0

for i in range(n):
    t, z, y = map(int, input().split())
    volunteers.append((t, z, y))
    time_dict[t] = time_dict.get(t, []) + [i]

while ballons != m:
    for volunteer in time_dict.get(time, []):
        ballons += 1
        count_ballons[volunteer] += 1
        if ballons == m:
            break
        t, z, y = volunteers[volunteer]
        next_move = time + y * (count_ballons[volunteer] % z == 0) + t
        time_dict[next_move] = time_dict.get(next_move, []) + [volunteer]
    
    time += 1 if ballons < m else 0

print(time)
print(*count_ballons)
