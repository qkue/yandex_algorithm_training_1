# Python 3.12.1

from collections import deque

n, d = map(int, input().split())
students = ((table, i) for i, table in enumerate(map(int, input().split())))
events = []
for student in students:
    table, num = student
    events.append((table, 0, num))
    events.append((table + d, 1, num))
events.sort()

n_tickets = 0
free_tickets = deque()
assignment = [None] * n
for table, operation, ind in events:
    if operation:
        free_tickets.append(assignment[ind][0])
    else:
        if free_tickets:
            t = free_tickets.popleft()
        else:
            n_tickets += 1
            t = n_tickets
        assignment[ind] = (t, ind)
assignment.sort(key = lambda p: p[1])
print(n_tickets)
ans = []
for ticket in assignment:
    ans.append(str(ticket[0]))
print(' '.join(ans))
