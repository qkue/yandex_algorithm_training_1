# Python 3.12.1

n, L = map(int, input().split())
list_of_seq = [list(map(int, input().split())) for _ in range(n)]
ans = []

for arr in range(n - 1):

    for compare_arr in range(arr + 1, n):
        counter_first = 0
        counter_second = 0
        counter_m = 0
        temp_list = 0

        while counter_m < L:
            if list_of_seq[arr][counter_first] < list_of_seq[compare_arr][counter_second]:
                temp_list = list_of_seq[arr][counter_first]
                counter_first += 1
                

            else:
                temp_list = list_of_seq[compare_arr][counter_second]
                counter_second += 1

            counter_m += 1
        ans.append(temp_list)
print(*ans, sep='\n')
