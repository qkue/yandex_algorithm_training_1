# Python 3.12.1

def counting(node, children):
    if node not in children:
        finished[node] = 0
        return 0
    parent = children[node]
    if parent in finished:
        cnt = finished[parent] + 1
    else:
        cnt = counting(parent, children) + 1
    finished[node] = cnt
    return cnt

all_man = set()
finished = dict()
children = dict()

n = int(input())

for t in range(n - 1):
    ch, parent = input().split()
    children[ch] = parent
    all_man.add(parent)
    all_man.add(ch)

for man in all_man:
    counting(man, children)

for name in sorted(finished):
    print(name, finished[name])
