# Python 3.12.1

def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]

def newnode(mem_struct):
    memory, first_free = mem_struct
    mem_struct[1] = memory[first_free][1]
    return first_free

def delnode(mem_struct, index):
    memory, first_free = mem_struct
    memory[index][1] = first_free
    mem_struct[1] = index

def create_and_fill_node(mem_struct, key):
    index = newnode(mem_struct)
    mem_struct[0][index][0] = key
    mem_struct[0][index][1] = -1
    mem_struct[0][index][2] = -1
    return index


def add(mem_struct, root, x, level = 2):
    key = mem_struct[0][root][0]
    if x == key:
        return 0
    #global max_level 
    #max_level = max(max_level, level)
    if x < key:
        left = mem_struct[0][root][1]
        if left == -1:
            mem_struct[0][root][1] = create_and_fill_node(mem_struct, x)
            ans.append(level)
        else:
            add(mem_struct, left, x, level + 1)
    elif x > key:
        right = mem_struct[0][root][2]
        if right == -1:
            mem_struct[0][root][2] = create_and_fill_node(mem_struct, x)
            ans.append(level)
        else: 
            add(mem_struct, right, x, level + 1)
    
arr_input = list(map(int, input().split()))
ans = []
mem_struct = initmemory(len(set(arr_input)) - 1)
root = create_and_fill_node(mem_struct, arr_input[0])
if root == 0:
    ans.append(1)
for num in range(1, len(arr_input) - 1):
    #max_level = 0
    add(mem_struct, root, arr_input[num])
    #print(max_level + 1)
print(' '.join(str(a) for a in ans))
#print(mem_struct[0])
