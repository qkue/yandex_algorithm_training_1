# Python 3.12.1

first = input()
second = input()
second_set = {second[ind] + second[ind+1] for ind in range(len(second) - 1)}
result = 0

for ind in range(len(first) - 1):
    pair = first[ind] + first[ind+1]
    if pair in second_set:
        
        result += 1

print(result)
