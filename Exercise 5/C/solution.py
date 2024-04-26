# Python 3.12.1

n = int(input())
mountain = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
trace = [list(map(int, input().split())) for _ in range(m)]

prefix_mountain = [0 for _ in range(n)]
for i in range(1, n):
    now = mountain[i][1]
    prev = mountain[i-1][1]
    prefix_mountain[i] = prefix_mountain[i - 1] + ((now - prev) if prev < now else 0)

prefix_mountain_reverse = [0 for _ in range(n)]
for i in range(n-2, -1, -1):
    now = mountain[i][1]
    prev = mountain[i+1][1]
    prefix_mountain_reverse[i] = prefix_mountain_reverse[i+1] + ((now - prev) if now > prev else 0)

result = []

for points in trace:
    left, right = points
    if left < right:
        result.append(prefix_mountain[right-1] - prefix_mountain[left-1])        
    elif right < left:
        result.append(prefix_mountain_reverse[right - 1] - prefix_mountain_reverse[left - 1])
    else:
        result.append(0)

print(*result, sep='\n')
