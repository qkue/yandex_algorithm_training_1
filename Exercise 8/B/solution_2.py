# Python 3.12.1
# Решение с просторов интернета, оно мне понравилось больше чем своё и оно ближе к лекции

binary=[]

#добавление корня дерева
def root(binary,x):
    binary=[x,[None,None]]
    return binary

#добавление нового элемента дерева
def ad_in_binary(binary,x):
    key=binary[0]
    if x<key:
        if binary[1][0]==None:
            binary[1][0]=[x,[None,None]]
        else:
            ad_in_binary(binary[1][0],x)
    if x>key:
        if binary[1][1]==None:
            binary[1][1]=[x,[None,None]]
        else:
            ad_in_binary(binary[1][1],x)               
    return binary

s=str(input()).split()
s=list(map(lambda x:int(x), s))
binary=root(binary,s[0])
i=1
while s[i]!=0:
    binary=ad_in_binary(binary,s[i])
    i=i+1
def floor(binary,x):
    key=binary[0]
    if x==key:
        return 1
    elif x<key:
        return floor(binary[1][0],x)+1
    elif x>key:
        return floor(binary[1][1],x)+1
i=0
sets=set()
while s[i]!=0:
    if s[i] not in sets:
        sets.add(s[i])
        print(floor(binary,s[i]), end=' ')
    i=i+1
