# Python 3.12.1
# Понравилось решение от лектора, что можно не моделировать полные сутки а ограничиться проходом по первым суткам и прибавить автобусы в пути. Моё решение немного побольше :-)

n, m = map(int, input().split())
depo = [0] * (n + 1)
buses = 0
route = []
on_the_way = set()

# input data
for i in range(m):
    f, x, g, y = input().split()
    route.append((int(''.join(x.split(':'))), 1, int(f), i + 1)) # DEPARTURE
    route.append((int(''.join(y.split(':'))), -1, int(g), i + 1)) # ARRIVE

route.sort()
#print(route)

# first pass
for bus_stop in route:
    if bus_stop[1] == -1 and bus_stop[3] in on_the_way:
        on_the_way.remove(bus_stop[3])
        depo[bus_stop[2]] += 1
    elif bus_stop[1] == 1:
        if depo[bus_stop[2]] == 0:
            buses += 1
            depo[bus_stop[2]] += 1
        depo[bus_stop[2]] -= 1
        on_the_way.add(bus_stop[3])
# print('first pass')
# print('depo', depo)
# print('buses', buses)
# print('on the way', on_the_way)

#second pass
for bus_stop in route:
    if bus_stop[1] == -1:
        on_the_way.remove(bus_stop[3])
        depo[bus_stop[2]] += 1
    elif bus_stop[1] == 1:
        if depo[bus_stop[2]] == 0:
            buses += 1
            depo[bus_stop[2]] += 1
        depo[bus_stop[2]] -= 1
        on_the_way.add(bus_stop[3])
    
# print('second pass')
# print('depo', depo)
# print('buses', buses)
# print('on the way', on_the_way)
# print('answer =', buses)

# third pass - control
answer = buses

for bus_stop in route:
    if bus_stop[1] == -1:
        on_the_way.remove(bus_stop[3])
        depo[bus_stop[2]] += 1
    elif bus_stop[1] == 1:
        if depo[bus_stop[2]] == 0:
            buses += 1
            break
            depo[bus_stop[2]] += 1
        depo[bus_stop[2]] -= 1
        on_the_way.add(bus_stop[3])

if answer != buses:
    print(-1)
else:
    print(buses)
