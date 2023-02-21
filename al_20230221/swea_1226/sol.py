import sys
sys.stdin = open("input.txt")

from collections import deque


dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(10):
    T = int(input())
    mat = [list(map(int,list(input()))) for i in range(16)]
    for i in range(16):
        for j in range(16):
            if mat[i][j] == 2:
                start = (i,j)
            if mat[i][j] == 3:
                end = (i,j)
    q = deque([start])
    res = 0
    while q:
        x,y = q.popleft()
        if (x,y) == end:
            res = 1
            break
        for i in range(4):
            nx = dx[i] +x
            ny = dy[i] +y
            if 0<= nx< 16 and 0<= ny < 16 and mat[nx][ny] != 1:
                q.append((nx,ny))
                mat[nx][ny] = 1

    print(f"#{T}", res)
