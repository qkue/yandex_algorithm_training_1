# Python 3.12.1

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
count_nums = {}

for elem in arr:
    count_nums[elem] = count_nums.get(elem, 0) + 1

uniq_nums = sorted(count_nums.keys())

last = 0
result = 0
dupl = 0

for first in range(len(uniq_nums)):
    while last < len(uniq_nums) and uniq_nums[first] * k >= uniq_nums[last]:
        if count_nums[uniq_nums[last]] > 1:
            dupl += 1
        last += 1
    len_range = last - first

    if count_nums[uniq_nums[first]] > 1:
        result += (len_range - 1) * 3
    if count_nums[uniq_nums[first]] > 2:
        result += 1
    result += (len_range - 1) * (len_range - 2) * 3
    if count_nums[uniq_nums[first]] > 1:
        dupl -= 1
    result += dupl * 3

print(result)
