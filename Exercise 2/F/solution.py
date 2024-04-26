# Python 3.12.1

def testing(seq):
    ans = []
    left = 0
    right = -1
    for i in range(len(seq)):
        if seq[left] == seq[right] and left == n-1:
            break
        elif seq[left] == seq[right] and seq[left:] == list(reversed(seq[left:])):
            #print(f'left seq - {seq[left+1:n // 2]} -- right seq - {seq[right - 1:(n // 2 - 1): -1]}')
            break   
        else:
            ans.append(seq[left])
            left += 1
    ans.reverse()        
    return ans

n = int(input())
arr = list(map(int, input().split()))
res = testing(arr)
print(len(res))
print(*res)
