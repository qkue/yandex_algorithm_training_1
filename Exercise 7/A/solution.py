# Python 3.12.1

n, m = map(int, input().split())

events = []

for i in range(m):
    start_watch, end_watch = map(int, input().split())
    events.append((start_watch, -1)) #IN
    events.append((end_watch, 1)) #OUT

events.sort()
table = 0

looking_for = 0
watch_flag = 0
begin_watching = 0
stop_watching = 0

#looking_for = [0 for _ in range(n)]
for event in range(len(events)):
    if events[event][1] == -1:
        looking_for += 1
        if watch_flag == 0:
            begin_watching = events[event][0]
            watch_flag = 1
    
    elif events[event][1] == 1:
        looking_for -= 1
    
    if looking_for == 0:
        stop_watching = events[event][0]
        table += stop_watching - begin_watching + 1
        watch_flag = 0 

print(n - table)
