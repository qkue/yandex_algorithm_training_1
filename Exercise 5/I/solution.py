# Python 3.12.1

n = int(input())
arr = input()

result = 0
cum_pref = 0

for letter in range(n, len(arr)):
    if arr[letter] == arr[letter - n]:
        cum_pref += 1
        result += cum_pref
    else:
        cum_pref = 0

print(result)
