# Python 3.12.1

x, y, z = map(int, input().split())
n = (input())
n_symbols = {int(num) for num in n}
#print(n_symbols)
dif_num = n_symbols - {x, y, z}
print(len(dif_num))
