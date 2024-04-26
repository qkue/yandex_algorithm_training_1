# Python 3.12.1

n = int(input())
prev = float(input())
left = 30.0
right = 4000.0

for row in range(n-1):
    new, text = input().strip().split()
    new = float(new)
    if text == 'closer':
        if new < prev:
            right = min(right, ((new + prev) / 2))
        else:
            left = max(left, ((new + prev) / 2))
    else:
        if new > prev:
            right = min(right, ((new + prev) / 2))
        else:
            left = max(left, ((new + prev) / 2))
    prev = new

print(left, right)
