# Python 3.12.1

from sys import stdin

n = int(stdin.readline().strip())
n_list = list(map(int, stdin.readline().split()))
m = int(stdin.readline().strip())
m_list = list(map(int, stdin.readline().split()))

def testing(n, m, n_list, m_list):
    left = 0
    right = 0
    x = 0
    y = 0
    min_delta = 10 ** 9 


    while left < n and right < m:
        delta = abs(n_list[left] - m_list[right])
        if delta < min_delta:
            min_delta = delta
            x = left
            y = right
        
        if n_list[left] < m_list[right]:
            left += 1
        else:
            right += 1

    return (n_list[x], m_list[y])
print(*testing(n, m, n_list, m_list))
