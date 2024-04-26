# Python 3.12.1

n, k, m = map(int, input().split())

result = 0

while n >= k:
	all_k = n // k
	if not all_k:
		break
    	
	n %= k
	detail = all_k * (k // m)
	if not detail:
		break
	result += detail
	n += (all_k * k) - (detail * m)
    
print(result)
