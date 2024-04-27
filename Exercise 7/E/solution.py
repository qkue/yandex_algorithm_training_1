# Python 3.12.1

n = int(input())

events = []
answer = 0

for i in range(n):
    open_h, open_m, close_h, close_m = map(int, input().split())
    if open_h * 60 + open_m > close_h * 60 + close_m:
        op = open_h * 60 + open_m
        cl = close_h * 60 + close_m
        events.append((op, - 1, i))
        events.append((24 * 60, 1, i))
        events.append((0, - 1, i))
        events.append((cl, 1, i))
        continue

    if open_h == close_h and open_m == close_m:
        open_h, open_m = 0, 0
        close_h, close_m = 24, 0
     
    events.append((open_h * 60 + open_m, -1, i)) # IN
    events.append((close_h * 60 + close_m, 1, i)) # OUT
events.sort()
open_ticket_office = set()
#print(events)

# first pass
for incident in range(len(events)):
    #if events[incident][0] <= 3600:
    if events[incident][1] == -1:
        open_ticket_office.add(events[incident][2])
    elif events[incident][1] == 1 and events[incident][2] in open_ticket_office:
        open_ticket_office.remove(events[incident][2])

#print(open_ticket_office)

total_time = 0
time_start = 0
#time_stop = 0

# second pass
for incident in range(len(events)):
    if events[incident][1] == -1:
        open_ticket_office.add(events[incident][2])
        if len(open_ticket_office) == n:
            time_start = events[incident][0]
            #print(time_start)

    if events[incident][1] == 1 and events[incident][2] in open_ticket_office:
        if len(open_ticket_office) == n:
            total_time += events[incident][0] - time_start
        open_ticket_office.remove(events[incident][2])
        
#print(open_ticket_office)
print(total_time)
