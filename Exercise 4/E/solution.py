# Python 3.12.1

n = int(input())
blocks = {}

for _ in range(n):
    w, h = map(int, input().split())
    if w not in blocks:
        blocks[w] = 0
    if blocks[w] < h:
        blocks[w] = h

blocks_sort_by_keys = sorted(blocks, reverse=True)
result = 0
for block in blocks_sort_by_keys:
    result += blocks[block]
print(result)
