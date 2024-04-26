# Python 3.12.1

a = int(input())
b = int(input())
n = int(input())
m = int(input())

best_a = n + a * (n - 1)
best_b = m + b * (m - 1)
best_ab = max(best_a, best_b)

worst_a = n + a * (n + 1)
worst_b = m + b * (m + 1)
worst_ab = min(worst_a, worst_b)

if worst_ab < best_ab:
	print(-1)
else:
	print(best_ab, worst_ab)
