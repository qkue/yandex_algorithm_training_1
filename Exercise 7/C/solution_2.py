# Python 3.9 (PyPy 7.3.11)
# Симуляция процесса

n, d = map(int, input().split())

students = []
students = list(map(int, input().split()))
cnt = 1
for i in range(len(students)):
    students[i] = (students[i], cnt) # number of seats
    cnt += 1
students.sort()

ticket = [students[0][0] + d]
list_tickets = [(students[0][0], students[0][1], 1)]
max_type_tickets = 1


for i in range(1, len(students)):
    flag_find = 0
    for t in range(len(ticket)):
        if students[i][0] > ticket[t]:
            ticket[t] = students[i][0] + d
            list_tickets.append((students[i][0], students[i][1], t + 1))
            flag_find = 1
            break

    if not flag_find:
        ticket.append(students[i][0] + d)
        list_tickets.append((students[i][0], students[i][1], len(ticket)))
        max_type_tickets += 1


list_tickets.sort(key = lambda p: p[1])
ans = []
for elem in list_tickets:
    ans.append(str(elem[2]))
print(max_type_tickets)
print(' '.join(ans))
