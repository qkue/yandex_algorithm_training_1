# Python 3.12.1

constant = 1
ascending = 1
weakly_ascending = 1
descending = 1
weakly_descending = 1
random = 1

input_num = int(input())
last_seen = input_num

while True:
    input_num = int(input())
    if input_num == (-2 * 10 ** 9):
        break
    if input_num != last_seen:
        constant = 0
    if input_num == last_seen:
        ascending = 0
        descending = 0
    if input_num < last_seen:
        weakly_ascending = 0
        ascending = 0
    if input_num > last_seen:
        weakly_descending = 0
        descending = 0
    last_seen = input_num

if constant:
    print('CONSTANT')
elif ascending:
    print('ASCENDING')
elif weakly_ascending:
    print('WEAKLY ASCENDING')
elif descending:
    print('DESCENDING')
elif weakly_descending:
    print('WEAKLY DESCENDING')
else:
    print('RANDOM')
