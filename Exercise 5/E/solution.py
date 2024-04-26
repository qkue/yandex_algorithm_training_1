# Python 3.12.1

n, k = map(int, input().split())

arr = list(map(int, input().split()))

pair_dict = {}
last = 0

number_set = set()
char_dict = {}

for first in range(n):
    while last < n and len(number_set) < k:
        number_set.add(arr[last])
        char_dict[arr[last]] = char_dict.get(arr[last], 0) + 1
        last += 1
        
    if len(number_set) == k:
        pair_dict[last - 1 -first] = [first+1, last]

    char_dict[arr[first]] -= 1
    if not char_dict[arr[first]]:
        number_set.remove(arr[first])

min_key = sorted(pair_dict)[0]
print(*pair_dict[min_key])
