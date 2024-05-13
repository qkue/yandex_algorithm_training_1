# Python 3.12.1
# Нашёл интересное решение. Оказывается, можно не проверять даты на високосный год и 29 февраля, а просто прибавлять, такого я не ожидал

def F_coeval(dates):
    new_people, now_people = False, []
    for y, m, d, type, i in dates:
        if type == 1:  # 18 годиков
            now_people.append(i)
            new_people = True
        else:       # смерть или 80 годиков
            if new_people:
                print(*now_people)
                new_people = False
            now_people.remove(i)
 
if __name__ == '__main__':
    dates, n = [], int(input())
 
    for i in range(n):  
        date = list(map(int, input().split()))

        coming_of_age = [date[2] + 18, date[1], date[0], 1, i+1] #смерть или 80 лет - 0, совершеннолетие - 1
        death = [date[5], date[4], date[3], 0, i+1]
        if coming_of_age < death:  # человеку при смерти должно быть больше 18
            dates.append(coming_of_age)
            old = [date[2]+80, date[1], date[0], 0, i+1]
            if death < old:  # что наступило раньше смерть или 80 лет?
                dates.append(death)
            else:
                dates.append(old)

    if dates == []:
        print(0)
    else:
        F_coeval(sorted(dates))
