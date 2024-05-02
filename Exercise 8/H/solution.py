# Python 3.12.1

binary = []

#добавление корня дерева
def root(binary, x):
    binary = [x, [None, None]]
    return binary

#добавление нового элемента дерева
def ad_in_binary(binary, x):
    key=binary[0]
    if x < key:
        if binary[1][0] == None:
            binary[1][0] = [x, [None, None]]
        else:
            ad_in_binary(binary[1][0], x)
    if x > key:
        if binary[1][1] == None:
            binary[1][1] = [x, [None, None]]
        else:
            ad_in_binary(binary[1][1], x)               
    return binary
s = list(map(int, input().split()))

binary = root(binary, s[0])
i = 1

while s[i] != 0:
    binary = ad_in_binary(binary, s[i])
    i = i + 1

balance_list = []
def walking(binary, x = 0):
    if binary == None:
        return 0
    left_walk = walking(binary[1][0], 0)
    res_left = left_walk
    right_walk = walking(binary[1][1], 1)
    res_right = right_walk
    balance = 0
    if abs(res_left - res_right) <= 1:
        balance = True
    balance_list.append(balance)
    return max(res_left, res_right) + 1

walking(binary)
print('YES' if 0 not in set(balance_list) else 'NO')
