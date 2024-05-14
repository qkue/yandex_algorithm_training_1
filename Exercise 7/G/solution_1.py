# Python 3.12.1
# Интересное решение на куче

import heapq
 
m,n = map(int, input().split())
t,z,y = map(list,zip(*[map(int, input().split()) for _ in range(n)]))

counter = [0]*n
times = list(zip(t,range(n)))
heapq.heapify(times)
next_time = 0
for _ in range(m):
    next_time, i = heapq.heappop(times)
    counter[i] += 1
    heapq.heappush(times, (next_time + t[i] + y[i]*(counter[i]%z[i]==0), i))
    
print(next_time)
print(*counter)
