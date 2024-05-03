# Python 3.12.1

import sys
sys.setrecursionlimit(100000)

def counting(node, children):
    cnt = 0
    if node in children:
        for ch in children[node]:
            if ch not in finished:
                finished[ch] = counting(ch, children)
            cnt += finished[ch] + 1
    finished[node] = cnt        
    return cnt

all_man = set()
finished = dict()
children = dict()

n = int(input())
for t in range(n - 1):
    ch, parent = input().split()
    if parent not in children:
        children[parent] = []
    children[parent].append(ch)
    all_man.add(parent)

for man in all_man:
    counting(man, children)


for name in sorted(finished):
    print(name, finished[name])
