# Python 3.12.1

n = int(input())
result = 0
turtle = set()
#temp = 0

for _ in range(n):
#    temp = 0
    forward, back = map(int, input().split())
    if abs(back) + 1 + abs(forward) == n and (forward, back) not in turtle:
        turtle.add((forward, back))
        result += 1

print(result)
