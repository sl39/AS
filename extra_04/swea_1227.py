import sys

sys.stdin = open("input.txt")


for _ in range(10):
    T = int(input())
    mat = []
    for i in range(100):
        mat.append(list(map(str,input().strip())))

    for i in range(100):
        for j in range(100):
            if mat[i][j] == "2":
                start = (i,j)
            if mat[i][j] == "3":
                end = (i,j)
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    stack = [start]
    count = 0
    while stack:
        p = stack.pop()
        if end == p:
            count = 1
        for i in range(4):
            nx = dx[i] + p[0]
            ny = dy[i] + p[1]
            if 0<= nx < 100 and 0<= ny < 100 and mat[nx][ny] != "1":
                mat[nx][ny] = "1"
                stack.append((nx,ny))
    print(f"#{T}",count)
            