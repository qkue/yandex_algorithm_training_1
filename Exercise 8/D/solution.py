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

pre_ans = []
def walking(binary, x = 0):
    if binary == None:
        return
    walking(binary[1][0], 0)
    pre_ans.append(binary[0])
    walking(binary[1][1], 1)

walking(binary)

print('\n'.join(str(a) for a in pre_ans))
