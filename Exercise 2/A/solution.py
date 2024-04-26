# Python 3.12.1

arr = list(map(int, input().split()))

last_seen = 0
flag_seq = 0

if len(arr) > 0:
    last_seen = arr[0]
for i in arr[1:]:
    if last_seen >= i:
        flag_seq = 1
        break
    last_seen = i

if flag_seq:
    print('NO')
else:
    print('YES')
