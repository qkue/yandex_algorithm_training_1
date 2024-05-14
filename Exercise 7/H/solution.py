# Python 3.12.1

answer = []
for _ in range(int(input())):

    test = list(map(int, input().split()))
    n = test[0]
    events = []

    cnt = 0
    for i in range(1, len(test), 2):
        start, end = test[i], test[i+1]
        events.append((start, -1, cnt)) # IN
        events.append((end, 1, cnt)) # OUT
        cnt += 1
    events.sort()

    alone = set()
    guardians = set()
    nobody = False
    for i in range(len(events)):
        if i == 0:
            guardians.add(events[i][2])
            if events[i][0] > 1:
                nobody = True
                break
            continue
        
        if len(guardians) == 1 and events[i][0] - events[i - 1][0] > 0:
            alone.update(guardians)
        
        if events[i][1] == -1:
            if len(guardians) == 0 and events[i][0] - events[i - 1][0] > 0:
                nobody = True
                break
            guardians.add(events[i][2])
        elif events[i][1] == 1:
            guardians.remove(events[i][2])

    if nobody or len(alone) != n or events[-1][0] < 10000:
        answer.append('Wrong Answer')
    else:
        answer.append('Accepted')

print('\n'.join(answer))
