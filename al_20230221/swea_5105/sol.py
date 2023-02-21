import sys
sys.stdin = open("sample_input.txt")

from collections import deque

TC = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for T in range(1,TC+1):
    n = int(input())
    mat = [list(map(int,list(input()))) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 2:
                start =(i,j)
                mat[i][j] = 0
            if mat[i][j] == 3:
                end = (i,j)

    res = 0
    stack = deque([start])
    while stack:
        x,y = stack.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx< n and 0<= ny < n:
                if mat[nx][ny] == 0:
                    stack.append((nx,ny))
                    mat[nx][ny] = mat[x][y] + 1
                elif (nx,ny) == end:
                    res = mat[x][y]
                    break
        if res:
            break
    print(f"#{T}",res)