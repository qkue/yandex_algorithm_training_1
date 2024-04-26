# Python 3.12.1

latin = 'qazwsxedcrfvtgbyhnujmikolp'
n, k = map(int, input().split())
arr = input()

last = 0
result_lenght = - 10 ** 9
first_letter_array = 0
char_dict = {letter: 0 for letter in latin}

for first in range(n):
    while last < n and char_dict[arr[last]] < k:
        char_dict[arr[last]] += 1
        last += 1
    if last - 1 - first > result_lenght:
        result_lenght = last - 1 - first
        first_letter_array = first + 1
    #result_lenght = (last - 1 - first) if last - 1 - first > result_lenght else result_lenght
    
    char_dict[arr[first]] -= 1
    #print(result_lenght, char_dict)
print(result_lenght + 1, first_letter_array)
