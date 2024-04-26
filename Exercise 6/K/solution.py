# Python 3.9 (PyPy 7.3.11)

n, L = map(int, input().split())
list_of_seq = []

# создаём необходимые списки из входных данных
for _ in range(n):
    x, d, a, c, m = map(int, input().split())
    row_numbers = [x]
    for number in range(L - 1):
        x = x + d
        d = ((a * d + c) % m)
        
        row_numbers.append(x)
    list_of_seq.append(row_numbers)

ans = []

def count_lt(seq, m):
    left_num = 0
    right_num = L - 1
    while left_num < right_num:
        mid_num = (left_num + right_num) // 2
        if seq[mid_num] >= m:
            right_num = mid_num
        else:
            left_num = mid_num + 1
    
    if seq[left_num] < m:
        return L
    return left_num

for arr in range(n - 1):

    for compare_arr in range(arr + 1, n):
        pre_answer = None
        left = min(list_of_seq[arr][0], list_of_seq[compare_arr][0])
        right = max(list_of_seq[arr][-1], list_of_seq[compare_arr][-1])
        while left < right:
            mid = (left + right) // 2
            less = count_lt(list_of_seq[arr], mid) + count_lt(list_of_seq[compare_arr], mid)
            great = (L - count_lt(list_of_seq[arr], mid + 1)) + (L - count_lt(list_of_seq[compare_arr], mid + 1))

            if less <= L - 1 and great <= L:
                pre_answer = mid
                break
            
            if great > L:
                left = mid + 1
            if less > L - 1:
                right = mid - 1
        
        if pre_answer is None:
            pre_answer = left


        ans.append(pre_answer)
print(*ans, sep='\n')
