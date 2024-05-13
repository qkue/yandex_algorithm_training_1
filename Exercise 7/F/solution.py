# Python 3.12.1

def leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def calculateAge(year_b, month_b, day_b, year_d, month_d, day_d):
    age = 0
    check_adult = year_d, month_b, day_b
    if not leap_year(year_d) and month_b == 2 and day_b == 29:
        check_adult = year_d, month_b + 1, 1
    
    if check_adult[1] > month_d or (check_adult[1] == month_d and check_adult[2] > day_d):
        age = year_d - year_b - 1
    else:
        age = year_d - year_b 
    
    if age >= 18:
        start = year_b + 18, month_b, day_b
        if leap_year(year_b) and month_b == 2 and day_b == 29 and not leap_year(year_b + 18):
            start = year_b + 18, month_b + 1, 1

        end = (year_d, month_d, day_d)
        if age >= 80:
            end = year_b + 80, month_b, day_b
            if leap_year(year_b) and month_b == 2 and day_b == 29 and not leap_year(year_b + 80):
                end = year_b + 80, month_b + 1, 1

        return (start, end)
    else:
        return 0, 0

n = int(input())
events = []

for i in range(1, n + 1):
    d_b, m_b, y_b, d_d, m_d, y_d = map(int, input().split())
    birth, last = calculateAge(y_b, m_b, d_b, y_d, m_d, d_d)
    if birth != 0 and last != 0 and birth != last:
        events.append((birth, 1, i))
        events.append((last, -1, i))
events.sort()
#print(events)
#print()
#print()
flag = False
answer = []
contemporary = set()
for event in events:
    if event[1] == 1:
        contemporary.add(event[2])
        flag = True
    elif event[1] == -1:
        if flag:
        #if not any([contemporary.issubset(elem) for elem in answer]):
            answer.append(contemporary.copy())
            flag = False
        contemporary.remove(event[2])
if answer:
    for people in answer:
        print(*people)
else:
    print(0)
