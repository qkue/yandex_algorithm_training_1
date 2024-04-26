# Python 3.12.1

n = int(input())

keyboard = dict()
keys_push = list(map(int, input().split()))

for i in range(1, n+1):
    keyboard[i] = keys_push[i-1]

push = int(input())
key_seq = list(map(int, input().split()))

for key in key_seq:
    keyboard[key] -= 1

for key in keyboard:
    print('YES' if keyboard[key] < 0 else 'NO')
