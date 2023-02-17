import sys
sys.stdin = open("sample_input.txt")
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

TC = int(input())
for T in range(1,TC+1):
    mat = []
    n,m = map(int,input().split())
    for i in range(n):
        mat.append(list(map(int,input().split)))
    
    houses = deque([])

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                mat[i][j] = m - 1
                houses.append((i,j))
    
    while houses:
        h = houses.popleft()


cost = 1 + 2*(k-1)*k

